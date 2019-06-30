import xmltodict


def extract_conta(an_account):
    return {
        'plano_conta': an_account['PlanoConta']['NumeroConta'],
        'descricao_conta': an_account['DescricaoConta1'],
        'valores_conta': [
            float(an_account['ValorConta1']),
            float(an_account['ValorConta2']),
            float(an_account['ValorConta3']),
            float(an_account['ValorConta4']),
            float(an_account['ValorConta5'])
        ]
    }


def extract(info_financeiras):
    the_dict = xmltodict.parse(info_financeiras.decode('utf-8'))
    info_finas_array = the_dict['ArrayOfInfoFinaDFin']['InfoFinaDFin']

    return list(map(lambda an_account: extract_conta(an_account), info_finas_array))
