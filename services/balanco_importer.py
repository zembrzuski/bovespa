from xml_extractors import formulario_cadastral_extractor
import helpers.bovespa_unzipper as bovespa_unzipper
import xml_extractors.info_financeiras_extractor as info_financeiras_extractor
from xml_extractors import composicao_capital_social_extractor
from helpers import filesystem_helper


def import_balanco(id_documento):
    downloaded_file = filesystem_helper.load_file(id_documento)
    all_files = bovespa_unzipper.unzip(downloaded_file)

    formulario_cadastral_info = formulario_cadastral_extractor.extract_information(all_files['formulario_cadastral'])
    info_financeiras = info_financeiras_extractor.extract_information(all_files['informacoes_financeiras'])
    composicao_capital = composicao_capital_social_extractor.extract_information(all_files['composicao_capital_social'])

    return True
