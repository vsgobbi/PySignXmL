from StringIO import StringIO

from lxml import etree

parser = etree.XMLParser(dtd_validation=True)

xsdFile = "/Users/vitorgabriel/Downloads/schemasv02/nfse/PedidoConsultaCNPJ_v01.xsd"
with open(xsdFile) as openXsd:
    schema_root = openXsd.read()
schema_root = StringIO(schema_root)
xmlschema_doc = etree.parse(xsdFile)
xmlschema = etree.XMLSchema(xmlschema_doc)

xml_generated = """<PedidoConsultaCNPJ>
       <Cabecalho Versao="test attribute">
              <CPFCNPJRemetente>test string</CPFCNPJRemetente>
          </Cabecalho>
       <CNPJContribuinte>test string</CNPJContribuinte>
   </PedidoConsultaCNPJ>"""


xml_envelope = "/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/PedidoConsultaCNPJ.xml"
xml_doc = etree.parse(xml_envelope)
result = xmlschema.validate(xml_doc)
print(result)
from lxml import etree, objectify
from lxml.etree import XMLSyntaxError

def xml_validator(some_xml_string, xsd_file=xsdFile):
    try:
        schema = etree.XMLSchema(file=xsd_file)
        parser = objectify.makeparser(schema=schema)
        objectify.fromstring(some_xml_string, parser)
        print "XML Validado"
    except XMLSyntaxError:
        print "XML invalido de acordo com XSD"
        pass

xml_file = open('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/PedidoConsultaCNPJ.xml', 'r')
xml_string = xml_file.read()
xml_file.close()
print("XSD ConsultaCNPJ: ")
xml_validator(xml_generated, xsdFile)

# Teste para EnviarLoteRPS:
xml_file = open('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/EnviarLoteRps.xml', 'r')
xml_string = xml_file.read()
xml_file.close()
xsd_enviar_File = "/Users/vitorgabriel/Downloads/schemasv02/nfse/PedidoEnvioLoteRPS_v01.xsd"
print("XSD enviar lote: ")
xml_validator(xml_string, xsd_enviar_File)

from Bindings import PedidoConsultaCNPJ


