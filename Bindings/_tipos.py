# ./_tipos.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:2e334b39c7bd1439ba40f8ef680545db7ebdc400
# Generated 2019-04-09 20:57:02.312433 by PyXB version 1.2.6 using Python 2.7.16.final.0
# Namespace http://www.prefeitura.sp.gov.br/nfe/tipos [xmlns:tipos]

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:2b6121d4-5b23-11e9-82e5-f01898534c67')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.prefeitura.sp.gov.br/nfe/tipos', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpAliquota
class tpAliquota (pyxb.binding.datatypes.decimal):

    """Tipo utilizado para valor de alíquota"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpAliquota')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 7, 2)
    _Documentation = 'Tipo utilizado para valor de al\xedquota'
tpAliquota._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=tpAliquota, value=pyxb.binding.datatypes.decimal('0.0'))
tpAliquota._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(4))
tpAliquota._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(5))
tpAliquota._InitializeFacetMap(tpAliquota._CF_minInclusive,
   tpAliquota._CF_fractionDigits,
   tpAliquota._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'tpAliquota', tpAliquota)
_module_typeBindings.tpAliquota = tpAliquota

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpAssinatura
class tpAssinatura (pyxb.binding.datatypes.base64Binary):

    """Assinatura digital do RPS emitido.O RPS deverá ser assinado digitalmente. O contribuinte deverá assinar uma cadeia de caracteres (ASCII) com informações do RPS emitido.O certificado digital utilizado na assinatura de cancelamento deverá ser o mesmo utilizado na assinatura da mensagem XML. A cadeia de caracteres a ser assinada deverá conter 86 posições com as informações apresentadas a seguir:Inscrição Municipal (CCM) do Prestador com 8 caracteres. Caso o CCM do Prestador tenha menos de 8 caracteres, o mesmo deverá ser completado com zeros à esquerda.Série do RPS com 5 posições. Caso a Série do RPS tenha menos de 5 caracteres, o mesmo deverá ser completado com espaços em branco à direita.Número do RPS com 12 posições. Caso o Número do RPS tenha menos de 12 caracteres, o mesmo deverá ser completado com zeros à esquerda.Data da emissão do RPS no formato AAAAMMDD.Tipo de Tributação do RPS com uma posição (sendo T: para Tributação no municipio de São Paulo; F: para Tributação fora do municipio de São Paulo; I: para Isento; J: para ISS Suspenso por Decisão Judicial).Status do RPS com uma posição (sendo N: Normal, C: Cancelado; E: Extraviado).ISS Retido com uma posição (sendo S: ISS Retido; N: Nota Fiscal sem ISS Retido).Valor dos Serviços com 15 posições e sem separador de milhar e decimal.Valor das Deduções com 15 posições e sem separador de milhar e decimal.Código do Serviço com 5 posições.CPF/CNPJ do tomador com 14 posições. Sem formatação (ponto, traço, barra, ....). Completar com zeros à esquerda caso seja necessário. Se o Indicador do CPF/CNPJ for 3 (não-informado), preencher com 14 zeros."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpAssinatura')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 17, 2)
    _Documentation = 'Assinatura digital do RPS emitido.O RPS dever\xe1 ser assinado digitalmente. O contribuinte dever\xe1 assinar uma cadeia de caracteres (ASCII) com informa\xe7\xf5es do RPS emitido.O certificado digital utilizado na assinatura de cancelamento dever\xe1 ser o mesmo utilizado na assinatura da mensagem XML. A cadeia de caracteres a ser assinada dever\xe1 conter 86 posi\xe7\xf5es com as informa\xe7\xf5es apresentadas a seguir:Inscri\xe7\xe3o Municipal (CCM) do Prestador com 8 caracteres. Caso o CCM do Prestador tenha menos de 8 caracteres, o mesmo dever\xe1 ser completado com zeros \xe0 esquerda.S\xe9rie do RPS com 5 posi\xe7\xf5es. Caso a S\xe9rie do RPS tenha menos de 5 caracteres, o mesmo dever\xe1 ser completado com espa\xe7os em branco \xe0 direita.N\xfamero do RPS com 12 posi\xe7\xf5es. Caso o N\xfamero do RPS tenha menos de 12 caracteres, o mesmo dever\xe1 ser completado com zeros \xe0 esquerda.Data da emiss\xe3o do RPS no formato AAAAMMDD.Tipo de Tributa\xe7\xe3o do RPS com uma posi\xe7\xe3o (sendo T: para Tributa\xe7\xe3o no municipio de S\xe3o Paulo; F: para Tributa\xe7\xe3o fora do municipio de S\xe3o Paulo; I: para Isento; J: para ISS Suspenso por Decis\xe3o Judicial).Status do RPS com uma posi\xe7\xe3o (sendo N: Normal, C: Cancelado; E: Extraviado).ISS Retido com uma posi\xe7\xe3o (sendo S: ISS Retido; N: Nota Fiscal sem ISS Retido).Valor dos Servi\xe7os com 15 posi\xe7\xf5es e sem separador de milhar e decimal.Valor das Dedu\xe7\xf5es com 15 posi\xe7\xf5es e sem separador de milhar e decimal.C\xf3digo do Servi\xe7o com 5 posi\xe7\xf5es.CPF/CNPJ do tomador com 14 posi\xe7\xf5es. Sem formata\xe7\xe3o (ponto, tra\xe7o, barra, ....). Completar com zeros \xe0 esquerda caso seja necess\xe1rio. Se o Indicador do CPF/CNPJ for 3 (n\xe3o-informado), preencher com 14 zeros.'
tpAssinatura._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'tpAssinatura', tpAssinatura)
_module_typeBindings.tpAssinatura = tpAssinatura

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpAssinaturaCancelamento
class tpAssinaturaCancelamento (pyxb.binding.datatypes.base64Binary):

    """Assinatura digital de cancelamento da NFS-e.Cada NFS-e a ser cancelada deverá ter sua respectiva assinatura de cancelamento. O contribuinte deverá assinar uma cadeia de caracteres (ASCII) com informações da NFS-e a ser cancelada.O certificado digital utilizado na assinatura de cancelamento deverá ser o mesmo utilizado na assinatura da mensagem XML. A cadeia de caracteres a ser assinada deverá conter 20 posições com as informações apresentadas a seguir:Inscrição Municipal (CCM) do Prestador com 8 caracteres. Caso o CCM do Prestador tenha menos de 8 caracteres, o mesmo deverá ser completado com zeros à esquerda.Número da NFS-e RPS com 12 posições. Caso o Número da NFS-e tenha menos de 12 caracteres, o mesmo deverá ser completado com zeros à esquerda."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpAssinaturaCancelamento')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 37, 2)
    _Documentation = 'Assinatura digital de cancelamento da NFS-e.Cada NFS-e a ser cancelada dever\xe1 ter sua respectiva assinatura de cancelamento. O contribuinte dever\xe1 assinar uma cadeia de caracteres (ASCII) com informa\xe7\xf5es da NFS-e a ser cancelada.O certificado digital utilizado na assinatura de cancelamento dever\xe1 ser o mesmo utilizado na assinatura da mensagem XML. A cadeia de caracteres a ser assinada dever\xe1 conter 20 posi\xe7\xf5es com as informa\xe7\xf5es apresentadas a seguir:Inscri\xe7\xe3o Municipal (CCM) do Prestador com 8 caracteres. Caso o CCM do Prestador tenha menos de 8 caracteres, o mesmo dever\xe1 ser completado com zeros \xe0 esquerda.N\xfamero da NFS-e RPS com 12 posi\xe7\xf5es. Caso o N\xfamero da NFS-e tenha menos de 12 caracteres, o mesmo dever\xe1 ser completado com zeros \xe0 esquerda.'
tpAssinaturaCancelamento._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'tpAssinaturaCancelamento', tpAssinaturaCancelamento)
_module_typeBindings.tpAssinaturaCancelamento = tpAssinaturaCancelamento

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpBairro
class tpBairro (pyxb.binding.datatypes.string):

    """Tipo bairro."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpBairro')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 48, 2)
    _Documentation = 'Tipo bairro.'
tpBairro._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tpBairro._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
tpBairro._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
tpBairro._InitializeFacetMap(tpBairro._CF_whiteSpace,
   tpBairro._CF_maxLength,
   tpBairro._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'tpBairro', tpBairro)
_module_typeBindings.tpBairro = tpBairro

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpCEP
class tpCEP (pyxb.binding.datatypes.int):

    """Tipo CEP."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpCEP')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 58, 2)
    _Documentation = 'Tipo CEP.'
tpCEP._CF_pattern = pyxb.binding.facets.CF_pattern()
tpCEP._CF_pattern.addPattern(pattern='[0-9]{7,8}')
tpCEP._InitializeFacetMap(tpCEP._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpCEP', tpCEP)
_module_typeBindings.tpCEP = tpCEP

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpCidade
class tpCidade (pyxb.binding.datatypes.int):

    """Tipo cidade."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpCidade')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 66, 2)
    _Documentation = 'Tipo cidade.'
tpCidade._CF_pattern = pyxb.binding.facets.CF_pattern()
tpCidade._CF_pattern.addPattern(pattern='[0-9]{7}')
tpCidade._InitializeFacetMap(tpCidade._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpCidade', tpCidade)
_module_typeBindings.tpCidade = tpCidade

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpCNPJ
class tpCNPJ (pyxb.binding.datatypes.string):

    """Tipo CNPJ."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpCNPJ')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 74, 2)
    _Documentation = 'Tipo CNPJ.'
tpCNPJ._CF_pattern = pyxb.binding.facets.CF_pattern()
tpCNPJ._CF_pattern.addPattern(pattern='[0-9]{14}')
tpCNPJ._InitializeFacetMap(tpCNPJ._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpCNPJ', tpCNPJ)
_module_typeBindings.tpCNPJ = tpCNPJ

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpCodigoServico
class tpCodigoServico (pyxb.binding.datatypes.int):

    """Tipo código de serviço."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpCodigoServico')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 82, 2)
    _Documentation = 'Tipo c\xf3digo de servi\xe7o.'
tpCodigoServico._CF_pattern = pyxb.binding.facets.CF_pattern()
tpCodigoServico._CF_pattern.addPattern(pattern='[0-9]{4,5}')
tpCodigoServico._InitializeFacetMap(tpCodigoServico._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpCodigoServico', tpCodigoServico)
_module_typeBindings.tpCodigoServico = tpCodigoServico

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpCodigoEvento
class tpCodigoEvento (pyxb.binding.datatypes.short):

    """Tipo código de evento."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpCodigoEvento')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 90, 2)
    _Documentation = 'Tipo c\xf3digo de evento.'
tpCodigoEvento._CF_pattern = pyxb.binding.facets.CF_pattern()
tpCodigoEvento._CF_pattern.addPattern(pattern='[0-9]{3,4}')
tpCodigoEvento._InitializeFacetMap(tpCodigoEvento._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpCodigoEvento', tpCodigoEvento)
_module_typeBindings.tpCodigoEvento = tpCodigoEvento

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpCodigoVerificacao
class tpCodigoVerificacao (pyxb.binding.datatypes.string):

    """Tipo Código de verificação da NFS-e."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpCodigoVerificacao')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 98, 2)
    _Documentation = 'Tipo C\xf3digo de verifica\xe7\xe3o da NFS-e.'
tpCodigoVerificacao._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tpCodigoVerificacao._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(8))
tpCodigoVerificacao._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(8))
tpCodigoVerificacao._InitializeFacetMap(tpCodigoVerificacao._CF_whiteSpace,
   tpCodigoVerificacao._CF_maxLength,
   tpCodigoVerificacao._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'tpCodigoVerificacao', tpCodigoVerificacao)
_module_typeBindings.tpCodigoVerificacao = tpCodigoVerificacao

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpComplementoEndereco
class tpComplementoEndereco (pyxb.binding.datatypes.string):

    """Tipo complemento do endereço."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpComplementoEndereco')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 108, 2)
    _Documentation = 'Tipo complemento do endere\xe7o.'
tpComplementoEndereco._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tpComplementoEndereco._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
tpComplementoEndereco._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
tpComplementoEndereco._InitializeFacetMap(tpComplementoEndereco._CF_whiteSpace,
   tpComplementoEndereco._CF_maxLength,
   tpComplementoEndereco._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'tpComplementoEndereco', tpComplementoEndereco)
_module_typeBindings.tpComplementoEndereco = tpComplementoEndereco

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpCPF
class tpCPF (pyxb.binding.datatypes.string):

    """Tipo CPF."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpCPF')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 118, 2)
    _Documentation = 'Tipo CPF.'
tpCPF._CF_pattern = pyxb.binding.facets.CF_pattern()
tpCPF._CF_pattern.addPattern(pattern='[0-9]{0}|[0-9]{11}')
tpCPF._InitializeFacetMap(tpCPF._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpCPF', tpCPF)
_module_typeBindings.tpCPF = tpCPF

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpDescricaoEvento
class tpDescricaoEvento (pyxb.binding.datatypes.string):

    """Tipo descrição do evento."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpDescricaoEvento')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 126, 2)
    _Documentation = 'Tipo descri\xe7\xe3o do evento.'
tpDescricaoEvento._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tpDescricaoEvento._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(300))
tpDescricaoEvento._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
tpDescricaoEvento._InitializeFacetMap(tpDescricaoEvento._CF_whiteSpace,
   tpDescricaoEvento._CF_maxLength,
   tpDescricaoEvento._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'tpDescricaoEvento', tpDescricaoEvento)
_module_typeBindings.tpDescricaoEvento = tpDescricaoEvento

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpDiscriminacao
class tpDiscriminacao (pyxb.binding.datatypes.string):

    """Tipo Discriminação Serviços."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpDiscriminacao')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 136, 2)
    _Documentation = 'Tipo Discrimina\xe7\xe3o Servi\xe7os.'
tpDiscriminacao._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tpDiscriminacao._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2000))
tpDiscriminacao._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tpDiscriminacao._InitializeFacetMap(tpDiscriminacao._CF_whiteSpace,
   tpDiscriminacao._CF_maxLength,
   tpDiscriminacao._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'tpDiscriminacao', tpDiscriminacao)
