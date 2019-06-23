import zipfile
import io as io


def bytes_to_zipfile(the_bytes):
    zip_data = io.BytesIO()
    zip_data.write(the_bytes)

    return zipfile.ZipFile(zip_data)
