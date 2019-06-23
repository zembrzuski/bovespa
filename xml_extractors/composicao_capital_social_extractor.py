import xmltodict


def extract_information(xml):
    the_dict = xmltodict.parse(xml.decode('utf-8'))

    array = the_dict['ArrayOfComposicaoCapitalSocialDemonstracaoFinanceira']

    # TODO remover essa porqueira de validaco medonha com o tempo
    if len(array) > 3:
        raise Exception('nao previ o caso em que existe mais de 1 elemento na composicao do capital social')

    capital_social = array['ComposicaoCapitalSocialDemonstracaoFinanceira']

    return {
        'capital_integralizado': {
            'on': int(capital_social['QuantidadeAcaoOrdinariaCapitalIntegralizado']),
            'pn': int(capital_social['QuantidadeAcaoPreferencialCapitalIntegralizado']),
            'total': int(capital_social['QuantidadeTotalAcaoCapitalIntegralizado'])
        },
        'tesouraria': {
            'on': int(capital_social['QuantidadeAcaoOrdinariaTesouraria']),
            'pn': int(capital_social['QuantidadeAcaoPreferencialTesouraria']),
            'total': int(capital_social['QuantidadeTotalAcaoTesouraria'])
        }
    }