_module_typeBindings.tpDiscriminacao = tpDiscriminacao

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpEmail
class tpEmail (pyxb.binding.datatypes.string):

    """Tipo E-mail."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpEmail')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 146, 2)
    _Documentation = 'Tipo E-mail.'
tpEmail._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tpEmail._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(75))
tpEmail._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
tpEmail._InitializeFacetMap(tpEmail._CF_whiteSpace,
   tpEmail._CF_maxLength,
   tpEmail._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'tpEmail', tpEmail)
_module_typeBindings.tpEmail = tpEmail

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpInscricaoEstadual
class tpInscricaoEstadual (pyxb.binding.datatypes.long):

    """Tipo Inscrição Estadual."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpInscricaoEstadual')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 156, 2)
    _Documentation = 'Tipo Inscri\xe7\xe3o Estadual.'
tpInscricaoEstadual._CF_pattern = pyxb.binding.facets.CF_pattern()
tpInscricaoEstadual._CF_pattern.addPattern(pattern='[0-9]{1,19}')
tpInscricaoEstadual._InitializeFacetMap(tpInscricaoEstadual._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpInscricaoEstadual', tpInscricaoEstadual)
_module_typeBindings.tpInscricaoEstadual = tpInscricaoEstadual

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpInscricaoMunicipal
class tpInscricaoMunicipal (pyxb.binding.datatypes.long):

    """Tipo padrão referente a inscrição municipal."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpInscricaoMunicipal')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 164, 2)
    _Documentation = 'Tipo padr\xe3o referente a inscri\xe7\xe3o municipal.'
tpInscricaoMunicipal._CF_pattern = pyxb.binding.facets.CF_pattern()
tpInscricaoMunicipal._CF_pattern.addPattern(pattern='[0-9]{8,8}')
tpInscricaoMunicipal._InitializeFacetMap(tpInscricaoMunicipal._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpInscricaoMunicipal', tpInscricaoMunicipal)
_module_typeBindings.tpInscricaoMunicipal = tpInscricaoMunicipal

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpLogradouro
class tpLogradouro (pyxb.binding.datatypes.string):

    """Endereço."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpLogradouro')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 172, 2)
    _Documentation = 'Endere\xe7o.'
tpLogradouro._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tpLogradouro._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
tpLogradouro._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
tpLogradouro._InitializeFacetMap(tpLogradouro._CF_whiteSpace,
   tpLogradouro._CF_maxLength,
   tpLogradouro._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'tpLogradouro', tpLogradouro)
_module_typeBindings.tpLogradouro = tpLogradouro

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpNumero
class tpNumero (pyxb.binding.datatypes.long):

    """Tipo número."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpNumero')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 182, 2)
    _Documentation = 'Tipo n\xfamero.'
tpNumero._CF_pattern = pyxb.binding.facets.CF_pattern()
tpNumero._CF_pattern.addPattern(pattern='[0-9]{1,12}')
tpNumero._InitializeFacetMap(tpNumero._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpNumero', tpNumero)
_module_typeBindings.tpNumero = tpNumero

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpNumeroEndereco
class tpNumeroEndereco (pyxb.binding.datatypes.string):

    """Tipo número do endereço."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpNumeroEndereco')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 190, 2)
    _Documentation = 'Tipo n\xfamero do endere\xe7o.'
tpNumeroEndereco._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tpNumeroEndereco._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10))
tpNumeroEndereco._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
tpNumeroEndereco._InitializeFacetMap(tpNumeroEndereco._CF_whiteSpace,
   tpNumeroEndereco._CF_maxLength,
   tpNumeroEndereco._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'tpNumeroEndereco', tpNumeroEndereco)
_module_typeBindings.tpNumeroEndereco = tpNumeroEndereco

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpOpcaoSimples
class tpOpcaoSimples (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipo referente às possíveis opções de escolha pelo Simples."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpOpcaoSimples')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 200, 2)
    _Documentation = 'Tipo referente \xe0s poss\xedveis op\xe7\xf5es de escolha pelo Simples.'
tpOpcaoSimples._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpOpcaoSimples, enum_prefix=None)
tpOpcaoSimples.n0 = tpOpcaoSimples._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
tpOpcaoSimples.n1 = tpOpcaoSimples._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
tpOpcaoSimples.n2 = tpOpcaoSimples._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
tpOpcaoSimples.n3 = tpOpcaoSimples._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
tpOpcaoSimples._InitializeFacetMap(tpOpcaoSimples._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'tpOpcaoSimples', tpOpcaoSimples)
_module_typeBindings.tpOpcaoSimples = tpOpcaoSimples

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpQuantidade
class tpQuantidade (pyxb.binding.datatypes.long):

    """Tipo padrão para quantidades."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpQuantidade')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 227, 2)
    _Documentation = 'Tipo padr\xe3o para quantidades.'
tpQuantidade._CF_pattern = pyxb.binding.facets.CF_pattern()
tpQuantidade._CF_pattern.addPattern(pattern='[0-9]{1,15}')
tpQuantidade._InitializeFacetMap(tpQuantidade._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpQuantidade', tpQuantidade)
_module_typeBindings.tpQuantidade = tpQuantidade

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpRazaoSocial
class tpRazaoSocial (pyxb.binding.datatypes.string):

    """Tipo Razão Social."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpRazaoSocial')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 235, 2)
    _Documentation = 'Tipo Raz\xe3o Social.'
tpRazaoSocial._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tpRazaoSocial._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(75))
tpRazaoSocial._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
tpRazaoSocial._InitializeFacetMap(tpRazaoSocial._CF_whiteSpace,
   tpRazaoSocial._CF_maxLength,
   tpRazaoSocial._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'tpRazaoSocial', tpRazaoSocial)
_module_typeBindings.tpRazaoSocial = tpRazaoSocial

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpSerieRPS
class tpSerieRPS (pyxb.binding.datatypes.string):

    """Tipo série de documento."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpSerieRPS')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 245, 2)
    _Documentation = 'Tipo s\xe9rie de documento.'
tpSerieRPS._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tpSerieRPS._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(5))
tpSerieRPS._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tpSerieRPS._InitializeFacetMap(tpSerieRPS._CF_whiteSpace,
   tpSerieRPS._CF_maxLength,
   tpSerieRPS._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'tpSerieRPS', tpSerieRPS)
_module_typeBindings.tpSerieRPS = tpSerieRPS

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpStatusNFe
class tpStatusNFe (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipo referente aos possíveis status de NFS-e."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpStatusNFe')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 255, 2)
    _Documentation = 'Tipo referente aos poss\xedveis status de NFS-e.'
tpStatusNFe._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpStatusNFe, enum_prefix=None)
tpStatusNFe.N = tpStatusNFe._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
tpStatusNFe.C = tpStatusNFe._CF_enumeration.addEnumeration(unicode_value='C', tag='C')
tpStatusNFe.E = tpStatusNFe._CF_enumeration.addEnumeration(unicode_value='E', tag='E')
tpStatusNFe._InitializeFacetMap(tpStatusNFe._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'tpStatusNFe', tpStatusNFe)
_module_typeBindings.tpStatusNFe = tpStatusNFe

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpSucesso
class tpSucesso (pyxb.binding.datatypes.boolean):

    """Tipo que indica se o pedido do serviço obteve sucesso."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpSucesso')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 277, 2)
    _Documentation = 'Tipo que indica se o pedido do servi\xe7o obteve sucesso.'
tpSucesso._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'tpSucesso', tpSucesso)
_module_typeBindings.tpSucesso = tpSucesso

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpTempoProcessamento
class tpTempoProcessamento (pyxb.binding.datatypes.long):

    """Tipo referente ao tempo de processamento do lote."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpTempoProcessamento')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 284, 2)
    _Documentation = 'Tipo referente ao tempo de processamento do lote.'
tpTempoProcessamento._CF_pattern = pyxb.binding.facets.CF_pattern()
tpTempoProcessamento._CF_pattern.addPattern(pattern='[0-9]{1,15}')
tpTempoProcessamento._InitializeFacetMap(tpTempoProcessamento._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpTempoProcessamento', tpTempoProcessamento)
_module_typeBindings.tpTempoProcessamento = tpTempoProcessamento

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpTipoLogradouro
class tpTipoLogradouro (pyxb.binding.datatypes.string):

    """Tipo do endereço (Rua, Av, ...)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpTipoLogradouro')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 292, 2)
    _Documentation = 'Tipo do endere\xe7o (Rua, Av, ...).'
tpTipoLogradouro._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tpTipoLogradouro._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
tpTipoLogradouro._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
tpTipoLogradouro._InitializeFacetMap(tpTipoLogradouro._CF_whiteSpace,
   tpTipoLogradouro._CF_maxLength,
   tpTipoLogradouro._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'tpTipoLogradouro', tpTipoLogradouro)
_module_typeBindings.tpTipoLogradouro = tpTipoLogradouro

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpTipoRPS
class tpTipoRPS (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipo referente aos possíveis tipos de RPS."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpTipoRPS')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 302, 2)
    _Documentation = 'Tipo referente aos poss\xedveis tipos de RPS.'
tpTipoRPS._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpTipoRPS, enum_prefix=None)
tpTipoRPS.RPS = tpTipoRPS._CF_enumeration.addEnumeration(unicode_value='RPS', tag='RPS')
tpTipoRPS.RPS_M = tpTipoRPS._CF_enumeration.addEnumeration(unicode_value='RPS-M', tag='RPS_M')
tpTipoRPS.RPS_C = tpTipoRPS._CF_enumeration.addEnumeration(unicode_value='RPS-C', tag='RPS_C')
tpTipoRPS._InitializeFacetMap(tpTipoRPS._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'tpTipoRPS', tpTipoRPS)
_module_typeBindings.tpTipoRPS = tpTipoRPS

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpTributacaoNFe
class tpTributacaoNFe (pyxb.binding.datatypes.string):

    """Tipo referente aos modos de tributação da NFe."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpTributacaoNFe')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 324, 2)
    _Documentation = 'Tipo referente aos modos de tributa\xe7\xe3o da NFe.'
tpTributacaoNFe._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tpTributacaoNFe._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tpTributacaoNFe._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tpTributacaoNFe._InitializeFacetMap(tpTributacaoNFe._CF_whiteSpace,
   tpTributacaoNFe._CF_maxLength,
   tpTributacaoNFe._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'tpTributacaoNFe', tpTributacaoNFe)
_module_typeBindings.tpTributacaoNFe = tpTributacaoNFe

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpUF
class tpUF (pyxb.binding.datatypes.string):

    """Tipo UF."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpUF')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 334, 2)
    _Documentation = 'Tipo UF.'
tpUF._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tpUF._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
tpUF._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
tpUF._InitializeFacetMap(tpUF._CF_whiteSpace,
   tpUF._CF_maxLength,
   tpUF._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'tpUF', tpUF)
_module_typeBindings.tpUF = tpUF

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpValor
class tpValor (pyxb.binding.datatypes.decimal):

    """Tipo utilizado para valores com 15 dígitos, sendo 13 de corpo e 2 decimais."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpValor')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 344, 2)
    _Documentation = 'Tipo utilizado para valores com 15 d\xedgitos, sendo 13 de corpo e 2 decimais.'
tpValor._CF_pattern = pyxb.binding.facets.CF_pattern()
tpValor._CF_pattern.addPattern(pattern='0|0\\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\\.[0-9]{0,2})?')
tpValor._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=tpValor, value=pyxb.binding.datatypes.decimal('0.0'))
tpValor._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2))
tpValor._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(15))
tpValor._InitializeFacetMap(tpValor._CF_pattern,
   tpValor._CF_minInclusive,
   tpValor._CF_fractionDigits,
   tpValor._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'tpValor', tpValor)
_module_typeBindings.tpValor = tpValor

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpVersao
class tpVersao (pyxb.binding.datatypes.long):

    """Tipo Versão do Schema."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpVersao')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 355, 2)
    _Documentation = 'Tipo Vers\xe3o do Schema.'
tpVersao._CF_pattern = pyxb.binding.facets.CF_pattern()
tpVersao._CF_pattern.addPattern(pattern='[0-9]{1,3}')
tpVersao._InitializeFacetMap(tpVersao._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpVersao', tpVersao)
_module_typeBindings.tpVersao = tpVersao

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpPercentualCargaTributaria
class tpPercentualCargaTributaria (pyxb.binding.datatypes.decimal):

    """Tipo utilizado para o valor do percentual da carga tributária."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpPercentualCargaTributaria')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 363, 2)
    _Documentation = 'Tipo utilizado para o valor do percentual da carga tribut\xe1ria.'
tpPercentualCargaTributaria._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=tpPercentualCargaTributaria, value=pyxb.binding.datatypes.decimal('0.0'))
tpPercentualCargaTributaria._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(4))
tpPercentualCargaTributaria._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(7))
tpPercentualCargaTributaria._InitializeFacetMap(tpPercentualCargaTributaria._CF_minInclusive,
   tpPercentualCargaTributaria._CF_fractionDigits,
   tpPercentualCargaTributaria._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'tpPercentualCargaTributaria', tpPercentualCargaTributaria)
_module_typeBindings.tpPercentualCargaTributaria = tpPercentualCargaTributaria

# Atomic simple type: {http://www.prefeitura.sp.gov.br/nfe/tipos}tpFonteCargaTributaria
class tpFonteCargaTributaria (pyxb.binding.datatypes.string):

    """Tipo utilizado para a fonte da carga tributária."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpFonteCargaTributaria')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 373, 2)
    _Documentation = 'Tipo utilizado para a fonte da carga tribut\xe1ria.'
tpFonteCargaTributaria._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tpFonteCargaTributaria._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10))
tpFonteCargaTributaria._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
tpFonteCargaTributaria._InitializeFacetMap(tpFonteCargaTributaria._CF_whiteSpace,
   tpFonteCargaTributaria._CF_maxLength,
   tpFonteCargaTributaria._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'tpFonteCargaTributaria', tpFonteCargaTributaria)
