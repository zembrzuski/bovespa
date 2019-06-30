from helpers import balanco_date_index_mapper
from helpers import date_helper
import unittest


class BalancoDateIndexTest(unittest.TestCase):

    def test_dfp_with_two_years(self):
        dfp = {
            'formulario_cadastral': {
                'data_documento': {
                    'data_referencia_documento': date_helper.parse('2019-12-31T00:00:00')
                }
            },
            'informacoes_financeiras': [
                {
                    'descricao_conta': 'Patrimônio Líquido',
                    'valores_conta': [500., 600., 0., 0., 0., 0.]
                },
                {
                    'descricao_conta': 'Ativo Circulante',
                    'valores_conta': [123., 23., 0., 0., 0., 0.]
                }
            ],

        }
        resp = balanco_date_index_mapper.indices_to_date(dfp)

        expected = {
            0: date_helper.parse('2019-12-31T00:00:00'),
            1: date_helper.parse('2018-12-31T00:00:00')
        }

        self.assertEquals(resp, expected)

    def test_dfp_with_three_years(self):
        dfp = {
            'formulario_cadastral': {
                'data_documento': {
                    'data_referencia_documento': date_helper.parse('2019-12-31T00:00:00')
                }
            },
            'informacoes_financeiras': [
                {
                    'descricao_conta': 'Patrimônio Líquido',
                    'valores_conta': [500., 600., 123., 0., 0., 0.]
                },
                {
                    'descricao_conta': 'Ativo Circulante',
                    'valores_conta': [123., 23., -123., 0., 0., 0.]
                }
            ],

        }
        resp = balanco_date_index_mapper.indices_to_date(dfp)

        expected = {
            0: date_helper.parse('2019-12-31T00:00:00'),
            1: date_helper.parse('2018-12-31T00:00:00'),
            2: date_helper.parse('2017-12-31T00:00:00')
        }

        self.assertEquals(resp, expected)


    def test_itr_with_three_years(self):
        itr = {
            'formulario_cadastral': {
                'data_documento': {
                    'data_referencia_documento': date_helper.parse('2019-03-31T00:00:00')
                }
            },
            'informacoes_financeiras': [
                {
                    'descricao_conta': 'Patrimônio Líquido',
                    'valores_conta': [0., 500., 600., 123., 0., 0.]
                },
                {
                    'descricao_conta': 'Ativo Circulante',
                    'valores_conta': [0., 123., 23., -123., 0., 0.]
                }
            ],

        }
        resp = balanco_date_index_mapper.indices_to_date(itr)

        expected = {
            1: date_helper.parse('2019-03-31T00:00:00'),
            2: date_helper.parse('2018-03-31T00:00:00'),
            3: date_helper.parse('2017-03-31T00:00:00')
        }

        self.assertEquals(resp, expected)

    def test_itr_with_two_years(self):
        itr = {
            'formulario_cadastral': {
                'data_documento': {
                    'data_referencia_documento': date_helper.parse('2019-03-31T00:00:00')
                }
            },
            'informacoes_financeiras': [
                {
                    'descricao_conta': 'Patrimônio Líquido',
                    'valores_conta': [0., 500., 600., 0., 0., 0.]
                },
                {
                    'descricao_conta': 'Ativo Circulante',
                    'valores_conta': [0., 123., 23., 0., 0., 0.]
                }
            ],

        }
        resp = balanco_date_index_mapper.indices_to_date(itr)

        expected = {
            1: date_helper.parse('2019-03-31T00:00:00'),
            2: date_helper.parse('2018-03-31T00:00:00')
        }

        self.assertEquals(resp, expected)


if __name__ == '__main__':
    unittest.main()
