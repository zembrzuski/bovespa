import requests
from xml_extractors import formulario_cadastral_extractor
import helpers.zip_helper as zip_helper
from helpers import bovespa_unzipper
from helpers import filesystem_helper

bovespa_url_base = \
    'https://www.rad.cvm.gov.br/enetconsulta/frmDownloadDocumento.aspx?' \
    'CodigoInstituicao=2&NumeroSequencialDocumento={}'


def process_file(index):
    downloaded_file = requests.get(bovespa_url_base.format(index), verify=False).content

    try:
        root_zip_file = zip_helper.bytes_to_zipfile(downloaded_file)
    except:
        print('file index {} is not a zip file'.format(index))
        return

    if len(list(filter(lambda x: ('DFP' in x.filename) or ('ITR' in x.filename), root_zip_file.filelist))) == 0:
        print('file index {} is not dfp nor itr'.format(index))
        return

    all_files = bovespa_unzipper.unzip(downloaded_file)
    formulario_cadastral_info = formulario_cadastral_extractor.extract(all_files['formulario_cadastral'])

    filesystem_helper.persist_file(
        codigo_cvm=formulario_cadastral_info['codigo_cvm'],
        file_index=index,
        file_to_persist=downloaded_file)


def download():
    index = 9675

    while index > 0:
        print('trying {}'.format(index))
        process_file(index)
        print('finished {}'.format(index))
        index = index - 1
