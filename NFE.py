# -*- coding: utf-8 -*-
from decimal import Decimal

CODIGO_BRASIL = '1058'

class FonteDados(object):

    _objetos = None

    def __init__(self, objetos=None):
        if objetos:
            self._objetos = objetos
        else:
            self._objetos = []

    def carregar_objetos(self, **kwargs):

        def filtrar(obj):
            ret = True

            for k, v in kwargs.items():
                ret = (k == '_classe' and isinstance(obj, v)) or \
                      (k != '_classe' and getattr(obj, k, None) == v)

                if not ret:
                    break

            return ret

        # Filtra a lista de objetos
        lista = filter(filtrar, self._objetos)

        return lista

_fonte_dados = FonteDados()


class Entidade(object):

    _fonte_dados = None

    def __init__(self, **kwargs):
        # Codigo para dinamizar a criacao de instancias de entidade,
        # aplicando os valores dos atributos na instanciacao
        for k, v in kwargs.items():
            setattr(self, k, v)

        # Adiciona o objeto à fonte de dados informada
        if not self._fonte_dados:
            import _fonte_dados
            self._fonte_dados = _fonte_dados

        self._fonte_dados.adicionar_objeto(self)

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, str(self))

    def adicionar_objeto(self, _objeto):
        u"""Metodo responsável por adicionar o(s) objeto(s) informado(s) ao
        repositorio de objetos da fonte de dados."""

        obj = FonteDados()
        # Adiciona _objeto como objeto
        if isinstance(_objeto, Entidade):
            obj._objetos.append(_objeto)

        # Adiciona _objeto como lista
        elif isinstance(_objeto, (list, tuple)):
            obj._objetos += _objeto

        else:
            raise Exception('Objeto informado e invalido!')


