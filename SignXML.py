import lxml
import subprocess
import xml.etree.ElementTree as ElementTree
import xml.etree.ElementTree as ET
from signxml import XMLSigner, XMLVerifier
import signxml
from Utils import AssinaturaA1
webService = "https://nfe.fazenda.sp.gov.br/ws/nfestatusservico4.asmx"
NAMESPACE_SIG = 'http://www.w3.org/2000/09/xmldsig#'


xml_envelope = " "
stringxml="""<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <ConsultaCNPJRequest xmlns="http://www.prefeitura.sp.gov.br/nfe">
      <VersaoSchema>1</VersaoSchema>
      <MensagemXML><Cabecalho Versao="1">
    <CPFCNPJRemetente>
      <CNPJ>20018183000180</CNPJ>
    </CPFCNPJRemetente>
  </Cabecalho>
  <CNPJContribuinte>
    <CNPJ>20018183000180</CNPJ>
  </CNPJContribuinte></MensagemXML>
    </ConsultaCNPJRequest>
  </soap12:Body>
</soap12:Envelope>"""

e = ElementTree.fromstring(stringxml)

class SignCert:

    # Generate a key file:
    def generateCert(self):
        print subprocess.Popen("ls -lash", shell=True, stdout=subprocess.PIPE).stdout.read()
        listPem = subprocess.Popen("ls -lash *pem", shell=True, stdout=subprocess.PIPE).stdout.read()
        generatePem = "openssl req -new -newkey rsa:4096 -nodes -keyout snakeoil.key -out snakeoil.csr"
        generateSelfSigned = "openssl x509 -req -sha256 -days 365 -in snakeoil.csr -signkey snakeoil.key -out snakeoil.pem"
        if "snakeoil.pem" in listPem:
            print("PEM file found")
            return listPem
        subprocess.Popen(generatePem, shell=True, stdout=subprocess.PIPE).stdout.read()
        subprocess.Popen(generateSelfSigned, shell=True, stdout=subprocess.PIPE).stdout.read()

    def signXML(self):

        print subprocess.Popen("ls -lash", shell=True, stdout=subprocess.PIPE).stdout.read()
        cert = open("certStark.pem", 'rb').read()
        key = open("privateKey.key", 'rb').read()

        root = ElementTree.fromstring('<xml1>12</xml1>')
        signed_root = XMLSigner().sign(root, key=key, cert=cert)
        verified_data = XMLVerifier().verify(signed_root).signed_xml
        print verified_data

    def loadPem(self):

        from cryptography.hazmat.backends import default_backend
        from cryptography import x509
        f = open('snakeoil.pem', "rb")
        pem_data = f.read()
        f.close()

        key = x509.load_pem_x509_certificate(pem_data, backend=default_backend())
        public_key = key.public_key()
        print(key)
        print(public_key)


# How to use:
# objSignCert = SignCert()
# objSignCert.generateCert()
# objSignCert.loadPem()
# objSignCert.signXML()
#


certificado = "cert_stark.pfx"
senha = "birdforever"
key = open("privateKey.key").read()
certificadoCERT = "converted.crt"

data = ET.fromstring(stringxml)
xmldsig_stuff = (data, 'sha1')
root = ElementTree.fromstring(stringxml)
# signed_root = XMLSigner().sign(
#     root,
#     key=key,
#     cert=certificado
#     # algorithm='rsa-sha1',
#     # c14n_algorithm='http://www.w3.org/TR/2001/REC-xml-c14n-20010315'
#     )
from lxml import etree
from base64 import b64decode
from signxml import XMLVerifier,  XMLSigner

with open("envelope_assinado.xml", "rb") as fh:
    cert = etree.parse(fh).find(".//X509Certificate")

signed_root = XMLSigner(method=signxml.methods.detached).sign(root, key=key, cert=certificado)

import signxml

signer = XMLSigner(
            method=signxml.methods.enveloped, signature_algorithm="rsa-sha1",
            digest_algorithm='sha1',
            c14n_algorithm='http://www.w3.org/TR/2001/REC-xml-c14n-20010315')
ns = {None: signer.namespaces['ds']}
signer.namespaces = ns


# Extract base64 data from cert file:
with open(certificadoCERT, 'rb') as certData:
    #print(certData.read())
    certBuffer = certData.read()
    # Remove white spaces :
    certBuffer = certBuffer.replace('\n', '')
    #certData2 = bufferData.replace('-----END CERTIFICATE-----', '')
    certData1 = certBuffer.split('-----BEGIN CERTIFICATE-----')
    certBuffer = str((certData1[1].replace('-----END CERTIFICATE-----', '')))
    print(certBuffer)

xmlBuffer = etree.fromstring(stringxml)
tree = etree.fromstring(stringxml)
print(tree.findall(".//*[@Id]"))
reference = tree.findall(".//*[@Id]")

ref_uri = ('#%s' % reference) if reference else None
signed_root = signer.sign(
    xmlBuffer, key=key, cert=certificado, reference_uri=ref_uri)

ns = {'ns': NAMESPACE_SIG}
# Insert the cert file buffered data (content) into specified tags X509Data/X509Certificate
tagX509Data = signed_root.find('.//ns:X509Data', namespaces=ns)
etree.SubElement(tagX509Data, 'X509Certificate').text = certBuffer
retorna_string = True
if retorna_string:
    print(etree.tostring(signed_root, encoding="unicode", pretty_print=False))
else:
    print(signed_root)

# assinatura
# a1 = AssinaturaA1(certificado, senha)
# print(a1)
# xml = a1.assinar(stringxml)
#print(xml)