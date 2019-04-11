import requests
import re
import tempfile
from lxml import etree
from Utils import CertData, Certificate

NAMESPACE_NFE = 'http://www.portalfiscal.inf.br/nfe'
NAMESPACE_NFE_PREFEITURA = 'http://www.prefeitura.sp.gov.br/nfe'
NAMESPACE_SIG = 'http://www.w3.org/2000/09/xmldsig#'
NAMESPACE_SOAP = 'http://www.w3.org/2003/05/soap-envelope'
NAMESPACE_XSI = 'http://www.w3.org/2001/XMLSchema-instance'
NAMESPACE_XSD = 'http://www.w3.org/2001/XMLSchema'
NAMESPACE_METODO = 'http://www.portalfiscal.inf.br/nfe/wsdl/'
NAMESPACE_METODO_PREFEITURA = 'http://www.prefeitura.sp.gov.br/nfe'

NFSE = {
    'AUTORIZACAO': 'https://nfe.prefeitura.sp.gov.br/ws/lotenfe.asmx'
}    # Prefeitura nao possui ambiente de homologacao para nfse

NFE = {
        'SP': {
        'STATUS': 'nfe.fazenda.sp.gov.br/ws/nfestatusservico4.asmx',
        'AUTORIZACAO': 'nfe.fazenda.sp.gov.br/ws/nfeautorizacao4.asmx',
        'RECIBO': 'nfe.fazenda.sp.gov.br/ws/nferetautorizacao4.asmx',
        'CHAVE': 'nfe.fazenda.sp.gov.br/ws/nfeconsultaprotocolo4.asmx',
        'INUTILIZACAO': 'nfe.fazenda.sp.gov.br/ws/nfeinutilizacao4.asmx',
        'EVENTOS': 'nfe.fazenda.sp.gov.br/ws/nferecepcaoevento4.asmx',
        'CADASTRO': 'nfe.fazenda.sp.gov.br/ws/cadconsultacadastro4.asmx',
        'HTTPS': 'https://',
        'HOMOLOGACAO': 'https://homologacao.'
        },
        'PREFEITURA': {
        'CADASTRO': 'nfe.prefeitura.sp.gov.br/ws/lotenfe.asmx',
        'AUTORIZACAO': 'nfe.prefeitura.sp.gov.br/ws/lotenfe.asmx',
        'CANCELAMENTO': 'nfe.prefeitura.sp.gov.br/ws/lotenfe.asmx',
        'CONSULTA': 'nfe.prefeitura.sp.gov.br/ws/lotenfe.asmx',
        'HTTPS': 'https://',
        }
    }


