import lxml
import subprocess
import xml.etree.ElementTree as ElementTree
from signxml import XMLSigner, XMLVerifier

webService = "https://nfe.fazenda.sp.gov.br/ws/nfestatusservico4.asmx"


xml_envelope = " "
stringxml='<?xml version="1.0"?><data><country name="Liechtenstein">' \
        '<rank>1</rank><year>2008</year><gdppc>141100</gdppc>' \
        '<neighbor name="Austria" direction="E"/>' \
        '<neighbor name="Switzerland" direction="W"/>' \
        '</country><country name="Singapore">' \
        '<rank>4</rank><year>2011</year><gdppc>59900</gdppc>' \
        '<neighbor name="Malaysia" direction="N"/></country>' \
        '<country name="Panama"><rank>68</rank>' \
        '<year>2011</year><gdppc>13600</gdppc>' \
        '<neighbor name="Costa Rica" direction="W"/>' \
        '<neighbor name="Colombia" direction="E"/>' \
        '</country></data>'

e = ElementTree.fromstring(stringxml) #will wok fine!
print(e)


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
        cert = open("snakeoil.pem", 'rb').read()
        key = open("snakeoil.key", 'rb').read()

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
objSignCert = SignCert()
objSignCert.generateCert()
objSignCert.loadPem()
objSignCert.signXML()