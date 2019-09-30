import os
from pathlib import Path
from config.local import config


def __find_filepath_by_id_documento(id_documento):
    zip_file_name = '{}.zip'.format(id_documento)

    for filename in Path(config['base_filesystem_path']).glob('**/{}'.format(zip_file_name)):
        return filename

    raise Exception("File not found {}".format(id_documento))


def load_file(id_documento):
    file_path = __find_filepath_by_id_documento(id_documento)

    with open(str(file_path), 'rb') as f:
        return f.read()


def persist_file(codigo_cvm, file_index, file_to_persist):
    directory = '{}/{}'.format(config['base_filesystem_path'], codigo_cvm)

    os.makedirs(directory)

    with open('{}/{}.zip'.format(directory, file_index), 'wb') as f:
        f.write(file_to_persist)

    return True


def find_all_balancos_from_company(cvm_code):
    directory = '{}/{}'.format(config['base_filesystem_path'], cvm_code)

    filtered = list(filter(lambda x: 'zip' in x, os.listdir(directory)))
    ids_demonstrativos = list(map(lambda x: int(x.replace('.zip', '')), filtered))

    return sorted(ids_demonstrativos)
