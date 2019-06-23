import requests
import zipfile
import io as io


def bytes_to_zipfile(the_bytes):
    zipdata = io.BytesIO()
    zipdata.write(the_bytes)
    return zipfile.ZipFile(zipdata)


def download_zip_file_from_bovespa():
    r = requests.get(
        'https://www.rad.cvm.gov.br/enetconsulta/frmDownloadDocumento.aspx?CodigoInstituicao=2&NumeroSequencialDocumento=81551',
        verify=False)

    myzipfile = bytes_to_zipfile(r.content)

    xmls = list(filter(lambda file: 'xml' in file.filename, myzipfile.filelist))
    innerzip = list(filter(lambda file: 'xml' not in file.filename, myzipfile.filelist))[0]

    innerzipfile = bytes_to_zipfile(myzipfile.open(innerzip.filename).read())

    all_files = {
        'root': xmls,
        'inner': innerzipfile
    }

    return all_files


def main():
    all_files = download_zip_file_from_bovespa()

    zipfile.ZipFile(zipdata)
    all_files['root'][0]
    print('ae')

if __name__ == '__main__':
    main()