class NotaFiscal(Entidade):

    NF_STATUS = (
        'Em Digitacao',
        'Validada',
        'Assinada',
        'Em processamento',
        'Autorizada',
        'Rejeitada',
        'Cancelada',
    )
    status = NF_STATUS[0]

    # Código numérico aleatório que compõe a chave de acesso
    codigo_numerico_aleatorio = str()

    # Digito verificador do codigo numerico aleatorio
    dv_codigo_numerico_aleatorio = str()

    # Nota Fisca eletronica
    # - Modelo (formato: NN)
    modelo = int()

    # - Serie (obrigatorio - formato: NNN)
    serie = str()

    # - Numero NF (obrigatorio)
    numero_nf = str()

    # - Data da Emissao (obrigatorio)
    data_emissao = None

    # - Natureza da Operacao (obrigatorio)
    natureza_operacao = str()

    # - Tipo do Documento (obrigatorio - seleciona de lista) - NF_TIPOS_DOCUMENTO
    tipo_documento = int()

    # - Processo de emissão da NF-e (obrigatorio - seleciona de lista) - NF_PROCESSOS_EMISSAO
    processo_emissao = 0

    # - Versao do processo de emissão da NF-e
    versao_processo_emissao = '0.4'

    # - Tipo impressao DANFE (obrigatorio - seleciona de lista) - NF_TIPOS_IMPRESSAO_DANFE
    tipo_impressao_danfe = int()

    # - Data de saida/entrada
    data_saida_entrada = None

    # - Forma de pagamento  (obrigatorio - seleciona de lista) - NF_FORMAS_PAGAMENTO
    # Removido na NF-e 4.00
    # forma_pagamento = int()

    # - Tipo de pagamento
    """ 
    Obrigatório o preenchimento do Grupo Informações de Pagamento para NF-e e NFC-e. 
    Para as notas com finalidade de Ajuste ou Devolução o campo Forma de Pagamento deve ser preenchido com 90=Sem Pagamento.
    01=Dinheiro
    02=Cheque
    03=Cartão de Crédito
    04=Cartão de Débito
    05=Crédito Loja
    10=Vale Alimentação
    11=Vale Refeição
    12=Vale Presente
    13=Vale Combustível
    14=Duplicata Mercantil
    90= Sem pagamento
    99=Outros
    """
    tipo_pagamento = int()

    # - Forma de emissao (obrigatorio - seleciona de lista) - NF_FORMAS_EMISSAO
    forma_emissao = str()

    # - Finalidade de emissao (obrigatorio - seleciona de lista) - NF_FINALIDADES_EMISSAO
    finalidade_emissao = int()

    # - Indica se a nota e para consumidor final
    cliente_final = int()

    # - Indica se a compra foi feita presencialmente, telefone, internet, etc
    """
        0=Não se aplica (por exemplo, Nota Fiscal complementar ou deajuste);
        1=Operação presencial;
        2=Operação não presencial, pela Internet;
        3=Operação não presencial, Teleatendimento;
        4=NFC-e em operação com entrega a domicílio;
        5=Operação presencial, fora do estabelecimento;
        9=Operação não presencial, outros.
    """
    indicador_presencial = int()

    """ nfce suporta apenas operação interna
        Identificador de local de destino da operação 1=Operação interna;2=Operação interestadual;3=Operação com exterior.
    """
    indicador_destino = int()
    # - UF - converter para codigos em CODIGOS_ESTADOS
    uf = str()

    # - Municipio de ocorrencia
    municipio = str()

    # - Digest value da NF-e (somente leitura)
    digest_value = None

    # - Valor total da nota (somente leitura)
    valor_total_nota = Decimal()

    # - Valor ICMS da nota (somente leitura)
    valor_icms_nota = Decimal()

    # - Valor ICMS ST da nota (somente leitura)
    valor_icms_st_nota = Decimal()

    # - Protocolo (somente leitura)
    protocolo = str()

    # - Data (somente leitura)
    data = None

    # - Notas Fiscais Referenciadas (lista 1 para * / ManyToManyField)
    notas_fiscais_referenciadas = None

    # - Emitente (CNPJ ???)
    emitente = None

    # - Destinatario/Remetente
    #  - Identificacao (seleciona de Clientes)
    destinatario_remetente = None

    # - Entrega (XXX sera possivel ter entrega e retirada ao mesmo tempo na NF?)
    entrega = None

    # - Retirada
    retirada = None

    # - Local Retirada/Entrega
    #  - Local de retirada diferente do emitente (Sim/Nao)
    local_retirada_diferente_emitente = False

    #  - Local de entrega diferente do destinatario (Sim/Nao)
    local_entrega_diferente_destinatario = False

    # - Produtos e Servicos (lista 1 para * / ManyToManyField)
    produtos_e_servicos = None

    # Totais
    # - ICMS
    #  - Base de calculo (somente leitura)
    totais_icms_base_calculo = Decimal()

    #  - Total do ICMS (somente leitura)
    totais_icms_total = Decimal()

    #  - Total do ICMS Desonerado (somente leitura)
    totais_icms_desonerado = Decimal()

    #  - Base de calculo do ICMS ST (somente leitura)
    totais_icms_st_base_calculo = Decimal()

    #  - Total do ICMS ST (somente leitura)
    totais_icms_st_total = Decimal()

    #  - Total dos produtos e servicos (somente leitura)
    totais_icms_total_produtos_e_servicos = Decimal()

    #  - Total do frete (somente leitura)
    totais_icms_total_frete = Decimal()

    #  - Total do seguro (somente leitura)
    totais_icms_total_seguro = Decimal()

    #  - Total do desconto (somente leitura)
    totais_icms_total_desconto = Decimal()

    #  - Total do II (somente leitura)
    totais_icms_total_ii = Decimal()

    #  - Total do IPI (somente leitura)
    totais_icms_total_ipi = Decimal()

    #  - Valor Total do IPI devolvido 
    # Deve ser informado quando preenchido o Grupo Tributos Devolvidos na emissão de nota finNFe=4 (devolução) nas operações com não contribuintes do IPI. 
    # Corresponde ao total da soma dos campos id:UA04.
    totais_icms_total_ipi_dev = Decimal()

    #  - PIS (somente leitura)
    totais_icms_pis = Decimal()

    #  - COFINS (somente leitura)
    totais_icms_cofins = Decimal()

    #  - Outras despesas acessorias
    totais_icms_outras_despesas_acessorias = Decimal()

    #  - Total da nota
    totais_icms_total_nota = Decimal()

    # - ISSQN
    #  - Base de calculo do ISS
    totais_issqn_base_calculo_iss = Decimal()

    #  - Total do ISS
    totais_issqn_total_iss = Decimal()

    #  - PIS sobre servicos
    totais_issqn_pis = Decimal()

    #  - COFINS sobre servicos
    totais_issqn_cofins = Decimal()

    #  - Total dos servicos sob nao-incidencia ou nao tributados pelo ICMS
    totais_issqn_total = Decimal()

    # - Retencao de Tributos
    #  - Valor retido de PIS
    totais_retencao_valor_retido_pis = Decimal()

    #  - Valor retido de COFINS
    totais_retencao_valor_retido_cofins = Decimal()

    #  - Valor retido de CSLL
    totais_retencao_valor_retido_csll = Decimal()

    #  - Base de calculo do IRRF
    totais_retencao_base_calculo_irrf = Decimal()

    #  - Valor retido do IRRF
    totais_retencao_valor_retido_irrf = Decimal()

    #  - BC da ret. da Prev. Social
    totais_retencao_bc_retencao_previdencia_social = Decimal()

    #  - Retencao da Prev. Social
    totais_retencao_retencao_previdencia_social = Decimal()

    #  - Valor aproximado total de tributos federais, estaduais e municipais.
    totais_tributos_aproximado = Decimal()

    # - Valor Total do FCP (Fundo de Combate à Pobreza)
    totais_fcp = Decimal()

    # - Valor total do ICMS relativo Fundo de Combate à Pobreza (FCP) da UF de destino 
    totais_fcp_destino = Decimal()

     # - Valor Total do FCP (Fundo de Combate à Pobreza) retido por substituição tributária
    totais_fcp_st = Decimal()

     # - Valor Total do FCP retido anteriormente por Substituição Tributária
    totais_fcp_st_ret = Decimal()

    # - Valor total do ICMS Interestadual para a UF de destino 
    totais_icms_inter_destino = Decimal()

    # - Valor total do ICMS Interestadual para a UF do remetente
    totais_icms_inter_remetente = Decimal()

    # Transporte
    # - Modalidade do Frete (obrigatorio - seleciona de lista) - MODALIDADES_FRETE
    # 0=Contratação do Frete por conta do Remetente (CIF);
    # 1=Contratação do Frete por conta do Destinatário (FOB);
    # 2=Contratação do Frete por conta de Terceiros;
    # 3=Transporte Próprio por conta do Remetente;
    # 4=Transporte Próprio por conta do Destinatário;
    # 9=Sem Ocorrência de Transporte.
    transporte_modalidade_frete = int()

    # - Transportador (seleciona de Transportadoras)
    transporte_transportadora = None

    # - Retencao do ICMS
    #  - Base de calculo
    transporte_retencao_icms_base_calculo = Decimal()

    #  - Aliquota
    transporte_retencao_icms_aliquota = Decimal()

    #  - Valor do servico
    transporte_retencao_icms_valor_servico = Decimal()

    #  - UF
    transporte_retencao_icms_uf = str()

    #  - Municipio
    transporte_retencao_icms_municipio = Decimal()

    #  - CFOP
    transporte_retencao_icms_cfop = str()

    #  - ICMS retido
    transporte_retencao_icms_retido = Decimal()

    # - Veiculo
    #  - Placa
    transporte_veiculo_placa = str()

    #  - RNTC
    transporte_veiculo_rntc = str()

    #  - UF
    transporte_veiculo_uf = str()

    # - Reboque
    #  - Placa
    transporte_reboque_placa = str()

    #  - RNTC
    transporte_reboque_rntc = str()

    #  - UF
    transporte_reboque_uf = str()

    # - Volumes (lista 1 para * / ManyToManyField)
    transporte_volumes = None

    # Cobranca
    # - Fatura
    #  - Numero
    fatura_numero = str()

    #  - Valor original
    fatura_valor_original = Decimal()

    #  - Valor do desconto
    fatura_valor_desconto = Decimal()

    #  - Valor liquido
    fatura_valor_liquido = Decimal()

    # - Duplicatas (lista 1 para * / ManyToManyField)
    duplicatas = None

    # Informacoes Adicionais
    # - Informacoes Adicionais
    #  - Informacoes adicionais de interesse do fisco
    informacoes_adicionais_interesse_fisco = str()

    #  - Informacoes complementares de interesse do contribuinte
    informacoes_complementares_interesse_contribuinte = str()

    # - Observacoes do Contribuinte (lista 1 para * / ManyToManyField)
    observacoes_contribuinte = None

    # - Processo Referenciado (lista 1 para * / ManyToManyField)
    processos_referenciados = None

    def __init__(self, *args, **kwargs):
        self.notas_fiscais_referenciadas = []
        self.produtos_e_servicos = []
        self.transporte_volumes = []
        self.duplicatas = []
        self.observacoes_contribuinte = []
        self.processos_referenciados = []

        super(NotaFiscal, self).__init__(*args, **kwargs)

    def __str__(self):
        return ' '.join([str(self.modelo), self.serie, self.numero_nf])

    def adicionar_nota_fiscal_referenciada(self, **kwargs):
        u"""Adiciona uma instancia de Nota Fisca referenciada"""
        obj = NotaFiscalReferenciada(**kwargs)
        self.notas_fiscais_referenciadas.append(obj)
        return obj

