import zipfile
import io as io


def bytes_to_zipfile(the_bytes):
    zip_data = io.BytesIO()
    zip_data.write(the_bytes)

    return zipfile.ZipFile(zip_data)


def open_zip_file(zip_file, file_inside_zipfile_to_be_read):
    return zip_file.open(file_inside_zipfile_to_be_read.filename).read()
