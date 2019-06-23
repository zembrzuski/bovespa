from datetime import datetime


def parse(date_str):
    return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
