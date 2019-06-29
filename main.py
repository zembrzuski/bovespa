from services import downloader_batch


def main():
    downloader_batch.download()
    print('finished')


if __name__ == '__main__':
    main()
