#!/usr/bin/env python
# -*- coding: utf-8 -*- 
conta_definition = {
    'patrimonio_liquido': {
        'predicate': [
            {
                'regex': '^patr(\.)?(im[oô]nio)? l[ií]q(\.)?(uido)?$',
                'codigo_tipo_informacao_financeira': 1,
            }
        ],
        'tipo_conta': 'balanco'
    },
    'lucro_liquido': {
        'predicate': [
            # {
            #     'regex': '^lucro l.quido consolidado',
            #     'codigo_tipo_informacao_financeira': 2,
            # },
            {
                'regex': '^lucro.preju.zo do per.odo',
                'codigo_tipo_informacao_financeira': 1,
                'tipo_conta': 'demonstrativo'
            }
        ],
        'tipo_conta': 'demonstrativo'
    }
}
