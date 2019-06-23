import xmltodict


def extract_information(info_financeiras):
    the_dict = xmltodict.parse(info_financeiras.decode('utf-8'))

    return None
