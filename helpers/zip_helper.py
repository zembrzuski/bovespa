import zipfile
import io as io


def bytes_to_zipfile(the_bytes):
    zip_data = io.BytesIO()
    zip_data.write(the_bytes)

    return zipfile.ZipFile(zip_data)


def open_file_inside_zip_file(zip_file, filename_inside_zip_file):
    """
    Dado um zipfile (do modulo zipfile) e um string que corresponde ao nome do arquivo dentro do zipfile
    passado como parametro, abre o arquivo e retorna seus bytes.

    :param zip_file: arquivo zip da classe zipfile
    :param filename_inside_zip_file: nome do arquivo (string) dentro do zip_file passado como parametro
    :return: retorna os bytes do arquivo que ele quer abrir
    """
    register_form_item = list(filter(
        lambda file: filename_inside_zip_file == file.filename, zip_file.filelist))[0]

    return zip_file.open(register_form_item.filename).read()
