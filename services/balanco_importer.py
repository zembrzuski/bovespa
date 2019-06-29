import helpers.bovespa_unzipper as bovespa_unzipper
from helpers import filesystem_helper
from xml_extractors import balanco_xml_extractor


def import_balanco(id_documento):
    downloaded_file = filesystem_helper.load_file(id_documento)
    all_files = bovespa_unzipper.unzip(downloaded_file)

    balanco = balanco_xml_extractor.extract_balanco(all_files)

    return True
