from helpers import regex_helper
import unittest


class TestRegex(unittest.TestCase):

    def test_patrimonio_liquido(self):
        positives = [
            'Patrimônio Líquido',
            'Patrimonio Liquido',
            'Patrimônio Liquido',
            'Patrimonio Líquido',
            'patrimônio líquido',
            'patrimonio liquido',
            'patrimônio liquido',
            'patrimonio líquido',
            'Patrimônio líquido',
            'patrimonio Liquido',
            'Patrimônio liquido',
            'patrimonio Líquido',
            'patrimônio líq',
            'patrimonio Liq',
            'Patrimônio liq',
            'patrimonio líq',
            'patr líquido',
            'patr. liq.',
            'patr. líq.',
            'patr liq.',
            'patr. liq',
            'patr. líq',
            'patr. líq.'
        ]

        for p in positives:
            resp1 = regex_helper.evaluate_indicador('patrimonio_liquido', p)
            self.assertIsNotNone(resp1, p)


if __name__ == '__main__':
    unittest.main()