class PostXML:

    def __init__(self, uf, cert, key):
        self.uf = uf
        self.ambiente = 2 if uf == "SP" else 1
        self.cert = cert
        self.key = key
        self.orgao_publico = ["SP", "PREFEITURA"]

    def _get_url(self, consulta):
        lista = ['SP', 'PREFEITURA']
        if self.uf.upper() in lista:
            if self.ambiente == 1:
                ambiente = 'HTTPS'
                self.url = NFE[self.uf.upper()][ambiente] + NFE[self.uf.upper()][consulta]
            else:
                ambiente = 'HOMOLOGACAO'
                self.url = NFE[self.uf.upper()][ambiente] + NFE[self.uf.upper()][consulta]
        return self.url

    def _post_header(self):
        response = {
            'content-type': 'application/soap+xml; charset=utf-8;',
            'Accept': 'application/soap+xml; charset=utf-8;',
        }
        return response

    def _post(self, url, xml):

        try:
            xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>'
            xml = re.sub(
                '<qrCode>(.*?)</qrCode>',
                lambda x: x.group(0).replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', ''),
                etree.tostring(xml, encoding='unicode').replace('\n', '')
            )
            xml = xml_declaration + xml

            # Must create cert and key with white spaces :
            with open(self.cert, "rb") as certBuffer:
                certBuffer = certBuffer.read()
            with open(self.key, "rb") as keyBuffer:
                keyBuffer = keyBuffer.read()

            with tempfile.NamedTemporaryFile(delete=False) as arqcert:
                arqcert.write(certBuffer)
            with tempfile.NamedTemporaryFile(delete=False) as arqchave:
                arqchave.write(keyBuffer)

            cert_key = (arqcert.name, arqchave.name)
            result = requests.post(url, xml, headers=self._post_header(),
                                   cert=cert_key, verify=False)
            print("Request Status: ", result.status_code)
            print(result.content)
            result.encoding = 'utf-8'
            return result
        except requests.exceptions.RequestException as e:
            raise e

    def _construir_xml_soap(self, metodo, dados, orgao_publico, cabecalho=False):
        """Mota o XML para o envio via SOAP"""
        self.orgao_publico = orgao_publico
        if orgao_publico == "SP":
            raiz = etree.Element('{%s}Envelope' % NAMESPACE_SOAP, nsmap={
              'xsi': NAMESPACE_XSI, 'xsd': NAMESPACE_XSD, 'soap': NAMESPACE_SOAP})
            body = etree.SubElement(raiz, '{%s}Body' % NAMESPACE_SOAP)
            # distribuicao tem um corpo de xml diferente
            if metodo == 'NFeDistribuicaoDFe':
                x = etree.SubElement(body, 'nfeDistDFeInteresse', xmlns=NAMESPACE_METODO+metodo)
                a = etree.SubElement(x, 'nfeDadosMsg')
            else:
                a = etree.SubElement(body, 'nfeDadosMsg', xmlns=NAMESPACE_METODO+metodo)
            a.append(dados)
        elif self.orgao_publico == "PREFEITURA":
            raiz = etree.Element('{%s}Envelope' % NAMESPACE_SOAP, nsmap={
                'xsi': NAMESPACE_XSI, 'xsd': NAMESPACE_XSD, 'soap': NAMESPACE_SOAP})
            body = etree.SubElement(raiz, '{%s}Body' % NAMESPACE_SOAP)
            a = etree.SubElement(body, 'ConsultaCNPJRequest', xmlns=NAMESPACE_METODO_PREFEITURA)
            a.append(dados)
        else:
            return "Nao foi possivel verificar tipo de servico"

        #print(etree.tostring(raiz))
        return raiz

    def consulta_cadastro(self, cnpj):

            lista_svrs = ['SP', 'PREFEITURA']

            if self.uf.upper() == 'SP':
                url = NFE['SP']['CADASTRO']

                raiz = etree.Element('ConsCad', versao='2.00', xmlns=NAMESPACE_NFE)
                info = etree.SubElement(raiz, 'infCons')
                etree.SubElement(info, 'xServ').text = 'CONS-CAD'
                etree.SubElement(info, 'UF').text = self.uf.upper()
                etree.SubElement(info, 'CNPJ').text = cnpj
                xml = self._construir_xml_soap('CadConsultaCadastro4', raiz, self.uf)
                url = self._get_url(consulta='CADASTRO')
                #print("URL SEFAZ SP: ", url)
                return self._post(url, xml)

            elif self.uf.upper() == 'PREFEITURA':
                url = NFE['PREFEITURA']['CADASTRO']
                raiz = etree.Element('MensagemXML')
                # ToDo verificar schema corretamente!
                #info = etree.SubElement(raiz, 'Cabecalho', versao='4.00', xmlns=NAMESPACE_NFE_PREFEITURA)
                cabecalho = etree.SubElement(raiz, 'Cabecalho', Versao="1")
                #etree.SubElement(cabecalho, 'Versao').text = '1'
                remetente = etree.SubElement(cabecalho, "CNPJRemetente")
                etree.SubElement(remetente, 'CNPJ').text = cnpj
                contribuinte = etree.SubElement(raiz, 'CNPJContribuinte')
                etree.SubElement(contribuinte, 'CNPJ').text = cnpj
                xmlToSign = etree.tostring(raiz)
                signedEnvelope = CertData(certFile=self.cert, keyFile=self.key)
                xmlSigned = signedEnvelope.signWithCert(xmlToSign, key=self.key)
                xmlSigned = (etree.fromstring(xmlSigned))
                xmlSigned = self._construir_xml_soap('ConsultaCNPJRequest', xmlSigned, self.uf)
                url = self._get_url(consulta='CADASTRO')

                print("Envelope assinado: ", etree.tostring(xmlSigned))

                return self._post(url, xmlSigned)

            else:
                url = self._get_url(consulta='CADASTRO')
                raiz = etree.Element('ConsCad', versao='2.00', xmlns=NAMESPACE_NFE)
                info = etree.SubElement(raiz, 'infCons')
                etree.SubElement(info, 'xServ').text = 'CONS-CAD'
                etree.SubElement(info, 'UF').text = self.uf.upper()
                etree.SubElement(info, 'CNPJ').text = cnpj
                xml = self._construir_xml_soap('ConsultaCNPJ', raiz, self.uf)
                return self._post(url, xml)


    def status_servico(self):

        url = self._get_url('STATUS')
        raiz = etree.Element('consStatServ', versao="4.00", xmlns=NAMESPACE_NFE)
        etree.SubElement(raiz, 'tpAmb').text = str(self.ambiente)
        etree.SubElement(raiz, 'cUF').text = "35"
        etree.SubElement(raiz, 'xServ').text = "STATUS"
        xml = self._construir_xml_soap('NFeStatusServico4', raiz, self.uf)
        print(etree.tostring(xml))
        return self._post(url, xml)

    def autorizacao(self, nota, consulta):

        url = self._get_url(consulta=consulta)
        if consulta == "SP":
            xml = etree.tostring(nota, encoding='unicode', pretty_print=False)
            # comunicacao via wsdl
            return self._post(url, xml)
        elif consulta == "PREFEITURA":
            xmlPrefeitura = etree.tostring(nota, encoding='unicode', pretty_print=True)
            print(xmlPrefeitura)
            return self._post(url, xmlPrefeitura)
        else:
            raise Exception("Metodo criado somente para SEFAZ 'SP' ou 'PREFEITURA' de SP")

    def consulta_recibo(self, number):

        url = self._get_url(consulta='RECIBO')
        raiz = etree.Element('consReciNFe', versao="4.00", xmlns=NAMESPACE_NFE)
        etree.SubElement(raiz, 'tpAmb').text = str(self.ambiente)
        etree.SubElement(raiz, 'nRec').text = number
        xml = self._construir_xml_soap('NFeRetAutorizacao4', raiz, self.uf)
        return self._post(url, xml)
