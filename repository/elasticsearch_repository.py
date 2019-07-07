from config.local import config
import requests
import copy


def serialize_date(date):
    return date.strftime('%Y-%m-%dT%H:%M:%SZ')


def date_to_trimestre(date):
    return int(date.month / 3)


def serialize_valores(values):
    serialized_values = list()

    for key, value in values.items():
        serialized_values.append({
            'trimester': date_to_trimestre(key),
            'year': int(key.year),
            'value': value
        })

    return serialized_values


def serialize_plano_contas(plano_contas):
    serialized_plano_contas = dict()

    for key, values in plano_contas.items():
        serialized_plano_contas[key] = serialize_valores(values)

    return serialized_plano_contas


def serialize_balanco(balanco):
    balanco_to_serialize = copy.deepcopy(balanco)

    balanco_to_serialize['data_entrega_documento'] = serialize_date(balanco_to_serialize['data_entrega_documento'])
    balanco_to_serialize['plano_contas'] = serialize_plano_contas(balanco['plano_contas'])

    return balanco_to_serialize


def index_balanco(balanco):
    url_to_post = '{}/teste/teste/{}'.format(config['elasticsearch'], balanco['numero_documento_original'])
    serialized = serialize_balanco(balanco)

    code = requests.post(url_to_post, json=serialized).status_code
    print('indexou {}'.format(balanco))
    return code
