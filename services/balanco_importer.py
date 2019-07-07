import helpers.bovespa_unzipper as bovespa_unzipper
from helpers import filesystem_helper
from services.xml_extractors import balanco_xml_extractor
from services.domain_converter import raw_to_bonito_converter
from repository import elasticsearch_repository
from helpers import filesystem_helper


def import_balanco(id_documento):
    downloaded_file = filesystem_helper.load_file(id_documento)
    all_files = bovespa_unzipper.unzip(downloaded_file)

    balanco_raw = balanco_xml_extractor.extract_balanco(all_files, id_documento)
    balanco_bonito = raw_to_bonito_converter.convert(balanco_raw, id_documento)

    return elasticsearch_repository.index_balanco(balanco_bonito)


def import_all_balancos_from_company(cvm_code):
    balancos = filesystem_helper.find_all_balancos_from_company(cvm_code)

    for b in balancos:
        # print('trying to import {}'.format(b))
        resp = import_balanco(b)
        # print('finished to import {} --> '.format(b, resp))

    return 'ok'
