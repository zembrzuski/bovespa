import os
from pathlib import Path

base_filesystem_path = '/home/zembrzuski/labs/rolling-snow-zips'


def find_filepath_by_id_documento(id_documento):
    zip_file_name = '{}.zip'.format(id_documento)

    for filename in Path(base_filesystem_path).glob('**/{}'.format(zip_file_name)):
        return filename

    raise Exception("File not found {}".format(id_documento))


def load_file(id_documento):
    file_path = find_filepath_by_id_documento(id_documento)

    with open(str(file_path), 'rb') as f:
        return f.read()


def persist_file(codigo_cvm, file_index, file_to_persist):
    directory = '{}/{}'.format(base_filesystem_path, codigo_cvm)

    os.makedirs(directory, exist_ok=True)

    with open('{}/{}.zip'.format(directory, file_index), 'wb') as f:
        f.write(file_to_persist)

    return True
