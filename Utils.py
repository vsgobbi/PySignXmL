# -*- coding: utf-8 -*-
from traceback import print_exc

import signxml
from signxml import XMLSigner, XMLVerifier
from lxml import etree


NAMESPACE_SIG = 'http://www.w3.org/2000/09/xmldsig#'


class Certificate(object):

    certFile = ""
    keyFile = ""

    def __init__(self, keyFile, certFile):
        self.certFile = certFile
        self.keyFile = keyFile

        # try:
        #      CertData.extractCertContent(certFile)
        #
        #      CertData.extractKeyContent(keyFile)
        # except:
        #      "Couldn't extract cert and key data"
             # ToDO: connect to google Datastore to receive cert files


class CertData(Certificate):

    def extractCertContent(self):

        # Extract base64 data from cert file:
        with open(self.certFile, 'rb') as certData:
            # print(certData.read())
            certBuffer = certData.read()
            # Remove white spaces :
            certBuffer = certBuffer.replace('\n', '')
            certData1 = certBuffer.split('-----BEGIN CERTIFICATE-----')
            certBuffer = str((certData1[1].replace('-----END CERTIFICATE-----', '')))
            #print(certBuffer)
            return certBuffer

    def extractKeyContent(self):

        # Extract base64 data from PrivateKey file
        with open(self.keyFile, 'rb') as keyData:
            keyBuffer = keyData.read()
            # Remove white spaces :
            keyBuffer = keyBuffer.replace('\n', '')
            keyData1 = keyBuffer.split('-----BEGIN PRIVATE KEY-----')
            keyBuffer = str((keyData1[1].replace('-----END PRIVATE KEY-----', '')))

            return keyBuffer

    def signWithCert(self, stringXml, key, returnString=True):

        xmlBuffer = etree.fromstring(stringXml)
        tree = etree.fromstring(stringXml)
        reference = tree.findall(".//*[@Id]")
        cert = self.extractCertContent()
        key = open(key, "rb").read()
        signer = XMLSigner(
            method=signxml.methods.enveloped, signature_algorithm="rsa-sha1",
            digest_algorithm='sha1',
            c14n_algorithm='http://www.w3.org/TR/2001/REC-xml-c14n-20010315')
        ns = {None: signer.namespaces['ds']}
        signer.namespaces = ns

        refUri = ('#%s' % reference) if reference else None
        signedRoot = signer.sign(
            xmlBuffer, key=key, cert=cert, reference_uri=refUri)

        ns = {'ns': NAMESPACE_SIG}
        # Insert the cert file buffered data (content) into specified tags X509Data/X509Certificate
        tagX509Data = signedRoot.find('.//ns:X509Data', namespaces=ns)
        etree.SubElement(tagX509Data, 'X509Certificate').text = cert

        if returnString:
            xmlEnvelope = etree.tostring(signedRoot, encoding="unicode",  pretty_print=False)
            return xmlEnvelope
        else:
            return signedRoot

    def verifyCert(self, signedRoot=signWithCert):
        from base64 import b64decode

        cert = self.extractCertContent()
        #assertion_data = XMLVerifier().verify(b64decode(signedRoot), x509_cert=cert)
        #print(assertion_data)
        try:
            ver = XMLVerifier().verify(signedRoot, x509_cert=cert)
            print(ver)
        except:
            print_exc()


class SerializeNFSe:
    pass


# class AssinaturaA1:
#
#     def __init__(self, certificado, senha):
#         self.key, self.cert = CertificadoA1(certificado).separar_arquivo(senha)
#
#     def assinar(self, xml, retorna_string=False):
#         # busca tag que tem id(reference_uri), logo nao importa se tem namespace
#
#         from xml.etree import ElementTree as et
#         tree = et.fromstring(xml)
#         print(tree.findall(".//*[@Id]"))
#         et.dump(tree)
#
#         #reference = xml.find(".//*[@Id]").attrib['Id']
#         reference =tree.findall(".//*[@Id]")
#
#
#         print(xml)
#         xml_str = etree.tostring(xml, 'utf-8', method="xml")
#
#         xml = etree.fromstring(xml_str)
#
#
#         signer = XMLSigner(
#             method=signxml.methods.enveloped, signature_algorithm="rsa-sha1",
#             digest_algorithm='sha1',
#             c14n_algorithm='http://www.w3.org/TR/2001/REC-xml-c14n-20010315')
#
#         ns = {None: signer.namespaces['ds']}
#         signer.namespaces = ns
#
#         ref_uri = ('#%s' % reference) if reference else None
#         signed_root = signer.sign(
#             xml, key=self.key, cert=self.cert, reference_uri=ref_uri)
#
#         ns = {'ns': NAMESPACE_SIG}
#         # coloca o certificado na tag X509Data/X509Certificate
#         tagX509Data = signed_root.find('.//ns:X509Data', namespaces=ns)
#         etree.SubElement(tagX509Data, 'X509Certificate').text = self.cert
#         if retorna_string:
#             return etree.tostring(signed_root, encoding="unicode", pretty_print=False)
#         else:
#             return signed_root