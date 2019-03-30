# -*- coding: utf-8 -*-
#from pynfe.utils import etree, remover_acentos
#from pynfe.utils.flags import NAMESPACE_SIG
import subprocess
import signxml
from signxml import XMLSigner
#from pynfe.entidades import CertificadoA1
from Base import Entidade
from OpenSSL import crypto
import tempfile
import os
import xml.etree.ElementTree as etree


NAMESPACE_SIG = 'http://www.w3.org/2000/09/xmldsig#'


class Certificado(Entidade):
    """Classe abstrata responsavel por definir o modelo padrao para as demais
    classes de certificados digitais.

    Caso va implementar um novo formato de certificado, crie uma classe que
    herde desta."""

    def __new__(cls, *args, **kwargs):
        if cls == Certificado:
            raise Exception('Esta classe nao pode ser instanciada diretamente!')
        else:
            return super(Certificado, cls).__new__(cls)


class CertificadoA1(Certificado):
    """Implementa a entidade do certificado eCNPJ A1, suportado pelo OpenSSL,
    e amplamente utilizado."""

    caminho_arquivo = None

    def __init__(self, caminho_arquivo=None):
        self.caminho_arquivo = caminho_arquivo
        self.arquivos_temp = []

    def separar_arquivo(self, senha, caminho=False):
        """Separa o arquivo de certificado em dois: de chave e de certificado,
        e retorna a string. Se caminho for True grava na pasta temporaria e retorna
        o caminho dos arquivos, senao retorna o objeto. Apos o uso devem ser excluidos com o metodo excluir."""

        # Carrega o arquivo .pfx, erro pode ocorrer se a senha estiver errada ou formato invalido.
        try:
            pkcs12 = crypto.load_pkcs12(open(self.caminho_arquivo, "rb").read(), senha)
        except Exception as e:
            raise Exception('Falha ao carregar certificado digital A1. Verifique local e senha.')

        if caminho:
            cert = crypto.dump_certificate(crypto.FILETYPE_PEM, pkcs12.get_certificate())
            chave = crypto.dump_privatekey(crypto.FILETYPE_PEM, pkcs12.get_privatekey())
            # cria arquivos temporarios
            with tempfile.NamedTemporaryFile(delete=False) as arqcert:
                arqcert.write(cert)
            with tempfile.NamedTemporaryFile(delete=False) as arqchave:
                arqchave.write(chave)
            self.arquivos_temp.append(arqchave.name)
            self.arquivos_temp.append(arqcert.name)
            return arqchave.name, arqcert.name
        else:
            # Certificado
            cert = crypto.dump_certificate(crypto.FILETYPE_PEM, pkcs12.get_certificate()).decode('utf-8')
            cert = cert.replace('\n', '')
            cert = cert.replace('-----BEGIN CERTIFICATE-----', '')
            cert = cert.replace('-----END CERTIFICATE-----', '')

            # Chave, string decodificada da chave privada
            chave = crypto.dump_privatekey(crypto.FILETYPE_PEM, pkcs12.get_privatekey())

            return chave, cert

    def excluir(self):
        """Exclui os arquivos temporarios utilizados para o request."""
        try:
            for i in self.arquivos_temp:
                os.remove(i)
            self.arquivos_temp.clear()
        except:
            pass


class Assinatura(object):
    """Classe abstrata responsavel por definir os metodos e logica das classes
    de assinatura digital."""

    certificado = None
    senha = None

    def __init__(self, certificado, senha, autorizador=None):
        self.certificado = certificado
        self.senha = senha
        self.autorizador = autorizador

    def assinar(self, xml):
        """Efetua a assinatura da nota"""
        pass


class AssinaturaA1(Assinatura):

    def __init__(self, certificado, senha):
        self.key, self.cert = CertificadoA1(certificado).separar_arquivo(senha)

    def assinar(self, xml, retorna_string=False):
        # busca tag que tem id(reference_uri), logo nao importa se tem namespace

        from xml.etree import ElementTree as et
        tree = et.fromstring(xml)
        print(tree.findall(".//*[@Id]"))
        et.dump(tree)

        #reference = xml.find(".//*[@Id]").attrib['Id']
        reference =tree.findall(".//*[@Id]")


        print(xml)
        xml_str = etree.tostring(xml, 'utf-8', method="xml")

        xml = etree.fromstring(xml_str)


        signer = XMLSigner(
            method=signxml.methods.enveloped, signature_algorithm="rsa-sha1",
            digest_algorithm='sha1',
            c14n_algorithm='http://www.w3.org/TR/2001/REC-xml-c14n-20010315')

        ns = {None: signer.namespaces['ds']}
        signer.namespaces = ns

        ref_uri = ('#%s' % reference) if reference else None
        signed_root = signer.sign(
            xml, key=self.key, cert=self.cert, reference_uri=ref_uri)

        ns = {'ns': NAMESPACE_SIG}
        # coloca o certificado na tag X509Data/X509Certificate
        tagX509Data = signed_root.find('.//ns:X509Data', namespaces=ns)
        etree.SubElement(tagX509Data, 'X509Certificate').text = self.cert
        if retorna_string:
            return etree.tostring(signed_root, encoding="unicode", pretty_print=False)
        else:
            return signed_root