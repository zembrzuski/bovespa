#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import xmltodict
import helpers.date_helper as date_helper


def extract(formulario_cadastral, formuladrio_demonstracao_financeira, doc_id):
    cadastral_dict = xmltodict.parse(formulario_cadastral.decode('utf-8'))
    demonstracao_financeira_dict = xmltodict.parse(formuladrio_demonstracao_financeira.decode('utf-8'))

    validation_for_possible_mistake(demonstracao_financeira_dict, doc_id)

    referencia = date_helper.parse(demonstracao_financeira_dict['Documento']['DataReferenciaDocumento'].strip())
    entrega = date_helper.parse(cadastral_dict['Documento']['DataEntrega'].strip())

    return {
        'codigo_cvm': cadastral_dict['Documento']['CompanhiaAberta']['CodigoCvm'].strip().replace('-', ''),
        'razao_social': cadastral_dict['Documento']['CompanhiaAberta']['NomeRazaoSocialCompanhiaAberta'].strip(),
        'data_entrega': entrega,
        'data_documento': {
            'data_referencia_documento': referencia,
            'trimestre': date_helper.extract_trimestre(referencia),
            'ano': referencia.year
        }
    }


def validation_for_possible_mistake(demonstracao_financeira_dict, doc_id):
    """
    Leia a excecao e entenderá a razao desse metodo estranho.
    """

    # documentos que está com bug no CodigoEscalaMoeda
    if doc_id in [8075]:
        return

    if demonstracao_financeira_dict['Documento']['CodigoEscalaMoeda'] != '2':
        raise Exception('se essa excecao for lancada, eu imagino que seja pelo fato de os '
                        'valores das contas nao estao em \'mil\' reais. se isso acontecer, '
                        'eu devo pegar o balanco da empresa e verificar no site da bovespa e,'
                        'se essa minha hipotese for verdadeira, entao vou ter que fazer uma logica'
                        'para deixar bem direitinho esses valores. Se o valor for 1, então o '
                        'balanço não está em \'mil reais\' e sim em \'reais\'. Entretanto, até hoje,'
                        'o único caso que vi assim era um erro no demonstrativo, e não um valor real')
