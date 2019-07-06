conta_definition = {
    'patrimonio_liquido': {
        'regexes': ['^patr(\.)?(im[oô]nio)? l[ií]q(\.)?(uido)?$'],
        'codigo_tipo_informacao_financeira': 1,
        'tipo_conta': 'balanco'
    },
    'lucro_liquido': {
        'regexes': [
            '^lucro l.quido consolidado',
            '^lucro.preju.zo do per.odo'
        ],
        'codigo_tipo_informacao_financeira': 2,
        'tipo_conta': 'demonstrativo'
    }
}
