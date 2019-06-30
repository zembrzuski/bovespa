from datetime import datetime


def parse(date_str):
    return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')


def extract_trimestre(date):
    if date.month == 3:
        return 1

    if date.month == 6:
        return 2

    if date.month == 9:
        return 3

    if date.month == 12:
        return 4

    raise Exception("trimestre invalido")
