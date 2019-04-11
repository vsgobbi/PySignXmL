# ./PedidoConsultaCNPJ.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:46d474fd6bbf6b525b44c76779cf0ba398ea8ab1
# Generated 2019-04-09 20:57:02.313001 by PyXB version 1.2.6 using Python 2.7.16.final.0
# Namespace http://www.prefeitura.sp.gov.br/nfe

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
import _ds as _ImportedBinding__ds
import _tipos as _ImportedBinding__tipos

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.prefeitura.sp.gov.br/nfe', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ds = _ImportedBinding__ds.Namespace
_Namespace_ds.configureCategories(['typeBinding', 'elementBinding'])

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


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Schema utilizado para PEDIDO de consultas de CNPJ.Este Schema XML é utilizado pelos tomadores e/ou prestadores de serviços consultarem quais Inscrições Municipais (CCM) estão vinculadas a um determinado CNPJ e se estes CCM emitem NFS-e ou não."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/PedidoConsultaCNPJ_v01.xsd', 13, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Cabecalho uses Python identifier Cabecalho
    __Cabecalho = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Cabecalho'), 'Cabecalho', '__httpwww_prefeitura_sp_gov_brnfe_CTD_ANON_Cabecalho', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/PedidoConsultaCNPJ_v01.xsd', 15, 8), )

    
    Cabecalho = property(__Cabecalho.value, __Cabecalho.set, None, 'Cabe\xe7alho do pedido.')

    
    # Element CNPJContribuinte uses Python identifier CNPJContribuinte
    __CNPJContribuinte = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CNPJContribuinte'), 'CNPJContribuinte', '__httpwww_prefeitura_sp_gov_brnfe_CTD_ANON_CNPJContribuinte', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/PedidoConsultaCNPJ_v01.xsd', 34, 8), )

    
    CNPJContribuinte = property(__CNPJContribuinte.value, __CNPJContribuinte.set, None, 'Informe o CNPJ do Contribuinte que se deseja consultar.')

    
    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature'), 'Signature', '__httpwww_prefeitura_sp_gov_brnfe_CTD_ANON_httpwww_w3_org200009xmldsigSignature', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/xmldsig-core-schema_v01.xsd', 8, 2), )

    
    Signature = property(__Signature.value, __Signature.set, None, None)

    _ElementMap.update({
        __Cabecalho.name() : __Cabecalho,
        __CNPJContribuinte.name() : __CNPJContribuinte,
        __Signature.name() : __Signature
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Cabeçalho do pedido."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/PedidoConsultaCNPJ_v01.xsd', 19, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element CPFCNPJRemetente uses Python identifier CPFCNPJRemetente
    __CPFCNPJRemetente = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), 'CPFCNPJRemetente', '__httpwww_prefeitura_sp_gov_brnfe_CTD_ANON__CPFCNPJRemetente', False, pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/PedidoConsultaCNPJ_v01.xsd', 21, 14), )

    
    CPFCNPJRemetente = property(__CPFCNPJRemetente.value, __CPFCNPJRemetente.set, None, 'Informe o CPF/CNPJ do Remetente autorizado a transmitir a mensagem XML.')

    
    # Attribute Versao uses Python identifier Versao
    __Versao = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Versao'), 'Versao', '__httpwww_prefeitura_sp_gov_brnfe_CTD_ANON__Versao', _ImportedBinding__tipos.tpVersao, fixed=True, unicode_default='1', required=True)
    __Versao._DeclarationLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/PedidoConsultaCNPJ_v01.xsd', 27, 12)
    __Versao._UseLocation = pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/PedidoConsultaCNPJ_v01.xsd', 27, 12)
    
    Versao = property(__Versao.value, __Versao.set, None, 'Informe a Vers\xe3o do Schema XML utilizado.')

    _ElementMap.update({
        __CPFCNPJRemetente.name() : __CPFCNPJRemetente
    })
    _AttributeMap.update({
        __Versao.name() : __Versao
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


PedidoConsultaCNPJ = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PedidoConsultaCNPJ'), CTD_ANON, documentation='Schema utilizado para PEDIDO de consultas de CNPJ.Este Schema XML \xe9 utilizado pelos tomadores e/ou prestadores de servi\xe7os consultarem quais Inscri\xe7\xf5es Municipais (CCM) est\xe3o vinculadas a um determinado CNPJ e se estes CCM emitem NFS-e ou n\xe3o.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/PedidoConsultaCNPJ_v01.xsd', 8, 2))
Namespace.addCategoryObject('elementBinding', PedidoConsultaCNPJ.name().localName(), PedidoConsultaCNPJ)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Cabecalho'), CTD_ANON_, scope=CTD_ANON, documentation='Cabe\xe7alho do pedido.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/PedidoConsultaCNPJ_v01.xsd', 15, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CNPJContribuinte'), _ImportedBinding__tipos.tpCPFCNPJ, scope=CTD_ANON, documentation='Informe o CNPJ do Contribuinte que se deseja consultar.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/PedidoConsultaCNPJ_v01.xsd', 34, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature'), _ImportedBinding__ds.SignatureType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/xmldsig-core-schema_v01.xsd', 8, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'Cabecalho')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/PedidoConsultaCNPJ_v01.xsd', 15, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'CNPJContribuinte')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/PedidoConsultaCNPJ_v01.xsd', 34, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/PedidoConsultaCNPJ_v01.xsd', 39, 8))
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
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), _ImportedBinding__tipos.tpCPFCNPJ, scope=CTD_ANON_, documentation='Informe o CPF/CNPJ do Remetente autorizado a transmitir a mensagem XML.', location=pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/PedidoConsultaCNPJ_v01.xsd', 21, 14)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente')), pyxb.utils.utility.Location('/Users/vitorgabriel/Desktop/pySignXML/PySignXmL/schemasv02/PedidoConsultaCNPJ_v01.xsd', 21, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()

