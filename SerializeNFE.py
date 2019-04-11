# -*- coding: utf-8 -*-
from NFE import NotaFiscal, Cliente, Emitente, CODIGO_BRASIL
from decimal import Decimal
from SignXML import PostXML
from Utils import Certificate, CertData
import datetime
import lxml


class Nfe(object):

    #Dados stark para emissao nota fiscal
    certificado = "/opt/pyNfe/PyNFe/tests/stark.pfx"
    senha = 'birdforever'
    uf = 'sp'
    homologacao = True
    modelo='nfe'
    cnpj= '20018183000180'
    razao_social = 'Stark Bank S.A'
    none_fanstasia = 'Stark Bank'
    inscricao_estadual = '118050288115'
    cnae_fiscal_emitente_stark = "8299799"

    codigo_de_regime_tributario = '1',  # 1 para simples nacional ou 3 para normal
    inscricao_estadual_emitente = '118050288115',  # numero de IE da empresa
    inscricao_municipal_emitente = '3550308',
    cnae_fiscal_emitente = '8299799',  # cnae apenas números
    endereco_logradouro_emitente = 'Rua dos Ingleses',
    endereco_numero_emitente = '586',
    endereco_bairro_emitente = 'Morro dos Ingleses',
    endereco_municipio_emitente = 'Sao Paulo',
    endereco_uf_emitente = 'SP',
    endereco_cep_emitente = '01329000',
    endereco_pais_emitente = CODIGO_BRASIL

    # emitente (stark bank sa)
    emitente = Emitente(
        razao_social='Stark Bank S.A',
        nome_fantasia='',
        cnpj=cnpj,           # cnpj apenas números
        codigo_de_regime_tributario='1',  # 1 para simples nacional ou 3 para normal
        inscricao_estadual="118050288115",  # numero de IE da empresa
        inscricao_municipal="3550308",
        cnae_fiscal="8299799",           # cnae apenas números
        endereco_logradouro="RUA DOS INGLESES",
        endereco_numero="586",
        endereco_bairro="Morro dos Ingleses",
        endereco_municipio="Sao Paulo",
        endereco_uf="SP",
        endereco_cep="01329000",
        endereco_pais=CODIGO_BRASIL
    )



    # cliente hummingbird:
    razao_social_cliente = 'HUMMINGBIRD HEALTH PRODUCTS',
    tipo_documento_cliente = 'CNPJ',  # CPF ou CNPJ
    email_cliente = 'DEROMIR.NEVES@HUMMINGBIRD.COM.BR',
    numero_documento_cliente = '30134945000167',  # numero do cpf ou cnpj
    indicador_ie_cliente = 1,  # 9=Não contribuinte, 1 = contribuinte ICMS
    endereco_logradouro_cliente = 'Rua dos Ingleses',
    endereco_numero_cliente = '586',
    endereco_complemento_cliente = 'Apto 63',
    endereco_bairro_cliente = 'Morro dos Ingleses',
    endereco_municipio_cliente = 'Sao Paulo',
    endereco_uf_cliente = 'SP',
    endereco_cep_cliente = '01329000',
    endereco_pais_cliente = CODIGO_BRASIL,
    endereco_telefone_cliente = '1163482485',

    # cliente
    cliente = Cliente(
        razao_social="HUMMINGBIRD HEALTH PRODUCTS",
        tipo_documento="CNPJ",           #CPF ou CNPJ
        email="DEROMIR.NEVES@HUMMINGBIRD.COM.BR",
        numero_documento="30134945000167",  # numero do cpf ou cnpj
        indicador_ie=1,  # 9=Não contribuinte, 1 = contribuinte ICMS
        endereco_logradouro="Rua dos Ingleses",
        endereco_numero="586",
        endereco_complemento="Apto 63",
        endereco_bairro="Morro dos Ingleses",
        endereco_municipio="Sao Paulo",
        endereco_uf="SP",
        endereco_cep="01329000",
        endereco_pais=CODIGO_BRASIL,
        endereco_telefone="1163482485",
    )

    # Nota Fiscal
    nota_fiscal = NotaFiscal(
       emitente=emitente,
       cliente=cliente,
       uf=uf.upper(),
       natureza_operacao='VENDA',  # venda, compra, transferência, devolução, etc
       forma_pagamento=0,         # 0=Pagamento à vista; 1=Pagamento a prazo; 2=Outros.
       tipo_pagamento=1,
       modelo=55,                 # 55=NF-e; 65=NFC-e
       serie='1',
       numero_nf='10101',           # Número do Documento Fiscal.
       data_emissao=datetime.datetime.now(),
       data_saida_entrada=datetime.datetime.now(),
       tipo_documento=1,          # 0=entrada; 1=saida
       municipio='3550308',       # Código IBGE do Município
       tipo_impressao_danfe=1,    # 0=Sem geração de DANFE;1=DANFE normal, Retrato;2=DANFE normal Paisagem;3=DANFE Simplificado;4=DANFE NFC-e;
       forma_emissao='1',         # 1=Emissão normal (não em contingência);
       cliente_final=1,           # 0=Normal;1=Consumidor final;
       indicador_destino=1,
       indicador_presencial=1,
       finalidade_emissao='1',    # 1=NF-e normal;2=NF-e complementar;3=NF-e de ajuste;4=Devolução de mercadoria.
       processo_emissao='0',      #0=Emissão de NF-e com aplicativo do contribuinte;
       transporte_modalidade_frete=1,
       informacoes_adicionais_interesse_fisco='Mensagem complementar',
       totais_tributos_aproximado=Decimal('2.06'),
    )

    # Produto
    nota_fiscal.adicionar_produto_servico(
        codigo='000328',                           # id do produto
        descricao='NOTA FISCAL EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL',
        ncm='985286910',  #ncm?
        #cest='0100100',  # NT2015/003
        cfop='5102',
        unidade_comercial='UN',
        ean='SEM GTIN',
        ean_tributavel='SEM GTIN',
        quantidade_comercial=Decimal('12'),        # 12 unidades
        valor_unitario_comercial=Decimal('9.75'),  # preço unitário
        valor_total_bruto=Decimal('2.00'),       # preço total
        unidade_tributavel='UN',
        quantidade_tributavel=Decimal('12'),
        valor_unitario_tributavel=Decimal('9.75'),
        ind_total=1,
        # numero_pedido='12345',                   # xPed
        # numero_item='123456',                    # nItemPed
        icms_modalidade='102',
        icms_origem=0,
        icms_csosn='400',
        pis_modalidade='07',
        cofins_modalidade='07',
        valor_tributos_aprox='21.06'
        )




