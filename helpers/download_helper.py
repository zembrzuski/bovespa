import requests


def download_zip_file_from_bovespa(url_to_download):
    return requests.get(url_to_download, verify=False).content
