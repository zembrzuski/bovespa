from services.xml_extractors import formulario_cadastral_extractor
from services.xml_extractors import composicao_capital_social_extractor
from services.xml_extractors import info_financeiras_extractor


def extract_balanco(all_files):
    return {
        'document_type': all_files['document_type'],
        'formulario_cadastral': formulario_cadastral_extractor.extract(all_files['formulario_cadastral']),
        'informacoes_financeiras': info_financeiras_extractor.extract(all_files['informacoes_financeiras']),
        'composicao_capital_social': composicao_capital_social_extractor.extract(all_files['composicao_capital_social'])
    }
