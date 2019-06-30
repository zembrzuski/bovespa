import re

regexes = {
    'patrimonio_liquido': '^patr(\.)?(im[oô]nio)? l[ií]q(\.)?(uido)?$'
}


def evaluate_indicador(indicador, txt):
    return re.search(regexes[indicador], txt, re.IGNORECASE)