class NotaFiscalReferenciada(Entidade):
    # - Tipo (seleciona de lista) - NF_REFERENCIADA_TIPOS
    tipo = str()

    #  - Nota Fiscal eletronica
    #   - Chave de Acesso
    chave_acesso = str()

    #  - Nota Fiscal
    #   - UF
    uf = str()

    #   - Mes e ano de emissao
    mes_ano_emissao = str()

    #   - CNPJ
    cnpj = str()

    #   - Serie (XXX)
    serie = str()

    #   - Numero
    numero = str()

    #   - Modelo
    modelo = str()


class Cliente(Entidade):
    # Dados do Cliente
    # - Nome/Razão Social (obrigatorio)
    razao_social = str()

    # - Email
    email = str()

    # - Tipo de Documento (obrigatorio) - default CNPJ - TIPOS_DOCUMENTO
    tipo_documento = 'CNPJ'

    # - Numero do Documento (obrigatorio)
    numero_documento = str()

    # - Indicador da IE do destinatário: 1 – Contribuinte ICMSpagamento à vista; 2 – Contribuinte isento de inscrição; 9 – Não Contribuinte
    indicador_ie = int()

    # - Inscricao Estadual
    inscricao_estadual = str()

    # - Inscricao Municial
    inscricao_municipal = str()

    # - Inscricao SUFRAMA
    inscricao_suframa = str()

    # - Isento do ICMS (Sim/Nao)
    isento_icms = False

    # Endereco
    # - Logradouro (obrigatorio)
    endereco_logradouro = str()

    # - Numero (obrigatorio)
    endereco_numero = str()

    # - Complemento
    endereco_complemento = str()

    # - Bairro (obrigatorio)
    endereco_bairro = str()

    # - CEP
    endereco_cep = str()

    # - Pais (seleciona de lista)
    endereco_pais = CODIGO_BRASIL

    # - UF (obrigatorio)
    endereco_uf = str()

    # - Municipio (obrigatorio)
    endereco_municipio = str()

    # - Código do Município (opt)
    endereco_cod_municipio = str()

    # - Telefone
    endereco_telefone = str()

    def __str__(self):
        return ' '.join([self.tipo_documento, self.numero_documento])