_module_typeBindings.tpFonteCargaTributaria = tpFonteCargaTributaria

# Complex type {http://www.prefeitura.sp.gov.br/nfe/tipos}tpEvento with content type ELEMENT_ONLY
class tpEvento (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.prefeitura.sp.gov.br/nfe/tipos}tpEvento with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpEvento')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 385, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Codigo uses Python identifier Codigo
    __Codigo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Codigo'), 'Codigo', '__httpwww_prefeitura_sp_gov_brnfetipos_tpEvento_Codigo', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 387, 6), )

    
    Codigo = property(__Codigo.value, __Codigo.set, None, 'C\xf3digo do evento.')

    
    # Element Descricao uses Python identifier Descricao
    __Descricao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Descricao'), 'Descricao', '__httpwww_prefeitura_sp_gov_brnfetipos_tpEvento_Descricao', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 392, 6), )

    
    Descricao = property(__Descricao.value, __Descricao.set, None, 'Descri\xe7\xe3o do enveto.')

    
    # Element ChaveRPS uses Python identifier ChaveRPS
    __ChaveRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ChaveRPS'), 'ChaveRPS', '__httpwww_prefeitura_sp_gov_brnfetipos_tpEvento_ChaveRPS', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 401, 8), )

    
    ChaveRPS = property(__ChaveRPS.value, __ChaveRPS.set, None, 'Chave do RPS.')

    
    # Element ChaveNFe uses Python identifier ChaveNFe
    __ChaveNFe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ChaveNFe'), 'ChaveNFe', '__httpwww_prefeitura_sp_gov_brnfetipos_tpEvento_ChaveNFe', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 406, 8), )

    
    ChaveNFe = property(__ChaveNFe.value, __ChaveNFe.set, None, 'Chave da NFe.')

    _ElementMap.update({
        __Codigo.name() : __Codigo,
        __Descricao.name() : __Descricao,
        __ChaveRPS.name() : __ChaveRPS,
        __ChaveNFe.name() : __ChaveNFe
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpEvento = tpEvento
Namespace.addCategoryObject('typeBinding', 'tpEvento', tpEvento)


# Complex type {http://www.prefeitura.sp.gov.br/nfe/tipos}tpCPFCNPJ with content type ELEMENT_ONLY
class tpCPFCNPJ (pyxb.binding.basis.complexTypeDefinition):
    """Tipo que representa um CPF/CNPJ."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpCPFCNPJ')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 414, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element CPF uses Python identifier CPF
    __CPF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPF'), 'CPF', '__httpwww_prefeitura_sp_gov_brnfetipos_tpCPFCNPJ_CPF', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 419, 6), )

    
    CPF = property(__CPF.value, __CPF.set, None, None)

    
    # Element CNPJ uses Python identifier CNPJ
    __CNPJ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CNPJ'), 'CNPJ', '__httpwww_prefeitura_sp_gov_brnfetipos_tpCPFCNPJ_CNPJ', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 420, 6), )

    
    CNPJ = property(__CNPJ.value, __CNPJ.set, None, None)

    _ElementMap.update({
        __CPF.name() : __CPF,
        __CNPJ.name() : __CNPJ
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpCPFCNPJ = tpCPFCNPJ
Namespace.addCategoryObject('typeBinding', 'tpCPFCNPJ', tpCPFCNPJ)


# Complex type {http://www.prefeitura.sp.gov.br/nfe/tipos}tpChaveNFeRPS with content type ELEMENT_ONLY
class tpChaveNFeRPS (pyxb.binding.basis.complexTypeDefinition):
    """Tipo que representa a chave de uma NFS-e e a Chave do RPS que a mesma substitui."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpChaveNFeRPS')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 423, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ChaveNFe uses Python identifier ChaveNFe
    __ChaveNFe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ChaveNFe'), 'ChaveNFe', '__httpwww_prefeitura_sp_gov_brnfetipos_tpChaveNFeRPS_ChaveNFe', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 428, 6), )

    
    ChaveNFe = property(__ChaveNFe.value, __ChaveNFe.set, None, 'Chave da NFS-e gerada.')

    
    # Element ChaveRPS uses Python identifier ChaveRPS
    __ChaveRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ChaveRPS'), 'ChaveRPS', '__httpwww_prefeitura_sp_gov_brnfetipos_tpChaveNFeRPS_ChaveRPS', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 433, 6), )

    
    ChaveRPS = property(__ChaveRPS.value, __ChaveRPS.set, None, 'Chave do RPS substitu\xeddo.')

    _ElementMap.update({
        __ChaveNFe.name() : __ChaveNFe,
        __ChaveRPS.name() : __ChaveRPS
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpChaveNFeRPS = tpChaveNFeRPS
Namespace.addCategoryObject('typeBinding', 'tpChaveNFeRPS', tpChaveNFeRPS)


# Complex type {http://www.prefeitura.sp.gov.br/nfe/tipos}tpChaveNFe with content type ELEMENT_ONLY
class tpChaveNFe (pyxb.binding.basis.complexTypeDefinition):
    """Chave de identificação da NFS-e."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpChaveNFe')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 440, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element InscricaoPrestador uses Python identifier InscricaoPrestador
    __InscricaoPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador'), 'InscricaoPrestador', '__httpwww_prefeitura_sp_gov_brnfetipos_tpChaveNFe_InscricaoPrestador', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 445, 6), )

    
    InscricaoPrestador = property(__InscricaoPrestador.value, __InscricaoPrestador.set, None, 'Inscri\xe7\xe3o municipal do prestador de servi\xe7os.')

    
    # Element NumeroNFe uses Python identifier NumeroNFe
    __NumeroNFe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroNFe'), 'NumeroNFe', '__httpwww_prefeitura_sp_gov_brnfetipos_tpChaveNFe_NumeroNFe', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 450, 6), )

    
    NumeroNFe = property(__NumeroNFe.value, __NumeroNFe.set, None, 'N\xfamero da NFS-e.')

    
    # Element CodigoVerificacao uses Python identifier CodigoVerificacao
    __CodigoVerificacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodigoVerificacao'), 'CodigoVerificacao', '__httpwww_prefeitura_sp_gov_brnfetipos_tpChaveNFe_CodigoVerificacao', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 455, 6), )

    
    CodigoVerificacao = property(__CodigoVerificacao.value, __CodigoVerificacao.set, None, 'C\xf3digo de verifica\xe7\xe3o da NFS-e.')

    _ElementMap.update({
        __InscricaoPrestador.name() : __InscricaoPrestador,
        __NumeroNFe.name() : __NumeroNFe,
        __CodigoVerificacao.name() : __CodigoVerificacao
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpChaveNFe = tpChaveNFe
Namespace.addCategoryObject('typeBinding', 'tpChaveNFe', tpChaveNFe)


# Complex type {http://www.prefeitura.sp.gov.br/nfe/tipos}tpChaveRPS with content type ELEMENT_ONLY
class tpChaveRPS (pyxb.binding.basis.complexTypeDefinition):
    """Tipo que define a chave identificadora de um RPS."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpChaveRPS')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 462, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element InscricaoPrestador uses Python identifier InscricaoPrestador
    __InscricaoPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador'), 'InscricaoPrestador', '__httpwww_prefeitura_sp_gov_brnfetipos_tpChaveRPS_InscricaoPrestador', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 467, 6), )

    
    InscricaoPrestador = property(__InscricaoPrestador.value, __InscricaoPrestador.set, None, 'Inscri\xe7\xe3o municipal do prestador de servi\xe7os.')

    
    # Element SerieRPS uses Python identifier SerieRPS
    __SerieRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SerieRPS'), 'SerieRPS', '__httpwww_prefeitura_sp_gov_brnfetipos_tpChaveRPS_SerieRPS', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 472, 6), )

    
    SerieRPS = property(__SerieRPS.value, __SerieRPS.set, None, 'S\xe9rie do RPS.')

    
    # Element NumeroRPS uses Python identifier NumeroRPS
    __NumeroRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroRPS'), 'NumeroRPS', '__httpwww_prefeitura_sp_gov_brnfetipos_tpChaveRPS_NumeroRPS', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 477, 6), )

    
    NumeroRPS = property(__NumeroRPS.value, __NumeroRPS.set, None, 'N\xfamero do RPS.')

    _ElementMap.update({
        __InscricaoPrestador.name() : __InscricaoPrestador,
        __SerieRPS.name() : __SerieRPS,
        __NumeroRPS.name() : __NumeroRPS
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpChaveRPS = tpChaveRPS
Namespace.addCategoryObject('typeBinding', 'tpChaveRPS', tpChaveRPS)


# Complex type {http://www.prefeitura.sp.gov.br/nfe/tipos}tpEndereco with content type ELEMENT_ONLY
class tpEndereco (pyxb.binding.basis.complexTypeDefinition):
    """Tipo Endereço."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpEndereco')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 484, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element TipoLogradouro uses Python identifier TipoLogradouro
    __TipoLogradouro = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TipoLogradouro'), 'TipoLogradouro', '__httpwww_prefeitura_sp_gov_brnfetipos_tpEndereco_TipoLogradouro', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 489, 6), )

    
    TipoLogradouro = property(__TipoLogradouro.value, __TipoLogradouro.set, None, None)

    
    # Element Logradouro uses Python identifier Logradouro
    __Logradouro = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Logradouro'), 'Logradouro', '__httpwww_prefeitura_sp_gov_brnfetipos_tpEndereco_Logradouro', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 490, 6), )

    
    Logradouro = property(__Logradouro.value, __Logradouro.set, None, None)

    
    # Element NumeroEndereco uses Python identifier NumeroEndereco
    __NumeroEndereco = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroEndereco'), 'NumeroEndereco', '__httpwww_prefeitura_sp_gov_brnfetipos_tpEndereco_NumeroEndereco', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 491, 6), )

    
    NumeroEndereco = property(__NumeroEndereco.value, __NumeroEndereco.set, None, None)

    
    # Element ComplementoEndereco uses Python identifier ComplementoEndereco
    __ComplementoEndereco = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ComplementoEndereco'), 'ComplementoEndereco', '__httpwww_prefeitura_sp_gov_brnfetipos_tpEndereco_ComplementoEndereco', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 492, 6), )

    
    ComplementoEndereco = property(__ComplementoEndereco.value, __ComplementoEndereco.set, None, None)

    
    # Element Bairro uses Python identifier Bairro
    __Bairro = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Bairro'), 'Bairro', '__httpwww_prefeitura_sp_gov_brnfetipos_tpEndereco_Bairro', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 493, 6), )

    
    Bairro = property(__Bairro.value, __Bairro.set, None, None)

    
    # Element Cidade uses Python identifier Cidade
    __Cidade = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Cidade'), 'Cidade', '__httpwww_prefeitura_sp_gov_brnfetipos_tpEndereco_Cidade', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 494, 6), )

    
    Cidade = property(__Cidade.value, __Cidade.set, None, None)

    
    # Element UF uses Python identifier UF
    __UF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'UF'), 'UF', '__httpwww_prefeitura_sp_gov_brnfetipos_tpEndereco_UF', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 495, 6), )

    
    UF = property(__UF.value, __UF.set, None, None)

    
    # Element CEP uses Python identifier CEP
    __CEP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CEP'), 'CEP', '__httpwww_prefeitura_sp_gov_brnfetipos_tpEndereco_CEP', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 496, 6), )

    
    CEP = property(__CEP.value, __CEP.set, None, None)

    _ElementMap.update({
        __TipoLogradouro.name() : __TipoLogradouro,
        __Logradouro.name() : __Logradouro,
        __NumeroEndereco.name() : __NumeroEndereco,
        __ComplementoEndereco.name() : __ComplementoEndereco,
        __Bairro.name() : __Bairro,
        __Cidade.name() : __Cidade,
        __UF.name() : __UF,
        __CEP.name() : __CEP
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpEndereco = tpEndereco
Namespace.addCategoryObject('typeBinding', 'tpEndereco', tpEndereco)


# Complex type {http://www.prefeitura.sp.gov.br/nfe/tipos}tpInformacoesLote with content type ELEMENT_ONLY
class tpInformacoesLote (pyxb.binding.basis.complexTypeDefinition):
    """Informações do lote processado."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpInformacoesLote')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 499, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element NumeroLote uses Python identifier NumeroLote
    __NumeroLote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroLote'), 'NumeroLote', '__httpwww_prefeitura_sp_gov_brnfetipos_tpInformacoesLote_NumeroLote', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 504, 6), )

    
    NumeroLote = property(__NumeroLote.value, __NumeroLote.set, None, 'N\xfamero de lote.')

    
    # Element InscricaoPrestador uses Python identifier InscricaoPrestador
    __InscricaoPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador'), 'InscricaoPrestador', '__httpwww_prefeitura_sp_gov_brnfetipos_tpInformacoesLote_InscricaoPrestador', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 509, 6), )

    
    InscricaoPrestador = property(__InscricaoPrestador.value, __InscricaoPrestador.set, None, 'Inscri\xe7\xe3o municipal do prestador dos RPS contidos no lote.')

    
    # Element CPFCNPJRemetente uses Python identifier CPFCNPJRemetente
    __CPFCNPJRemetente = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), 'CPFCNPJRemetente', '__httpwww_prefeitura_sp_gov_brnfetipos_tpInformacoesLote_CPFCNPJRemetente', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 514, 6), )

    
    CPFCNPJRemetente = property(__CPFCNPJRemetente.value, __CPFCNPJRemetente.set, None, 'CNPJ do remetente autorizado a transmitir a mensagem XML.')

    
    # Element DataEnvioLote uses Python identifier DataEnvioLote
    __DataEnvioLote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DataEnvioLote'), 'DataEnvioLote', '__httpwww_prefeitura_sp_gov_brnfetipos_tpInformacoesLote_DataEnvioLote', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 519, 6), )

    
    DataEnvioLote = property(__DataEnvioLote.value, __DataEnvioLote.set, None, 'Data/hora de envio do lote.')

    
    # Element QtdNotasProcessadas uses Python identifier QtdNotasProcessadas
    __QtdNotasProcessadas = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'QtdNotasProcessadas'), 'QtdNotasProcessadas', '__httpwww_prefeitura_sp_gov_brnfetipos_tpInformacoesLote_QtdNotasProcessadas', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 524, 6), )

    
    QtdNotasProcessadas = property(__QtdNotasProcessadas.value, __QtdNotasProcessadas.set, None, 'Quantidade de RPS do lote.')

    
    # Element TempoProcessamento uses Python identifier TempoProcessamento
    __TempoProcessamento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TempoProcessamento'), 'TempoProcessamento', '__httpwww_prefeitura_sp_gov_brnfetipos_tpInformacoesLote_TempoProcessamento', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 529, 6), )

    
    TempoProcessamento = property(__TempoProcessamento.value, __TempoProcessamento.set, None, 'Tempo de processamento do lote.')

    
    # Element ValorTotalServicos uses Python identifier ValorTotalServicos
    __ValorTotalServicos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorTotalServicos'), 'ValorTotalServicos', '__httpwww_prefeitura_sp_gov_brnfetipos_tpInformacoesLote_ValorTotalServicos', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 534, 6), )

    
    ValorTotalServicos = property(__ValorTotalServicos.value, __ValorTotalServicos.set, None, 'Valor total dos servi\xe7os dos RPS contidos na mensagem XML.')

    
    # Element ValorTotalDeducoes uses Python identifier ValorTotalDeducoes
    __ValorTotalDeducoes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorTotalDeducoes'), 'ValorTotalDeducoes', '__httpwww_prefeitura_sp_gov_brnfetipos_tpInformacoesLote_ValorTotalDeducoes', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 539, 6), )

    
    ValorTotalDeducoes = property(__ValorTotalDeducoes.value, __ValorTotalDeducoes.set, None, 'Valor total das dedu\xe7\xf5es dos RPS contidos na mensagem XML.')

    _ElementMap.update({
        __NumeroLote.name() : __NumeroLote,
        __InscricaoPrestador.name() : __InscricaoPrestador,
        __CPFCNPJRemetente.name() : __CPFCNPJRemetente,
        __DataEnvioLote.name() : __DataEnvioLote,
        __QtdNotasProcessadas.name() : __QtdNotasProcessadas,
        __TempoProcessamento.name() : __TempoProcessamento,
        __ValorTotalServicos.name() : __ValorTotalServicos,
        __ValorTotalDeducoes.name() : __ValorTotalDeducoes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpInformacoesLote = tpInformacoesLote
Namespace.addCategoryObject('typeBinding', 'tpInformacoesLote', tpInformacoesLote)


# Complex type {http://www.prefeitura.sp.gov.br/nfe/tipos}tpNFe with content type ELEMENT_ONLY
class tpNFe (pyxb.binding.basis.complexTypeDefinition):
    """Tipo que representa uma NFS-e"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpNFe')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 546, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Assinatura uses Python identifier Assinatura
    __Assinatura = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Assinatura'), 'Assinatura', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_Assinatura', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 551, 6), )

    
    Assinatura = property(__Assinatura.value, __Assinatura.set, None, 'Assinatura digital da NFS-e.')

    
    # Element ChaveNFe uses Python identifier ChaveNFe
    __ChaveNFe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ChaveNFe'), 'ChaveNFe', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_ChaveNFe', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 556, 6), )

    
    ChaveNFe = property(__ChaveNFe.value, __ChaveNFe.set, None, 'Chave de identifica\xe7\xe3o da NFS-e.')

    
    # Element DataEmissaoNFe uses Python identifier DataEmissaoNFe
    __DataEmissaoNFe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DataEmissaoNFe'), 'DataEmissaoNFe', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_DataEmissaoNFe', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 561, 6), )

    
    DataEmissaoNFe = property(__DataEmissaoNFe.value, __DataEmissaoNFe.set, None, 'Data de emiss\xe3o da NFS-e')

    
    # Element NumeroLote uses Python identifier NumeroLote
    __NumeroLote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroLote'), 'NumeroLote', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_NumeroLote', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 566, 6), )

    
    NumeroLote = property(__NumeroLote.value, __NumeroLote.set, None, 'N\xfamero de lote gerador da NFS-e.')

    
    # Element ChaveRPS uses Python identifier ChaveRPS
    __ChaveRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ChaveRPS'), 'ChaveRPS', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_ChaveRPS', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 571, 6), )

    
    ChaveRPS = property(__ChaveRPS.value, __ChaveRPS.set, None, 'Chave do RPS que originou a NFS-e.')

    
    # Element TipoRPS uses Python identifier TipoRPS
    __TipoRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TipoRPS'), 'TipoRPS', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_TipoRPS', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 576, 6), )

    
    TipoRPS = property(__TipoRPS.value, __TipoRPS.set, None, 'Tipo do RPS emitido.')

    
    # Element DataEmissaoRPS uses Python identifier DataEmissaoRPS
    __DataEmissaoRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DataEmissaoRPS'), 'DataEmissaoRPS', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_DataEmissaoRPS', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 581, 6), )

    
    DataEmissaoRPS = property(__DataEmissaoRPS.value, __DataEmissaoRPS.set, None, 'Data de emiss\xe3o do RPS que originou a NFS-e.')

    
    # Element CPFCNPJPrestador uses Python identifier CPFCNPJPrestador
    __CPFCNPJPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJPrestador'), 'CPFCNPJPrestador', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_CPFCNPJPrestador', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 586, 6), )

    
    CPFCNPJPrestador = property(__CPFCNPJPrestador.value, __CPFCNPJPrestador.set, None, 'CPF/CNPJ do Prestador do servi\xe7o.')

    
    # Element RazaoSocialPrestador uses Python identifier RazaoSocialPrestador
    __RazaoSocialPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RazaoSocialPrestador'), 'RazaoSocialPrestador', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_RazaoSocialPrestador', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 591, 6), )

    
    RazaoSocialPrestador = property(__RazaoSocialPrestador.value, __RazaoSocialPrestador.set, None, 'Nome/Raz\xe3o Social do Prestador.')

    
    # Element EnderecoPrestador uses Python identifier EnderecoPrestador
    __EnderecoPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EnderecoPrestador'), 'EnderecoPrestador', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_EnderecoPrestador', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 596, 6), )

    
    EnderecoPrestador = property(__EnderecoPrestador.value, __EnderecoPrestador.set, None, 'Endere\xe7o do Prestador.')

    
    # Element EmailPrestador uses Python identifier EmailPrestador
    __EmailPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EmailPrestador'), 'EmailPrestador', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_EmailPrestador', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 601, 6), )

    
    EmailPrestador = property(__EmailPrestador.value, __EmailPrestador.set, None, 'E-mail do Prestador.')

    
    # Element StatusNFe uses Python identifier StatusNFe
    __StatusNFe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'StatusNFe'), 'StatusNFe', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_StatusNFe', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 606, 6), )

    
    StatusNFe = property(__StatusNFe.value, __StatusNFe.set, None, 'Status da NFS-e.')

    
    # Element DataCancelamento uses Python identifier DataCancelamento
    __DataCancelamento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DataCancelamento'), 'DataCancelamento', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_DataCancelamento', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 611, 6), )

    
    DataCancelamento = property(__DataCancelamento.value, __DataCancelamento.set, None, 'Data de cancelamento da NFS-e.')

    
    # Element TributacaoNFe uses Python identifier TributacaoNFe
    __TributacaoNFe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TributacaoNFe'), 'TributacaoNFe', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_TributacaoNFe', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 616, 6), )

    
    TributacaoNFe = property(__TributacaoNFe.value, __TributacaoNFe.set, None, 'Tributa\xe7\xe3o da NFS-e.')

    
    # Element OpcaoSimples uses Python identifier OpcaoSimples
    __OpcaoSimples = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'OpcaoSimples'), 'OpcaoSimples', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_OpcaoSimples', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 621, 6), )

    
    OpcaoSimples = property(__OpcaoSimples.value, __OpcaoSimples.set, None, 'Op\xe7\xe3o pelo Simples.')

    
    # Element NumeroGuia uses Python identifier NumeroGuia
    __NumeroGuia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroGuia'), 'NumeroGuia', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_NumeroGuia', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 626, 6), )

    
    NumeroGuia = property(__NumeroGuia.value, __NumeroGuia.set, None, 'N\xfamero da guia vinculada a NFS-e.')

    
    # Element DataQuitacaoGuia uses Python identifier DataQuitacaoGuia
    __DataQuitacaoGuia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DataQuitacaoGuia'), 'DataQuitacaoGuia', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_DataQuitacaoGuia', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 631, 6), )

    
    DataQuitacaoGuia = property(__DataQuitacaoGuia.value, __DataQuitacaoGuia.set, None, 'Data de quita\xe7\xe3o da guia vinculada a NFS-e.')

    
    # Element ValorServicos uses Python identifier ValorServicos
    __ValorServicos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorServicos'), 'ValorServicos', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_ValorServicos', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 636, 6), )

    
    ValorServicos = property(__ValorServicos.value, __ValorServicos.set, None, 'Valor dos servi\xe7os prestados.')

    
    # Element ValorDeducoes uses Python identifier ValorDeducoes
    __ValorDeducoes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorDeducoes'), 'ValorDeducoes', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_ValorDeducoes', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 641, 6), )

    
    ValorDeducoes = property(__ValorDeducoes.value, __ValorDeducoes.set, None, 'Valor das dedu\xe7\xf5es.')

    
    # Element ValorPIS uses Python identifier ValorPIS
    __ValorPIS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorPIS'), 'ValorPIS', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_ValorPIS', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 646, 6), )

    
    ValorPIS = property(__ValorPIS.value, __ValorPIS.set, None, 'Valor da reten\xe7\xe3o do PIS.')

    
    # Element ValorCOFINS uses Python identifier ValorCOFINS
    __ValorCOFINS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorCOFINS'), 'ValorCOFINS', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_ValorCOFINS', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 651, 6), )

    
    ValorCOFINS = property(__ValorCOFINS.value, __ValorCOFINS.set, None, 'Valor da reten\xe7\xe3o do COFINS.')

    
    # Element ValorINSS uses Python identifier ValorINSS
    __ValorINSS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorINSS'), 'ValorINSS', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_ValorINSS', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 656, 6), )

    
    ValorINSS = property(__ValorINSS.value, __ValorINSS.set, None, 'Valor da reten\xe7\xe3o do INSS.')

    
    # Element ValorIR uses Python identifier ValorIR
    __ValorIR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorIR'), 'ValorIR', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_ValorIR', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 661, 6), )

    
    ValorIR = property(__ValorIR.value, __ValorIR.set, None, 'Valor da reten\xe7\xe3o do IR.')

    
    # Element ValorCSLL uses Python identifier ValorCSLL
    __ValorCSLL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorCSLL'), 'ValorCSLL', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_ValorCSLL', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 666, 6), )

    
    ValorCSLL = property(__ValorCSLL.value, __ValorCSLL.set, None, 'Valor da reten\xe7\xe3o do CSLL.')

    
    # Element CodigoServico uses Python identifier CodigoServico
    __CodigoServico = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodigoServico'), 'CodigoServico', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_CodigoServico', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 671, 6), )

    
    CodigoServico = property(__CodigoServico.value, __CodigoServico.set, None, 'C\xf3digo do servi\xe7o.')

    
    # Element AliquotaServicos uses Python identifier AliquotaServicos
    __AliquotaServicos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AliquotaServicos'), 'AliquotaServicos', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_AliquotaServicos', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 676, 6), )

    
    AliquotaServicos = property(__AliquotaServicos.value, __AliquotaServicos.set, None, 'Valor da al\xedquota.')

    
    # Element ValorISS uses Python identifier ValorISS
    __ValorISS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorISS'), 'ValorISS', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_ValorISS', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 681, 6), )

    
    ValorISS = property(__ValorISS.value, __ValorISS.set, None, 'Valor do ISS.')

    
    # Element ValorCredito uses Python identifier ValorCredito
    __ValorCredito = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorCredito'), 'ValorCredito', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_ValorCredito', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 686, 6), )

    
    ValorCredito = property(__ValorCredito.value, __ValorCredito.set, None, 'Valor do cr\xe9dito gerado.')

    
    # Element ISSRetido uses Python identifier ISSRetido
    __ISSRetido = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ISSRetido'), 'ISSRetido', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_ISSRetido', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 691, 6), )

    
    ISSRetido = property(__ISSRetido.value, __ISSRetido.set, None, 'Reten\xe7\xe3o do ISS.')

    
    # Element CPFCNPJTomador uses Python identifier CPFCNPJTomador
    __CPFCNPJTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJTomador'), 'CPFCNPJTomador', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_CPFCNPJTomador', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 696, 6), )

    
    CPFCNPJTomador = property(__CPFCNPJTomador.value, __CPFCNPJTomador.set, None, 'CPF/CNPJ do tomador do servi\xe7o.')

    
    # Element InscricaoMunicipalTomador uses Python identifier InscricaoMunicipalTomador
    __InscricaoMunicipalTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalTomador'), 'InscricaoMunicipalTomador', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_InscricaoMunicipalTomador', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 701, 6), )

    
    InscricaoMunicipalTomador = property(__InscricaoMunicipalTomador.value, __InscricaoMunicipalTomador.set, None, 'Inscri\xe7\xe3o Municipal do Tomador.')

    
    # Element InscricaoEstadualTomador uses Python identifier InscricaoEstadualTomador
    __InscricaoEstadualTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InscricaoEstadualTomador'), 'InscricaoEstadualTomador', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_InscricaoEstadualTomador', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 706, 6), )

    
    InscricaoEstadualTomador = property(__InscricaoEstadualTomador.value, __InscricaoEstadualTomador.set, None, 'Inscri\xe7\xe3o Estadual do tomador.')

    
    # Element RazaoSocialTomador uses Python identifier RazaoSocialTomador
    __RazaoSocialTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RazaoSocialTomador'), 'RazaoSocialTomador', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_RazaoSocialTomador', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 711, 6), )

    
    RazaoSocialTomador = property(__RazaoSocialTomador.value, __RazaoSocialTomador.set, None, 'Nome/Raz\xe3o Social do tomador.')

    
    # Element EnderecoTomador uses Python identifier EnderecoTomador
    __EnderecoTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EnderecoTomador'), 'EnderecoTomador', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_EnderecoTomador', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 716, 6), )

    
    EnderecoTomador = property(__EnderecoTomador.value, __EnderecoTomador.set, None, 'Endere\xe7o do tomador.')

    
    # Element EmailTomador uses Python identifier EmailTomador
    __EmailTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EmailTomador'), 'EmailTomador', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_EmailTomador', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 721, 6), )

    
    EmailTomador = property(__EmailTomador.value, __EmailTomador.set, None, 'E-mail do tomador.')

    
    # Element CPFCNPJIntermediario uses Python identifier CPFCNPJIntermediario
    __CPFCNPJIntermediario = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJIntermediario'), 'CPFCNPJIntermediario', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_CPFCNPJIntermediario', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 726, 6), )

    
    CPFCNPJIntermediario = property(__CPFCNPJIntermediario.value, __CPFCNPJIntermediario.set, None, 'CNPJ do intermedi\xe1rio de servi\xe7o.')

    
    # Element InscricaoMunicipalIntermediario uses Python identifier InscricaoMunicipalIntermediario
    __InscricaoMunicipalIntermediario = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalIntermediario'), 'InscricaoMunicipalIntermediario', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_InscricaoMunicipalIntermediario', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 731, 6), )

    
    InscricaoMunicipalIntermediario = property(__InscricaoMunicipalIntermediario.value, __InscricaoMunicipalIntermediario.set, None, 'Inscri\xe7\xe3o Municipal do intermedi\xe1rio de servi\xe7o.')

    
    # Element ISSRetidoIntermediario uses Python identifier ISSRetidoIntermediario
    __ISSRetidoIntermediario = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ISSRetidoIntermediario'), 'ISSRetidoIntermediario', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_ISSRetidoIntermediario', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 736, 6), )

    
    ISSRetidoIntermediario = property(__ISSRetidoIntermediario.value, __ISSRetidoIntermediario.set, None, 'Reten\xe7\xe3o do ISS pelo intermedi\xe1rio de servi\xe7o.')

    
    # Element EmailIntermediario uses Python identifier EmailIntermediario
    __EmailIntermediario = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EmailIntermediario'), 'EmailIntermediario', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_EmailIntermediario', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 741, 6), )

    
    EmailIntermediario = property(__EmailIntermediario.value, __EmailIntermediario.set, None, 'E-mail do intermedi\xe1rio de servi\xe7o.')

    
    # Element Discriminacao uses Python identifier Discriminacao
    __Discriminacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Discriminacao'), 'Discriminacao', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_Discriminacao', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 746, 6), )

    
    Discriminacao = property(__Discriminacao.value, __Discriminacao.set, None, 'Descri\xe7\xe3o dos servi\xe7os.')

    
    # Element ValorCargaTributaria uses Python identifier ValorCargaTributaria
    __ValorCargaTributaria = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorCargaTributaria'), 'ValorCargaTributaria', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_ValorCargaTributaria', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 751, 6), )

    
    ValorCargaTributaria = property(__ValorCargaTributaria.value, __ValorCargaTributaria.set, None, 'Valor da carga tribut\xe1ria total em R$.')

    
    # Element PercentualCargaTributaria uses Python identifier PercentualCargaTributaria
    __PercentualCargaTributaria = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PercentualCargaTributaria'), 'PercentualCargaTributaria', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_PercentualCargaTributaria', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 756, 6), )

    
    PercentualCargaTributaria = property(__PercentualCargaTributaria.value, __PercentualCargaTributaria.set, None, 'Valor percentual da carga tribut\xe1ria.')

    
    # Element FonteCargaTributaria uses Python identifier FonteCargaTributaria
    __FonteCargaTributaria = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'FonteCargaTributaria'), 'FonteCargaTributaria', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_FonteCargaTributaria', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 761, 6), )

    
    FonteCargaTributaria = property(__FonteCargaTributaria.value, __FonteCargaTributaria.set, None, 'Fonte de informa\xe7\xe3o da carga tribut\xe1ria.')

    
    # Element CodigoCEI uses Python identifier CodigoCEI
    __CodigoCEI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodigoCEI'), 'CodigoCEI', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_CodigoCEI', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 766, 6), )

    
    CodigoCEI = property(__CodigoCEI.value, __CodigoCEI.set, None, 'C\xf3digo do CEI \u2013 Cadastro espec\xedfico do INSS.')

    
    # Element MatriculaObra uses Python identifier MatriculaObra
    __MatriculaObra = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MatriculaObra'), 'MatriculaObra', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_MatriculaObra', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 771, 6), )

    
    MatriculaObra = property(__MatriculaObra.value, __MatriculaObra.set, None, 'C\xf3digo que representa a matr\xedcula da obra no sistema de cadastro de obras.')

    
    # Element MunicipioPrestacao uses Python identifier MunicipioPrestacao
    __MunicipioPrestacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MunicipioPrestacao'), 'MunicipioPrestacao', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_MunicipioPrestacao', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 776, 6), )

    
    MunicipioPrestacao = property(__MunicipioPrestacao.value, __MunicipioPrestacao.set, None, 'C\xf3digo da cidade do munic\xedpio da presta\xe7\xe3o do servi\xe7o.')

    
    # Element NumeroEncapsulamento uses Python identifier NumeroEncapsulamento
    __NumeroEncapsulamento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroEncapsulamento'), 'NumeroEncapsulamento', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_NumeroEncapsulamento', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 781, 6), )

    
    NumeroEncapsulamento = property(__NumeroEncapsulamento.value, __NumeroEncapsulamento.set, None, 'C\xf3digo que representa o n\xfamero do encapsulamento.')

    
    # Element ValorTotalRecebido uses Python identifier ValorTotalRecebido
    __ValorTotalRecebido = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorTotalRecebido'), 'ValorTotalRecebido', '__httpwww_prefeitura_sp_gov_brnfetipos_tpNFe_ValorTotalRecebido', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 786, 6), )

    
    ValorTotalRecebido = property(__ValorTotalRecebido.value, __ValorTotalRecebido.set, None, 'Informe o valor total recebido.')

    _ElementMap.update({
        __Assinatura.name() : __Assinatura,
        __ChaveNFe.name() : __ChaveNFe,
        __DataEmissaoNFe.name() : __DataEmissaoNFe,
        __NumeroLote.name() : __NumeroLote,
        __ChaveRPS.name() : __ChaveRPS,
        __TipoRPS.name() : __TipoRPS,
        __DataEmissaoRPS.name() : __DataEmissaoRPS,
        __CPFCNPJPrestador.name() : __CPFCNPJPrestador,
        __RazaoSocialPrestador.name() : __RazaoSocialPrestador,
        __EnderecoPrestador.name() : __EnderecoPrestador,
        __EmailPrestador.name() : __EmailPrestador,
        __StatusNFe.name() : __StatusNFe,
        __DataCancelamento.name() : __DataCancelamento,
        __TributacaoNFe.name() : __TributacaoNFe,
        __OpcaoSimples.name() : __OpcaoSimples,
        __NumeroGuia.name() : __NumeroGuia,
        __DataQuitacaoGuia.name() : __DataQuitacaoGuia,
        __ValorServicos.name() : __ValorServicos,
        __ValorDeducoes.name() : __ValorDeducoes,
        __ValorPIS.name() : __ValorPIS,
        __ValorCOFINS.name() : __ValorCOFINS,
        __ValorINSS.name() : __ValorINSS,
        __ValorIR.name() : __ValorIR,
        __ValorCSLL.name() : __ValorCSLL,
        __CodigoServico.name() : __CodigoServico,
        __AliquotaServicos.name() : __AliquotaServicos,
        __ValorISS.name() : __ValorISS,
        __ValorCredito.name() : __ValorCredito,
        __ISSRetido.name() : __ISSRetido,
        __CPFCNPJTomador.name() : __CPFCNPJTomador,
        __InscricaoMunicipalTomador.name() : __InscricaoMunicipalTomador,
        __InscricaoEstadualTomador.name() : __InscricaoEstadualTomador,
        __RazaoSocialTomador.name() : __RazaoSocialTomador,
        __EnderecoTomador.name() : __EnderecoTomador,
        __EmailTomador.name() : __EmailTomador,
        __CPFCNPJIntermediario.name() : __CPFCNPJIntermediario,
        __InscricaoMunicipalIntermediario.name() : __InscricaoMunicipalIntermediario,
        __ISSRetidoIntermediario.name() : __ISSRetidoIntermediario,
        __EmailIntermediario.name() : __EmailIntermediario,
        __Discriminacao.name() : __Discriminacao,
        __ValorCargaTributaria.name() : __ValorCargaTributaria,
        __PercentualCargaTributaria.name() : __PercentualCargaTributaria,
        __FonteCargaTributaria.name() : __FonteCargaTributaria,
        __CodigoCEI.name() : __CodigoCEI,
        __MatriculaObra.name() : __MatriculaObra,
        __MunicipioPrestacao.name() : __MunicipioPrestacao,
        __NumeroEncapsulamento.name() : __NumeroEncapsulamento,
        __ValorTotalRecebido.name() : __ValorTotalRecebido
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpNFe = tpNFe
Namespace.addCategoryObject('typeBinding', 'tpNFe', tpNFe)


# Complex type {http://www.prefeitura.sp.gov.br/nfe/tipos}tpRPS with content type ELEMENT_ONLY
class tpRPS (pyxb.binding.basis.complexTypeDefinition):
    """Tipo que representa um RPS."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpRPS')
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 793, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Assinatura uses Python identifier Assinatura
    __Assinatura = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Assinatura'), 'Assinatura', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_Assinatura', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 798, 6), )

    
    Assinatura = property(__Assinatura.value, __Assinatura.set, None, 'Assinatura digital do RPS.')

    
    # Element ChaveRPS uses Python identifier ChaveRPS
    __ChaveRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ChaveRPS'), 'ChaveRPS', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_ChaveRPS', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 803, 6), )

    
    ChaveRPS = property(__ChaveRPS.value, __ChaveRPS.set, None, 'Informe a chave do RPS emitido.')

    
    # Element TipoRPS uses Python identifier TipoRPS
    __TipoRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TipoRPS'), 'TipoRPS', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_TipoRPS', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 808, 6), )

    
    TipoRPS = property(__TipoRPS.value, __TipoRPS.set, None, 'Informe o Tipo do RPS emitido.')

    
    # Element DataEmissao uses Python identifier DataEmissao
    __DataEmissao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DataEmissao'), 'DataEmissao', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_DataEmissao', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 813, 6), )

    
    DataEmissao = property(__DataEmissao.value, __DataEmissao.set, None, 'Informe a Data de emiss\xe3o do RPS.')

    
    # Element StatusRPS uses Python identifier StatusRPS
    __StatusRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'StatusRPS'), 'StatusRPS', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_StatusRPS', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 818, 6), )

    
    StatusRPS = property(__StatusRPS.value, __StatusRPS.set, None, 'Informe o Status do RPS.')

    
    # Element TributacaoRPS uses Python identifier TributacaoRPS
    __TributacaoRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TributacaoRPS'), 'TributacaoRPS', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_TributacaoRPS', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 823, 6), )

    
    TributacaoRPS = property(__TributacaoRPS.value, __TributacaoRPS.set, None, 'Informe o tipo de tributa\xe7\xe3o do RPS.')

    
    # Element ValorServicos uses Python identifier ValorServicos
    __ValorServicos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorServicos'), 'ValorServicos', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_ValorServicos', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 828, 6), )

    
    ValorServicos = property(__ValorServicos.value, __ValorServicos.set, None, 'Informe o valor dos servi\xe7os prestados.')

    
    # Element ValorDeducoes uses Python identifier ValorDeducoes
    __ValorDeducoes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorDeducoes'), 'ValorDeducoes', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_ValorDeducoes', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 833, 6), )

    
    ValorDeducoes = property(__ValorDeducoes.value, __ValorDeducoes.set, None, 'Informe o valor das dedu\xe7\xf5es.')

    
    # Element ValorPIS uses Python identifier ValorPIS
    __ValorPIS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorPIS'), 'ValorPIS', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_ValorPIS', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 838, 6), )

    
    ValorPIS = property(__ValorPIS.value, __ValorPIS.set, None, 'Informe o valor da reten\xe7\xe3o do PIS.')

    
    # Element ValorCOFINS uses Python identifier ValorCOFINS
    __ValorCOFINS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorCOFINS'), 'ValorCOFINS', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_ValorCOFINS', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 843, 6), )

    
    ValorCOFINS = property(__ValorCOFINS.value, __ValorCOFINS.set, None, 'Informe o valor da reten\xe7\xe3o do COFINS.')

    
    # Element ValorINSS uses Python identifier ValorINSS
    __ValorINSS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorINSS'), 'ValorINSS', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_ValorINSS', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 848, 6), )

    
    ValorINSS = property(__ValorINSS.value, __ValorINSS.set, None, 'Informe o valor da reten\xe7\xe3o do INSS.')

    
    # Element ValorIR uses Python identifier ValorIR
    __ValorIR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorIR'), 'ValorIR', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_ValorIR', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 853, 6), )

    
    ValorIR = property(__ValorIR.value, __ValorIR.set, None, 'Informe o valor da reten\xe7\xe3o do IR.')

    
    # Element ValorCSLL uses Python identifier ValorCSLL
    __ValorCSLL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorCSLL'), 'ValorCSLL', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_ValorCSLL', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 858, 6), )

    
    ValorCSLL = property(__ValorCSLL.value, __ValorCSLL.set, None, 'Informe o valor da reten\xe7\xe3o do CSLL.')

    
    # Element CodigoServico uses Python identifier CodigoServico
    __CodigoServico = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodigoServico'), 'CodigoServico', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_CodigoServico', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 863, 6), )

    
    CodigoServico = property(__CodigoServico.value, __CodigoServico.set, None, 'Informe o c\xf3digo do servi\xe7o do RPS. Este c\xf3digo deve pertencer \xe0 lista de servi\xe7os.')

    
    # Element AliquotaServicos uses Python identifier AliquotaServicos
    __AliquotaServicos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AliquotaServicos'), 'AliquotaServicos', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_AliquotaServicos', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 868, 6), )

    
    AliquotaServicos = property(__AliquotaServicos.value, __AliquotaServicos.set, None, 'Informe o valor da al\xedquota. Obs. O conte\xfado deste campo ser\xe1 ignorado caso a tributa\xe7\xe3o ocorra no munic\xedpio (Situa\xe7\xe3o do RPS = T ).')

    
    # Element ISSRetido uses Python identifier ISSRetido
    __ISSRetido = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ISSRetido'), 'ISSRetido', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_ISSRetido', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 873, 6), )

    
    ISSRetido = property(__ISSRetido.value, __ISSRetido.set, None, 'Informe a reten\xe7\xe3o.')

    
    # Element CPFCNPJTomador uses Python identifier CPFCNPJTomador
    __CPFCNPJTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJTomador'), 'CPFCNPJTomador', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_CPFCNPJTomador', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 878, 6), )

    
    CPFCNPJTomador = property(__CPFCNPJTomador.value, __CPFCNPJTomador.set, None, 'Informe o CPF/CNPJ do tomador do servi\xe7o. O conte\xfado deste campo ser\xe1 ignorado caso o campo InscricaoMunicipalTomador esteja preenchido.')

    
    # Element InscricaoMunicipalTomador uses Python identifier InscricaoMunicipalTomador
    __InscricaoMunicipalTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalTomador'), 'InscricaoMunicipalTomador', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_InscricaoMunicipalTomador', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 883, 6), )

    
    InscricaoMunicipalTomador = property(__InscricaoMunicipalTomador.value, __InscricaoMunicipalTomador.set, None, 'Informe a Inscri\xe7\xe3o Municipal do Tomador. ATEN\xc7\xc3O: Este campo s\xf3 dever\xe1 ser preenchido para tomadores estabelecidos no munic\xedpio de S\xe3o Paulo (CCM). Quando este campo for preenchido, seu conte\xfado ser\xe1 considerado como priorit\xe1rio com rela\xe7\xe3o ao campo de CPF/CNPJ do Tomador, sendo utilizado para identificar o Tomador e recuperar seus dados da base de dados da Prefeitura.')

    
    # Element InscricaoEstadualTomador uses Python identifier InscricaoEstadualTomador
    __InscricaoEstadualTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InscricaoEstadualTomador'), 'InscricaoEstadualTomador', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_InscricaoEstadualTomador', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 888, 6), )

    
    InscricaoEstadualTomador = property(__InscricaoEstadualTomador.value, __InscricaoEstadualTomador.set, None, 'Informe a inscri\xe7\xe3o estadual do tomador. Este campo ser\xe1 ignorado caso seja fornecido um CPF/CNPJ ou a Inscri\xe7\xe3o Municipal do tomador perten\xe7a ao munic\xedpio de S\xe3o Paulo.')

    
    # Element RazaoSocialTomador uses Python identifier RazaoSocialTomador
    __RazaoSocialTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RazaoSocialTomador'), 'RazaoSocialTomador', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_RazaoSocialTomador', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 893, 6), )

    
    RazaoSocialTomador = property(__RazaoSocialTomador.value, __RazaoSocialTomador.set, None, 'Informe o Nome/Raz\xe3o Social do tomador. Este campo \xe9 obrigat\xf3rio apenas para tomadores Pessoa Jur\xeddica (CNPJ). Este campo ser\xe1 ignorado caso seja fornecido um CPF/CNPJ ou a Inscri\xe7\xe3o Municipal do tomador perten\xe7a ao munic\xedpio de S\xe3o Paulo.')

    
    # Element EnderecoTomador uses Python identifier EnderecoTomador
    __EnderecoTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EnderecoTomador'), 'EnderecoTomador', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_EnderecoTomador', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 898, 6), )

    
    EnderecoTomador = property(__EnderecoTomador.value, __EnderecoTomador.set, None, 'Informe o endere\xe7o do tomador. Os campos do endere\xe7o s\xe3o obrigat\xf3rios apenas para tomadores pessoa jur\xeddica (CNPJ informado). O conte\xfado destes campos ser\xe1 ignorado caso seja fornecido um CPF/CNPJ ou a Inscri\xe7\xe3o Municipal do tomador perten\xe7a ao munic\xedpio de S\xe3o Paulo.')

    
    # Element EmailTomador uses Python identifier EmailTomador
    __EmailTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EmailTomador'), 'EmailTomador', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_EmailTomador', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 903, 6), )

    
    EmailTomador = property(__EmailTomador.value, __EmailTomador.set, None, 'Informe o e-mail do tomador.')

    
    # Element CPFCNPJIntermediario uses Python identifier CPFCNPJIntermediario
    __CPFCNPJIntermediario = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJIntermediario'), 'CPFCNPJIntermediario', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_CPFCNPJIntermediario', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 908, 6), )

    
    CPFCNPJIntermediario = property(__CPFCNPJIntermediario.value, __CPFCNPJIntermediario.set, None, 'CNPJ do intermedi\xe1rio de servi\xe7o.')

    
    # Element InscricaoMunicipalIntermediario uses Python identifier InscricaoMunicipalIntermediario
    __InscricaoMunicipalIntermediario = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalIntermediario'), 'InscricaoMunicipalIntermediario', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_InscricaoMunicipalIntermediario', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 913, 6), )

    
    InscricaoMunicipalIntermediario = property(__InscricaoMunicipalIntermediario.value, __InscricaoMunicipalIntermediario.set, None, 'Inscri\xe7\xe3o Municipal do intermedi\xe1rio de servi\xe7o.')

    
    # Element ISSRetidoIntermediario uses Python identifier ISSRetidoIntermediario
    __ISSRetidoIntermediario = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ISSRetidoIntermediario'), 'ISSRetidoIntermediario', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_ISSRetidoIntermediario', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 918, 6), )

    
    ISSRetidoIntermediario = property(__ISSRetidoIntermediario.value, __ISSRetidoIntermediario.set, None, 'Reten\xe7\xe3o do ISS pelo intermedi\xe1rio de servi\xe7o.')

    
    # Element EmailIntermediario uses Python identifier EmailIntermediario
    __EmailIntermediario = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EmailIntermediario'), 'EmailIntermediario', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_EmailIntermediario', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 923, 6), )

    
    EmailIntermediario = property(__EmailIntermediario.value, __EmailIntermediario.set, None, 'E-mail do intermedi\xe1rio de servi\xe7o.')

    
    # Element Discriminacao uses Python identifier Discriminacao
    __Discriminacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Discriminacao'), 'Discriminacao', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_Discriminacao', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 928, 6), )

    
    Discriminacao = property(__Discriminacao.value, __Discriminacao.set, None, 'Informe a discrimina\xe7\xe3o dos servi\xe7os.')

    
    # Element ValorCargaTributaria uses Python identifier ValorCargaTributaria
    __ValorCargaTributaria = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorCargaTributaria'), 'ValorCargaTributaria', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_ValorCargaTributaria', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 933, 6), )

    
    ValorCargaTributaria = property(__ValorCargaTributaria.value, __ValorCargaTributaria.set, None, 'Valor da carga tribut\xe1ria total em R$.')

    
    # Element PercentualCargaTributaria uses Python identifier PercentualCargaTributaria
    __PercentualCargaTributaria = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PercentualCargaTributaria'), 'PercentualCargaTributaria', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_PercentualCargaTributaria', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 938, 6), )

    
    PercentualCargaTributaria = property(__PercentualCargaTributaria.value, __PercentualCargaTributaria.set, None, 'Valor percentual da carga tribut\xe1ria.')

    
    # Element FonteCargaTributaria uses Python identifier FonteCargaTributaria
    __FonteCargaTributaria = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'FonteCargaTributaria'), 'FonteCargaTributaria', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_FonteCargaTributaria', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 943, 6), )

    
    FonteCargaTributaria = property(__FonteCargaTributaria.value, __FonteCargaTributaria.set, None, 'Fonte de informa\xe7\xe3o da carga tribut\xe1ria.')

    
    # Element CodigoCEI uses Python identifier CodigoCEI
    __CodigoCEI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodigoCEI'), 'CodigoCEI', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_CodigoCEI', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 948, 6), )

    
    CodigoCEI = property(__CodigoCEI.value, __CodigoCEI.set, None, 'C\xf3digo do CEI \u2013 Cadastro espec\xedfico do INSS.')

    
    # Element MatriculaObra uses Python identifier MatriculaObra
    __MatriculaObra = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MatriculaObra'), 'MatriculaObra', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_MatriculaObra', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 953, 6), )

    
    MatriculaObra = property(__MatriculaObra.value, __MatriculaObra.set, None, 'C\xf3digo que representa a matr\xedcula da obra no sistema de cadastro de obras.')

    
    # Element MunicipioPrestacao uses Python identifier MunicipioPrestacao
    __MunicipioPrestacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MunicipioPrestacao'), 'MunicipioPrestacao', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_MunicipioPrestacao', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 958, 6), )

    
    MunicipioPrestacao = property(__MunicipioPrestacao.value, __MunicipioPrestacao.set, None, 'C\xf3digo da cidade do munic\xedpio da presta\xe7\xe3o do servi\xe7o.')

    
    # Element NumeroEncapsulamento uses Python identifier NumeroEncapsulamento
    __NumeroEncapsulamento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroEncapsulamento'), 'NumeroEncapsulamento', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_NumeroEncapsulamento', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 963, 6), )

    
    NumeroEncapsulamento = property(__NumeroEncapsulamento.value, __NumeroEncapsulamento.set, None, 'C\xf3digo que representa o n\xfamero do encapsulamento da obra.')

    
    # Element ValorTotalRecebido uses Python identifier ValorTotalRecebido
    __ValorTotalRecebido = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorTotalRecebido'), 'ValorTotalRecebido', '__httpwww_prefeitura_sp_gov_brnfetipos_tpRPS_ValorTotalRecebido', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 968, 6), )

    
    ValorTotalRecebido = property(__ValorTotalRecebido.value, __ValorTotalRecebido.set, None, 'Informe o valor total recebido.')

    _ElementMap.update({
        __Assinatura.name() : __Assinatura,
        __ChaveRPS.name() : __ChaveRPS,
        __TipoRPS.name() : __TipoRPS,
        __DataEmissao.name() : __DataEmissao,
        __StatusRPS.name() : __StatusRPS,
        __TributacaoRPS.name() : __TributacaoRPS,
        __ValorServicos.name() : __ValorServicos,
        __ValorDeducoes.name() : __ValorDeducoes,
        __ValorPIS.name() : __ValorPIS,
        __ValorCOFINS.name() : __ValorCOFINS,
        __ValorINSS.name() : __ValorINSS,
        __ValorIR.name() : __ValorIR,
        __ValorCSLL.name() : __ValorCSLL,
        __CodigoServico.name() : __CodigoServico,
        __AliquotaServicos.name() : __AliquotaServicos,
        __ISSRetido.name() : __ISSRetido,
        __CPFCNPJTomador.name() : __CPFCNPJTomador,
        __InscricaoMunicipalTomador.name() : __InscricaoMunicipalTomador,
        __InscricaoEstadualTomador.name() : __InscricaoEstadualTomador,
        __RazaoSocialTomador.name() : __RazaoSocialTomador,
        __EnderecoTomador.name() : __EnderecoTomador,
        __EmailTomador.name() : __EmailTomador,
        __CPFCNPJIntermediario.name() : __CPFCNPJIntermediario,
        __InscricaoMunicipalIntermediario.name() : __InscricaoMunicipalIntermediario,
        __ISSRetidoIntermediario.name() : __ISSRetidoIntermediario,
        __EmailIntermediario.name() : __EmailIntermediario,
        __Discriminacao.name() : __Discriminacao,
        __ValorCargaTributaria.name() : __ValorCargaTributaria,
        __PercentualCargaTributaria.name() : __PercentualCargaTributaria,
        __FonteCargaTributaria.name() : __FonteCargaTributaria,
        __CodigoCEI.name() : __CodigoCEI,
        __MatriculaObra.name() : __MatriculaObra,
        __MunicipioPrestacao.name() : __MunicipioPrestacao,
        __NumeroEncapsulamento.name() : __NumeroEncapsulamento,
        __ValorTotalRecebido.name() : __ValorTotalRecebido
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpRPS = tpRPS
Namespace.addCategoryObject('typeBinding', 'tpRPS', tpRPS)




tpEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Codigo'), tpCodigoEvento, scope=tpEvento, documentation='C\xf3digo do evento.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 387, 6)))

tpEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Descricao'), tpDescricaoEvento, scope=tpEvento, documentation='Descri\xe7\xe3o do enveto.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 392, 6)))

tpEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ChaveRPS'), tpChaveRPS, scope=tpEvento, documentation='Chave do RPS.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 401, 8)))

tpEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ChaveNFe'), tpChaveNFe, scope=tpEvento, documentation='Chave da NFe.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 406, 8)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 392, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 397, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpEvento._UseForTag(pyxb.namespace.ExpandedName(None, 'Codigo')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 387, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tpEvento._UseForTag(pyxb.namespace.ExpandedName(None, 'Descricao')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 392, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(tpEvento._UseForTag(pyxb.namespace.ExpandedName(None, 'ChaveRPS')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 401, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(tpEvento._UseForTag(pyxb.namespace.ExpandedName(None, 'ChaveNFe')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 406, 8))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpEvento._Automaton = _BuildAutomaton()




tpCPFCNPJ._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPF'), tpCPF, scope=tpCPFCNPJ, location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 419, 6)))

tpCPFCNPJ._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CNPJ'), tpCNPJ, scope=tpCPFCNPJ, location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 420, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpCPFCNPJ._UseForTag(pyxb.namespace.ExpandedName(None, 'CPF')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 419, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpCPFCNPJ._UseForTag(pyxb.namespace.ExpandedName(None, 'CNPJ')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 420, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpCPFCNPJ._Automaton = _BuildAutomaton_()




tpChaveNFeRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ChaveNFe'), tpChaveNFe, scope=tpChaveNFeRPS, documentation='Chave da NFS-e gerada.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 428, 6)))

tpChaveNFeRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ChaveRPS'), tpChaveRPS, scope=tpChaveNFeRPS, documentation='Chave do RPS substitu\xeddo.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 433, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpChaveNFeRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'ChaveNFe')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 428, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpChaveNFeRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'ChaveRPS')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 433, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpChaveNFeRPS._Automaton = _BuildAutomaton_2()




tpChaveNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador'), tpInscricaoMunicipal, scope=tpChaveNFe, documentation='Inscri\xe7\xe3o municipal do prestador de servi\xe7os.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 445, 6)))

tpChaveNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroNFe'), tpNumero, scope=tpChaveNFe, documentation='N\xfamero da NFS-e.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 450, 6)))

tpChaveNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodigoVerificacao'), tpCodigoVerificacao, scope=tpChaveNFe, documentation='C\xf3digo de verifica\xe7\xe3o da NFS-e.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 455, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 455, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpChaveNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 445, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpChaveNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroNFe')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 450, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tpChaveNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'CodigoVerificacao')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 455, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpChaveNFe._Automaton = _BuildAutomaton_3()




tpChaveRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador'), tpInscricaoMunicipal, scope=tpChaveRPS, documentation='Inscri\xe7\xe3o municipal do prestador de servi\xe7os.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 467, 6)))

tpChaveRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SerieRPS'), tpSerieRPS, scope=tpChaveRPS, documentation='S\xe9rie do RPS.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 472, 6)))

tpChaveRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroRPS'), tpNumero, scope=tpChaveRPS, documentation='N\xfamero do RPS.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 477, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 472, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpChaveRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 467, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpChaveRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'SerieRPS')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 472, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpChaveRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroRPS')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 477, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpChaveRPS._Automaton = _BuildAutomaton_4()




tpEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TipoLogradouro'), tpTipoLogradouro, scope=tpEndereco, location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 489, 6)))

tpEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Logradouro'), tpLogradouro, scope=tpEndereco, location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 490, 6)))

tpEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroEndereco'), tpNumeroEndereco, scope=tpEndereco, location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 491, 6)))

tpEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ComplementoEndereco'), tpComplementoEndereco, scope=tpEndereco, location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 492, 6)))

tpEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Bairro'), tpBairro, scope=tpEndereco, location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 493, 6)))

tpEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Cidade'), tpCidade, scope=tpEndereco, location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 494, 6)))

tpEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'UF'), tpUF, scope=tpEndereco, location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 495, 6)))

tpEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CEP'), tpCEP, scope=tpEndereco, location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 496, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 489, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 490, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 491, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 492, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 493, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 494, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 495, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 496, 6))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tpEndereco._UseForTag(pyxb.namespace.ExpandedName(None, 'TipoLogradouro')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 489, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(tpEndereco._UseForTag(pyxb.namespace.ExpandedName(None, 'Logradouro')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 490, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(tpEndereco._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroEndereco')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 491, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(tpEndereco._UseForTag(pyxb.namespace.ExpandedName(None, 'ComplementoEndereco')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 492, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(tpEndereco._UseForTag(pyxb.namespace.ExpandedName(None, 'Bairro')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 493, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(tpEndereco._UseForTag(pyxb.namespace.ExpandedName(None, 'Cidade')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 494, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(tpEndereco._UseForTag(pyxb.namespace.ExpandedName(None, 'UF')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 495, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(tpEndereco._UseForTag(pyxb.namespace.ExpandedName(None, 'CEP')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 496, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
tpEndereco._Automaton = _BuildAutomaton_5()




tpInformacoesLote._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroLote'), tpNumero, scope=tpInformacoesLote, documentation='N\xfamero de lote.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 504, 6)))

tpInformacoesLote._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador'), tpInscricaoMunicipal, scope=tpInformacoesLote, documentation='Inscri\xe7\xe3o municipal do prestador dos RPS contidos no lote.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 509, 6)))

tpInformacoesLote._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), tpCPFCNPJ, scope=tpInformacoesLote, documentation='CNPJ do remetente autorizado a transmitir a mensagem XML.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 514, 6)))

tpInformacoesLote._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DataEnvioLote'), pyxb.binding.datatypes.dateTime, scope=tpInformacoesLote, documentation='Data/hora de envio do lote.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 519, 6)))

