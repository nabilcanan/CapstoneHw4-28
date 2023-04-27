import unittest


def calc_total(state, items):
    tax_rates = {'DE': 0.0, 'NJ': 0.066, 'PA': 0.06}
    # print(tax_rates)
    # print(totalz)

    exempt_types = ['Wic Eligible food']

    clothing_exempt_types = ['Clothing']

    subtotal = sum(item['price'] for item in items)

    if state not in tax_rates:
        raise ValueError(f"Invalid state: {state}")




    tax_rate = tax_rates[state]
    taxable_items = [item for item in items if item['type'] not in exempt_types]
    taxable_clothing_items = [item for item in taxable_items if
                              item['type'] in clothing_exempt_types and 'fur' not in item['name'].lower()]



    tax_amount = sum(item['price'] * tax_rate for item in taxable_items) + sum(
        item['price'] * tax_rate for item in taxable_clothing_items)

    totalz = subtotal + tax_amount
    # print(totalz)
    return totalz


class TestCalculateTotal(unittest.TestCase):
    def test_DE_all_exempt(self):
        state = 'DE'


        items = [
            {'type': 'Wic Eligible food', 'name': 'Bread', 'price': 2.99},
            {'type': 'Clothing', 'name': 'T-Shirt', 'price': 9.99},
            {'type': 'everything else', 'name': 'Book', 'price': 14.99},
        ]


        expected_total = sum(item['price'] for item in items)
        total = calc_total(state, items)
        self.assertAlmostEqual(total, expected_total, delta=4)

    def test_NJ_all_taxable(self):
        state = 'NJ'
        items = [
            {'type': 'Wic Eligible food', 'name': 'Milk', 'price': 3.49},
            {'type': 'Clothing', 'name': 'Fur Coat', 'price': 299.99},
            {'type': 'everything else', 'name': 'Smartphone', 'price': 699.99},
        ]


        expected_total = sum(item['price'] for item in items) * 1.066
        total = calc_total(state, items)


        self.assertAlmostEqual(total, expected_total, delta=4)

    def test_PA_clothing_exempt(self):
        state = 'PA'

        items = [
            {'type': 'Wic Eligible food', 'name': 'Eggs', 'price': 1.99},
            {'type': 'Clothing', 'name': 'Sweater', 'price': 29.99},
            {'type': 'everything else', 'name': 'Headphones', 'price': 49.99},
        ]
        expected_total = sum(item['price'] for item in items) * 1.06 - 29.99 * 0.06
        total = calc_total(state, items)



        self.assertAlmostEqual(total, expected_total, delta=4)


if __name__ == '__main__':
    unittest.main()