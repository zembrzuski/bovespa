import helpers.bovespa_unzipper as bovespa_unzipper
from helpers import filesystem_helper
from services.xml_extractors import balanco_xml_extractor
from services.domain_converter import raw_to_bonito_converter


def import_balanco(id_documento):
    downloaded_file = filesystem_helper.load_file(id_documento)
    all_files = bovespa_unzipper.unzip(downloaded_file)

    balanco_raw = balanco_xml_extractor.extract_balanco(all_files)
    balanco_bonito = raw_to_bonito_converter.convert(balanco_raw, id_documento)

    return True
