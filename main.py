from services import downloader_batch
from services import balanco_importer


def main():
    # downloader_batch.download()
    balanco_importer.import_balanco(81551)  # dimed DFP

    # balanco_importer.import_balanco(69690)      # ITR dimed mes 09
    # balanco_importer.import_balanco(68182)      # ITR dimed mes 06
    # balanco_importer.import_balanco(65643)      # ITR dimed mes 03

    print('finished')


if __name__ == '__main__':
    main()
