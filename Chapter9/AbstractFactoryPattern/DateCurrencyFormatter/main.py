class FranceDateFormatter:
    def formate_date(self, y, m, d):
        y, m, d = (str(x) for x in (y, m, d))
        y = '20{0}'.format(y if len(y) == 2 else y)
        m = '0{0}'.format(m if len(m) == 1 else m)
        d = '0{0}'.format(d if len(d) == 1 else d)
        return "{0}/{1}/{2}".format(d, m, y)


class USADateFormatter:
    def format_date(self, y, m, d):
        y, m, d = (str(x) for x in (y, m, d))
        y = '20{0}'.format(y if len(y) == 2 else y)
        m = '0{0}'.format(m if len(m) == 1 else m)
        d = '0{0}'.format(d if len(d) == 1 else d)
        return "{0}-{1}-{2}".format(m, d, y)


class FranceCurrencyFormatter:
    def format_currency(self, base, cents):
        base, cents = (str(x) for x in (base, cents))
        if len(cents) == 0:
            cents = "00"
        elif len(cents) == 1:
            cents = f"0{cents}"

        digits = []
        for i, c in enumerate(reversed(base)):
            if i and not i % 3:
                digits.append(' ')
            digits.append(c)

        base = ''.join(reversed(digits))
        return "{0}€{1}".format(base, cents)


class USACurrencyFormatter:
    def format_currency(self, base, cents):
        base, cents = (str(x) for x in (base, cents))
        if len(cents) == 0:
            cents = "00"
        elif len(cents) == 1:
            cents = f"0{cents}"

        digits = []
        for i, c in enumerate(reversed(base))
            if i and not i % 3:
                digits.append(",")

            digits.append(c)

        base = ''.join(reversed(digits))
        return "${0}.{1}".format(base, cents)


class USAFormatterFactory:
    def create_date_formatter(self):
        return USADateFormatter

    def create_currency_formatter(self):
        return USACurrencyFormatter()


class FranceFormatterFactory:
    def create_date_formatter(self):
        return FranceDateFormatter()

    def create_currency_formatter(self):
        return FranceCurrencyFormatter()


if __name__ == '__main__':
    country_code = "US"
    factory_map = {
        "USA" : USAFormatterFactory,
        "FR" : FranceFormatterFactory
    }
    formatter_factory = factory_map.get(country_code)()