tpInformacoesLote._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'QtdNotasProcessadas'), tpQuantidade, scope=tpInformacoesLote, documentation='Quantidade de RPS do lote.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 524, 6)))

tpInformacoesLote._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TempoProcessamento'), tpTempoProcessamento, scope=tpInformacoesLote, documentation='Tempo de processamento do lote.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 529, 6)))

tpInformacoesLote._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorTotalServicos'), tpValor, scope=tpInformacoesLote, documentation='Valor total dos servi\xe7os dos RPS contidos na mensagem XML.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 534, 6)))

tpInformacoesLote._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorTotalDeducoes'), tpValor, scope=tpInformacoesLote, documentation='Valor total das dedu\xe7\xf5es dos RPS contidos na mensagem XML.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 539, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 504, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 539, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpInformacoesLote._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroLote')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 504, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpInformacoesLote._UseForTag(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 509, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpInformacoesLote._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 514, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpInformacoesLote._UseForTag(pyxb.namespace.ExpandedName(None, 'DataEnvioLote')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 519, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpInformacoesLote._UseForTag(pyxb.namespace.ExpandedName(None, 'QtdNotasProcessadas')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 524, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpInformacoesLote._UseForTag(pyxb.namespace.ExpandedName(None, 'TempoProcessamento')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 529, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpInformacoesLote._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorTotalServicos')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 534, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(tpInformacoesLote._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorTotalDeducoes')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 539, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpInformacoesLote._Automaton = _BuildAutomaton_6()




tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Assinatura'), tpAssinatura, scope=tpNFe, documentation='Assinatura digital da NFS-e.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 551, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ChaveNFe'), tpChaveNFe, scope=tpNFe, documentation='Chave de identifica\xe7\xe3o da NFS-e.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 556, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DataEmissaoNFe'), pyxb.binding.datatypes.dateTime, scope=tpNFe, documentation='Data de emiss\xe3o da NFS-e', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 561, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroLote'), tpNumero, scope=tpNFe, documentation='N\xfamero de lote gerador da NFS-e.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 566, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ChaveRPS'), tpChaveRPS, scope=tpNFe, documentation='Chave do RPS que originou a NFS-e.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 571, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TipoRPS'), tpTipoRPS, scope=tpNFe, documentation='Tipo do RPS emitido.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 576, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DataEmissaoRPS'), pyxb.binding.datatypes.date, scope=tpNFe, documentation='Data de emiss\xe3o do RPS que originou a NFS-e.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 581, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJPrestador'), tpCPFCNPJ, scope=tpNFe, documentation='CPF/CNPJ do Prestador do servi\xe7o.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 586, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RazaoSocialPrestador'), tpRazaoSocial, scope=tpNFe, documentation='Nome/Raz\xe3o Social do Prestador.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 591, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EnderecoPrestador'), tpEndereco, scope=tpNFe, documentation='Endere\xe7o do Prestador.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 596, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EmailPrestador'), tpEmail, scope=tpNFe, documentation='E-mail do Prestador.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 601, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'StatusNFe'), tpStatusNFe, scope=tpNFe, documentation='Status da NFS-e.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 606, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DataCancelamento'), pyxb.binding.datatypes.dateTime, scope=tpNFe, documentation='Data de cancelamento da NFS-e.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 611, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TributacaoNFe'), tpTributacaoNFe, scope=tpNFe, documentation='Tributa\xe7\xe3o da NFS-e.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 616, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'OpcaoSimples'), tpOpcaoSimples, scope=tpNFe, documentation='Op\xe7\xe3o pelo Simples.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 621, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroGuia'), tpNumero, scope=tpNFe, documentation='N\xfamero da guia vinculada a NFS-e.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 626, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DataQuitacaoGuia'), pyxb.binding.datatypes.date, scope=tpNFe, documentation='Data de quita\xe7\xe3o da guia vinculada a NFS-e.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 631, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorServicos'), tpValor, scope=tpNFe, documentation='Valor dos servi\xe7os prestados.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 636, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorDeducoes'), tpValor, scope=tpNFe, documentation='Valor das dedu\xe7\xf5es.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 641, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorPIS'), tpValor, scope=tpNFe, documentation='Valor da reten\xe7\xe3o do PIS.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 646, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorCOFINS'), tpValor, scope=tpNFe, documentation='Valor da reten\xe7\xe3o do COFINS.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 651, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorINSS'), tpValor, scope=tpNFe, documentation='Valor da reten\xe7\xe3o do INSS.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 656, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorIR'), tpValor, scope=tpNFe, documentation='Valor da reten\xe7\xe3o do IR.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 661, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorCSLL'), tpValor, scope=tpNFe, documentation='Valor da reten\xe7\xe3o do CSLL.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 666, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodigoServico'), tpCodigoServico, scope=tpNFe, documentation='C\xf3digo do servi\xe7o.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 671, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AliquotaServicos'), tpAliquota, scope=tpNFe, documentation='Valor da al\xedquota.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 676, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorISS'), tpValor, scope=tpNFe, documentation='Valor do ISS.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 681, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorCredito'), tpValor, scope=tpNFe, documentation='Valor do cr\xe9dito gerado.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 686, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ISSRetido'), pyxb.binding.datatypes.boolean, scope=tpNFe, documentation='Reten\xe7\xe3o do ISS.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 691, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJTomador'), tpCPFCNPJ, scope=tpNFe, documentation='CPF/CNPJ do tomador do servi\xe7o.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 696, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalTomador'), tpInscricaoMunicipal, scope=tpNFe, documentation='Inscri\xe7\xe3o Municipal do Tomador.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 701, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InscricaoEstadualTomador'), tpInscricaoEstadual, scope=tpNFe, documentation='Inscri\xe7\xe3o Estadual do tomador.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 706, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RazaoSocialTomador'), tpRazaoSocial, scope=tpNFe, documentation='Nome/Raz\xe3o Social do tomador.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 711, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EnderecoTomador'), tpEndereco, scope=tpNFe, documentation='Endere\xe7o do tomador.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 716, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EmailTomador'), tpEmail, scope=tpNFe, documentation='E-mail do tomador.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 721, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJIntermediario'), tpCPFCNPJ, scope=tpNFe, documentation='CNPJ do intermedi\xe1rio de servi\xe7o.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 726, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalIntermediario'), tpInscricaoMunicipal, scope=tpNFe, documentation='Inscri\xe7\xe3o Municipal do intermedi\xe1rio de servi\xe7o.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 731, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ISSRetidoIntermediario'), pyxb.binding.datatypes.string, scope=tpNFe, documentation='Reten\xe7\xe3o do ISS pelo intermedi\xe1rio de servi\xe7o.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 736, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EmailIntermediario'), tpEmail, scope=tpNFe, documentation='E-mail do intermedi\xe1rio de servi\xe7o.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 741, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Discriminacao'), tpDiscriminacao, scope=tpNFe, documentation='Descri\xe7\xe3o dos servi\xe7os.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 746, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorCargaTributaria'), tpValor, scope=tpNFe, documentation='Valor da carga tribut\xe1ria total em R$.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 751, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PercentualCargaTributaria'), tpPercentualCargaTributaria, scope=tpNFe, documentation='Valor percentual da carga tribut\xe1ria.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 756, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'FonteCargaTributaria'), tpFonteCargaTributaria, scope=tpNFe, documentation='Fonte de informa\xe7\xe3o da carga tribut\xe1ria.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 761, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodigoCEI'), tpNumero, scope=tpNFe, documentation='C\xf3digo do CEI \u2013 Cadastro espec\xedfico do INSS.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 766, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MatriculaObra'), tpNumero, scope=tpNFe, documentation='C\xf3digo que representa a matr\xedcula da obra no sistema de cadastro de obras.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 771, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MunicipioPrestacao'), tpCidade, scope=tpNFe, documentation='C\xf3digo da cidade do munic\xedpio da presta\xe7\xe3o do servi\xe7o.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 776, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroEncapsulamento'), tpNumero, scope=tpNFe, documentation='C\xf3digo que representa o n\xfamero do encapsulamento.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 781, 6)))

tpNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorTotalRecebido'), tpValor, scope=tpNFe, documentation='Informe o valor total recebido.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 786, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 551, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 566, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 571, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 576, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 581, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 601, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 611, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 626, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 631, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 641, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 646, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 651, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 656, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 661, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 666, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 696, 6))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 701, 6))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 706, 6))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 711, 6))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 716, 6))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 721, 6))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 726, 6))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 731, 6))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 736, 6))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 741, 6))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 751, 6))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 756, 6))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 761, 6))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 766, 6))
    counters.add(cc_28)
    cc_29 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 771, 6))
    counters.add(cc_29)
    cc_30 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 776, 6))
    counters.add(cc_30)
    cc_31 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 781, 6))
    counters.add(cc_31)
    cc_32 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 786, 6))
    counters.add(cc_32)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'Assinatura')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 551, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'ChaveNFe')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 556, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'DataEmissaoNFe')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 561, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroLote')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 566, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'ChaveRPS')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 571, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'TipoRPS')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 576, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'DataEmissaoRPS')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 581, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJPrestador')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 586, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'RazaoSocialPrestador')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 591, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'EnderecoPrestador')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 596, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'EmailPrestador')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 601, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'StatusNFe')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 606, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'DataCancelamento')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 611, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'TributacaoNFe')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 616, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'OpcaoSimples')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 621, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroGuia')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 626, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'DataQuitacaoGuia')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 631, 6))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorServicos')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 636, 6))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorDeducoes')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 641, 6))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorPIS')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 646, 6))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorCOFINS')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 651, 6))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorINSS')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 656, 6))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorIR')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 661, 6))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorCSLL')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 666, 6))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'CodigoServico')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 671, 6))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'AliquotaServicos')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 676, 6))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorISS')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 681, 6))
    st_26 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorCredito')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 686, 6))
    st_27 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'ISSRetido')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 691, 6))
    st_28 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJTomador')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 696, 6))
    st_29 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalTomador')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 701, 6))
    st_30 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'InscricaoEstadualTomador')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 706, 6))
    st_31 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'RazaoSocialTomador')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 711, 6))
    st_32 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_32)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'EnderecoTomador')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 716, 6))
    st_33 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_33)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'EmailTomador')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 721, 6))
    st_34 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_34)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJIntermediario')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 726, 6))
    st_35 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_35)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalIntermediario')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 731, 6))
    st_36 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_36)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'ISSRetidoIntermediario')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 736, 6))
    st_37 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_37)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'EmailIntermediario')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 741, 6))
    st_38 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_38)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'Discriminacao')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 746, 6))
    st_39 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_39)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_25, False))
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorCargaTributaria')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 751, 6))
    st_40 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_40)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_26, False))
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'PercentualCargaTributaria')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 756, 6))
    st_41 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_41)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_27, False))
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'FonteCargaTributaria')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 761, 6))
    st_42 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_42)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_28, False))
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'CodigoCEI')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 766, 6))
    st_43 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_43)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_29, False))
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'MatriculaObra')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 771, 6))
    st_44 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_44)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_30, False))
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'MunicipioPrestacao')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 776, 6))
    st_45 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_45)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_31, False))
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroEncapsulamento')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 781, 6))
    st_46 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_46)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_32, False))
    symbol = pyxb.binding.content.ElementUse(tpNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorTotalRecebido')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 786, 6))
    st_47 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_47)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
         ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
         ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
         ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
         ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
         ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    transitions.append(fac.Transition(st_34, [
         ]))
    transitions.append(fac.Transition(st_35, [
         ]))
    transitions.append(fac.Transition(st_36, [
         ]))
    transitions.append(fac.Transition(st_37, [
         ]))
    transitions.append(fac.Transition(st_38, [
         ]))
    transitions.append(fac.Transition(st_39, [
         ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_31._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_32._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_33._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_34._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_35._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_22, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_22, False) ]))
    st_36._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_23, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_23, False) ]))
    st_37._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_24, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_24, False) ]))
    st_38._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_40, [
         ]))
    transitions.append(fac.Transition(st_41, [
         ]))
    transitions.append(fac.Transition(st_42, [
         ]))
    transitions.append(fac.Transition(st_43, [
         ]))
    transitions.append(fac.Transition(st_44, [
         ]))
    transitions.append(fac.Transition(st_45, [
         ]))
    transitions.append(fac.Transition(st_46, [
         ]))
    transitions.append(fac.Transition(st_47, [
         ]))
    st_39._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_25, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_25, False) ]))
    st_40._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_26, True) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_26, False) ]))
    st_41._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_27, True) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_27, False) ]))
    st_42._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_28, True) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_28, False) ]))
    st_43._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_29, True) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_29, False) ]))
    st_44._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_30, True) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_30, False) ]))
    st_45._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_31, True) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_31, False) ]))
    st_46._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_32, True) ]))
    st_47._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpNFe._Automaton = _BuildAutomaton_7()




tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Assinatura'), tpAssinatura, scope=tpRPS, documentation='Assinatura digital do RPS.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 798, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ChaveRPS'), tpChaveRPS, scope=tpRPS, documentation='Informe a chave do RPS emitido.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 803, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TipoRPS'), tpTipoRPS, scope=tpRPS, documentation='Informe o Tipo do RPS emitido.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 808, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DataEmissao'), pyxb.binding.datatypes.date, scope=tpRPS, documentation='Informe a Data de emiss\xe3o do RPS.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 813, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'StatusRPS'), tpStatusNFe, scope=tpRPS, documentation='Informe o Status do RPS.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 818, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TributacaoRPS'), tpTributacaoNFe, scope=tpRPS, documentation='Informe o tipo de tributa\xe7\xe3o do RPS.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 823, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorServicos'), tpValor, scope=tpRPS, documentation='Informe o valor dos servi\xe7os prestados.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 828, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorDeducoes'), tpValor, scope=tpRPS, documentation='Informe o valor das dedu\xe7\xf5es.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 833, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorPIS'), tpValor, scope=tpRPS, documentation='Informe o valor da reten\xe7\xe3o do PIS.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 838, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorCOFINS'), tpValor, scope=tpRPS, documentation='Informe o valor da reten\xe7\xe3o do COFINS.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 843, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorINSS'), tpValor, scope=tpRPS, documentation='Informe o valor da reten\xe7\xe3o do INSS.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 848, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorIR'), tpValor, scope=tpRPS, documentation='Informe o valor da reten\xe7\xe3o do IR.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 853, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorCSLL'), tpValor, scope=tpRPS, documentation='Informe o valor da reten\xe7\xe3o do CSLL.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 858, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodigoServico'), tpCodigoServico, scope=tpRPS, documentation='Informe o c\xf3digo do servi\xe7o do RPS. Este c\xf3digo deve pertencer \xe0 lista de servi\xe7os.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 863, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AliquotaServicos'), tpAliquota, scope=tpRPS, documentation='Informe o valor da al\xedquota. Obs. O conte\xfado deste campo ser\xe1 ignorado caso a tributa\xe7\xe3o ocorra no munic\xedpio (Situa\xe7\xe3o do RPS = T ).', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 868, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ISSRetido'), pyxb.binding.datatypes.boolean, scope=tpRPS, documentation='Informe a reten\xe7\xe3o.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 873, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJTomador'), tpCPFCNPJ, scope=tpRPS, documentation='Informe o CPF/CNPJ do tomador do servi\xe7o. O conte\xfado deste campo ser\xe1 ignorado caso o campo InscricaoMunicipalTomador esteja preenchido.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 878, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalTomador'), tpInscricaoMunicipal, scope=tpRPS, documentation='Informe a Inscri\xe7\xe3o Municipal do Tomador. ATEN\xc7\xc3O: Este campo s\xf3 dever\xe1 ser preenchido para tomadores estabelecidos no munic\xedpio de S\xe3o Paulo (CCM). Quando este campo for preenchido, seu conte\xfado ser\xe1 considerado como priorit\xe1rio com rela\xe7\xe3o ao campo de CPF/CNPJ do Tomador, sendo utilizado para identificar o Tomador e recuperar seus dados da base de dados da Prefeitura.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 883, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InscricaoEstadualTomador'), tpInscricaoEstadual, scope=tpRPS, documentation='Informe a inscri\xe7\xe3o estadual do tomador. Este campo ser\xe1 ignorado caso seja fornecido um CPF/CNPJ ou a Inscri\xe7\xe3o Municipal do tomador perten\xe7a ao munic\xedpio de S\xe3o Paulo.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 888, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RazaoSocialTomador'), tpRazaoSocial, scope=tpRPS, documentation='Informe o Nome/Raz\xe3o Social do tomador. Este campo \xe9 obrigat\xf3rio apenas para tomadores Pessoa Jur\xeddica (CNPJ). Este campo ser\xe1 ignorado caso seja fornecido um CPF/CNPJ ou a Inscri\xe7\xe3o Municipal do tomador perten\xe7a ao munic\xedpio de S\xe3o Paulo.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 893, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EnderecoTomador'), tpEndereco, scope=tpRPS, documentation='Informe o endere\xe7o do tomador. Os campos do endere\xe7o s\xe3o obrigat\xf3rios apenas para tomadores pessoa jur\xeddica (CNPJ informado). O conte\xfado destes campos ser\xe1 ignorado caso seja fornecido um CPF/CNPJ ou a Inscri\xe7\xe3o Municipal do tomador perten\xe7a ao munic\xedpio de S\xe3o Paulo.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 898, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EmailTomador'), tpEmail, scope=tpRPS, documentation='Informe o e-mail do tomador.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 903, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJIntermediario'), tpCPFCNPJ, scope=tpRPS, documentation='CNPJ do intermedi\xe1rio de servi\xe7o.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 908, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalIntermediario'), tpInscricaoMunicipal, scope=tpRPS, documentation='Inscri\xe7\xe3o Municipal do intermedi\xe1rio de servi\xe7o.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 913, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ISSRetidoIntermediario'), pyxb.binding.datatypes.string, scope=tpRPS, documentation='Reten\xe7\xe3o do ISS pelo intermedi\xe1rio de servi\xe7o.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 918, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EmailIntermediario'), tpEmail, scope=tpRPS, documentation='E-mail do intermedi\xe1rio de servi\xe7o.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 923, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Discriminacao'), tpDiscriminacao, scope=tpRPS, documentation='Informe a discrimina\xe7\xe3o dos servi\xe7os.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 928, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorCargaTributaria'), tpValor, scope=tpRPS, documentation='Valor da carga tribut\xe1ria total em R$.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 933, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PercentualCargaTributaria'), tpPercentualCargaTributaria, scope=tpRPS, documentation='Valor percentual da carga tribut\xe1ria.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 938, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'FonteCargaTributaria'), tpFonteCargaTributaria, scope=tpRPS, documentation='Fonte de informa\xe7\xe3o da carga tribut\xe1ria.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 943, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodigoCEI'), tpNumero, scope=tpRPS, documentation='C\xf3digo do CEI \u2013 Cadastro espec\xedfico do INSS.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 948, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MatriculaObra'), tpNumero, scope=tpRPS, documentation='C\xf3digo que representa a matr\xedcula da obra no sistema de cadastro de obras.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 953, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MunicipioPrestacao'), tpCidade, scope=tpRPS, documentation='C\xf3digo da cidade do munic\xedpio da presta\xe7\xe3o do servi\xe7o.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 958, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroEncapsulamento'), tpNumero, scope=tpRPS, documentation='C\xf3digo que representa o n\xfamero do encapsulamento da obra.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 963, 6)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorTotalRecebido'), tpValor, scope=tpRPS, documentation='Informe o valor total recebido.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 968, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 838, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 843, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 848, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 853, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 858, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 878, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 883, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 888, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 893, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 898, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 903, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 908, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 913, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 918, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 923, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 933, 6))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 938, 6))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 943, 6))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 948, 6))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 953, 6))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 958, 6))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 963, 6))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 968, 6))
    counters.add(cc_22)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'Assinatura')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 798, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'ChaveRPS')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 803, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'TipoRPS')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 808, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'DataEmissao')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 813, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'StatusRPS')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 818, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'TributacaoRPS')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 823, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorServicos')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 828, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorDeducoes')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 833, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorPIS')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 838, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorCOFINS')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 843, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorINSS')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 848, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorIR')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 853, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorCSLL')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 858, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'CodigoServico')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 863, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'AliquotaServicos')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 868, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'ISSRetido')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 873, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJTomador')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 878, 6))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalTomador')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 883, 6))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'InscricaoEstadualTomador')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 888, 6))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'RazaoSocialTomador')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 893, 6))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'EnderecoTomador')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 898, 6))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'EmailTomador')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 903, 6))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJIntermediario')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 908, 6))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalIntermediario')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 913, 6))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'ISSRetidoIntermediario')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 918, 6))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'EmailIntermediario')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 923, 6))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'Discriminacao')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 928, 6))
    st_26 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorCargaTributaria')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 933, 6))
    st_27 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'PercentualCargaTributaria')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 938, 6))
    st_28 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'FonteCargaTributaria')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 943, 6))
    st_29 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'CodigoCEI')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 948, 6))
    st_30 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'MatriculaObra')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 953, 6))
    st_31 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'MunicipioPrestacao')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 958, 6))
    st_32 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_32)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroEncapsulamento')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 963, 6))
    st_33 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_33)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_22, False))
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorTotalRecebido')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/TiposNFe_v01.xsd', 968, 6))
    st_34 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_34)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
         ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
         ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    transitions.append(fac.Transition(st_34, [
         ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_31._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_32._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_33._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_22, True) ]))
    st_34._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpRPS._Automaton = _BuildAutomaton_8()