class Emitente(Entidade):
    # Dados do Emitente
    # - Nome/Razao Social (obrigatorio)
    razao_social = str()

    # - Nome Fantasia
    nome_fantasia = str()

    # - CNPJ (obrigatorio)
    cnpj = str()

    # - Inscricao Estadual (obrigatorio)
    inscricao_estadual = str()

    # - CNAE Fiscal
    cnae_fiscal = str()

    # - Inscricao Municipal
    inscricao_municipal = str()

    # - Inscricao Estadual (Subst. Tributario)
    inscricao_estadual_subst_tributaria = str()

    # - Codigo de Regime Tributario (obrigatorio)
    codigo_de_regime_tributario = str()

    # Endereco
    # - Logradouro (obrigatorio)
    endereco_logradouro = str()

    # - Numero (obrigatorio)
    endereco_numero = str()

    # - Complemento
    endereco_complemento = str()

    # - Bairro (obrigatorio)
    endereco_bairro = str()

    # - CEP
    endereco_cep = str()

    # - Pais (aceita somente Brasil)
    endereco_pais = CODIGO_BRASIL

    # - UF (obrigatorio)
    endereco_uf = str()

    # - Municipio (obrigatorio)
    endereco_municipio = str()

    # - Codigo Municipio (opt)
    endereco_cod_municipio = str()

    # - Telefone
    endereco_telefone = str()

    # Logotipo
    logotipo = None

    def __str__(self):
        return self.cnpj
