import subprocess
import xml.etree.ElementTree as ElementTree
from lxml import etree
from signxml import XMLSigner, XMLVerifier
from Utils import Certificate, CertData
from PostXML import PostXML


NAMESPACE_SIG = 'http://www.w3.org/2000/09/xmldsig#'

# Working with .crt and .pem files
certificateFile = "certfiles/certStark.pem"
privatekeyFile = "certfiles/privateKey.key"
key = open(privatekeyFile, "rb").read()
cnpj = "20018183000180"


class SignCert:

    def __init__(self):
        self.cert = Certificate(keyFile=privatekeyFile, certFile=certificateFile)
        self.certData = CertData(certFile=certificateFile, keyFile=privatekeyFile)

    # Generate a self signed key and cert file if they doesnt't exists:
    def generateCert(self):
        print subprocess.Popen("ls -lash", shell=True, stdout=subprocess.PIPE).stdout.read()
        listPem = subprocess.Popen("ls -lash *pem", shell=True, stdout=subprocess.PIPE).stdout.read()
        generatePem = "openssl req -new -newkey rsa:4096 -nodes -keyout snakeoil.key -out snakeoil.csr"
        generateSelfSigned = "openssl x509 -req -sha256 -days 365 -in snakeoil.csr -signkey snakeoil.key -out snakeoil.pem"
        if "snakeoil.pem" in listPem:
            print("PEM file already found")
            return listPem
        subprocess.Popen(generatePem, shell=True, stdout=subprocess.PIPE).stdout.read()
        subprocess.Popen(generateSelfSigned, shell=True, stdout=subprocess.PIPE).stdout.read()

    # Load certificate content from .pem or certificate files
    def loadPem(self):
        from cryptography.hazmat.backends import default_backend
        from cryptography import x509
        f = open('certfiles/certStark.pem', "rb")
        pem_data = f.read()
        f.close()

        key = x509.load_pem_x509_certificate(pem_data, backend=default_backend())
        # Not serialized Public Key:
        public_key = key.public_key()
        return key


    def loadCert(self):

        return(self.certData.extractCertContent())

    def loadKey(self):

        return self.certData.extractKeyContent()

    def signXML(self, xmlEnvelope):

        key = open(privatekeyFile, 'rb').read()
        root = ElementTree.fromstring(xmlEnvelope)
        signedRoot = XMLSigner().sign(root, key=key, cert=certificateFile)
        return signedRoot

    def signA1Cert(self, stringXml):

        return self.certData.signWithCert(stringXml=stringXml, key=privatekeyFile)

    def verifySignature(self, signedRoot):

        return self.certData.verifyCert(signedRoot)
