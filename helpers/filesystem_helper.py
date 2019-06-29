import os


def load_file(id_documento):
    print('ae')


def persist_file(codigo_cvm, file_index, file_to_persist):
    directory = '{}/{}'.format('/home/zembrzuski/labs/rolling-snow-zips', codigo_cvm)

    os.makedirs(directory, exist_ok=True)

    with open('{}/{}.zip'.format(directory, file_index), 'wb') as f:
        f.write(file_to_persist)

    return None
