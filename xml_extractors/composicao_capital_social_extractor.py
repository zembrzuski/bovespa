import xmltodict


def __capital_social_converter(capital_social_dict):
    return {
        'capital_integralizado': {
            'on': int(capital_social_dict['QuantidadeAcaoOrdinariaCapitalIntegralizado']),
            'pn': int(capital_social_dict['QuantidadeAcaoPreferencialCapitalIntegralizado']),
            'total': int(capital_social_dict['QuantidadeTotalAcaoCapitalIntegralizado'])
        },
        'tesouraria': {
            'on': int(capital_social_dict['QuantidadeAcaoOrdinariaTesouraria']),
            'pn': int(capital_social_dict['QuantidadeAcaoPreferencialTesouraria']),
            'total': int(capital_social_dict['QuantidadeTotalAcaoTesouraria'])
        }
    }


def __capital_social_list_filter(composicao_capital_social_list):
    filtered = list(filter(
        lambda x: int(x['QuantidadeAcaoOrdinariaCapitalIntegralizado']) > 0, composicao_capital_social_list))

    if len(filtered) != 1:
        raise Exception('caso nao previsto ainda')

    return __capital_social_converter(filtered[0])


def extract(xml):
    the_dict = xmltodict.parse(xml.decode('utf-8'))

    array = the_dict['ArrayOfComposicaoCapitalSocialDemonstracaoFinanceira']

    # TODO remover essa porqueira de validaco medonha com o tempo
    if len(array) > 3:
        raise Exception('nao previ o caso em que existe mais de 1 elemento na composicao do capital social')

    capital_social = array['ComposicaoCapitalSocialDemonstracaoFinanceira']

    if isinstance(capital_social, list):
        return __capital_social_list_filter(capital_social)
    elif isinstance(capital_social, dict):
        return __capital_social_converter(capital_social)
    else:
        raise Exception('caso nao previsto ainda')

