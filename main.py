from services import downloader_batch
from services import balanco_importer


def main():
    # downloader_batch.download()
    # balanco_importer.import_balanco(81551) # dimed
    # balanco_importer.import_balanco(80929) # petrobras
    balanco_importer.import_balanco(80981)  # hering

    print('finished')


if __name__ == '__main__':
    main()
