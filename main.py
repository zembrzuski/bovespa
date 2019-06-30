from services import downloader_batch
from services import balanco_importer


def main():
    # downloader_batch.download()
    balanco_importer.import_balanco(81551)  # dimed DFP
    # balanco_importer.import_balanco(60695)  # 60695 ITR petro
    # balanco_importer.import_balanco(63571)      # DFP petro
    # balanco_importer.import_balanco(69690)      # ITR dimed
    print('finished')


if __name__ == '__main__':
    main()
