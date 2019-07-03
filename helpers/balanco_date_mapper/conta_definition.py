conta_definition = {
    'patrimonio_liquido': {
        'regex': '^patr(\.)?(im[oô]nio)? l[ií]q(\.)?(uido)?$',
        'codigo_tipo_informacao_financeira': 1,
        'tipo_conta': 'balanco'
    },
    'lucro_liquido': {
        'regex': '^lucro l.quido consolidado',
        'codigo_tipo_informacao_financeira': 2,
        'tipo_conta': 'demonstrativo'
    }
}
