#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from services import downloader_batch
from services import balanco_importer


def main():
    downloader_batch.download()
    # downloader_batch.download_list(dimed_list)

    # balanco_importer.import_all_balancos_from_company('009342')

    # balanco_importer.import_balanco(45446)  # dimed itr_1
    # balanco_importer.import_balanco(77224)  # dimed itr_2
    # balanco_importer.import_balanco(79372)  # dimed itr_3
    # balanco_importer.import_balanco(81551)  # dimed dfp_4

    print('finished')


if __name__ == '__main__':
    main()
