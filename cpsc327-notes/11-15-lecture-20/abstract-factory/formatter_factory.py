# date formatters

class DateFormatter:
    def format_date(self, y, m, d):
        raise NotImplementedError()

class FranceDateFormatter(DateFormatter):
    def format_date(self, y, m, d):
        y, m, d = (str(x) for x in (y, m, d))
        y = "20" + y if len(y) == 2 else y
        m = "0" + m if len(m) == 1 else m
        d = "0" + d if len(d) == 1 else d
        return "{0}/{1}/{2}".format(d, m, y)

class USADateFormatter(DateFormatter):
    def format_date(self, y, m, d):
        y, m, d = (str(x) for x in (y, m, d))
        y = "20" + y if len(y) == 2 else y
        m = "0" + m if len(m) == 1 else m
        d = "0" + d if len(d) == 1 else d
        return "{0}-{1}-{2}".format(m, d, y)



# currency formatters

class CurrencyFormatter:
    def format_currency(self, base, cents):
        raise NotImplementedError()

class FranceCurrencyFormatter(CurrencyFormatter):
    def format_currency(self, base, cents):
        base, cents = (str(x) for x in (base, cents))
        if len(cents) == 0:
            cents = "00"
        elif len(cents) == 1:
            cents = "0" + cents

        digits = []
        for i, c in enumerate(reversed(base)):
            if i and not i % 3:
                digits.append(" ")
            digits.append(c)
        base = "".join(reversed(digits))
        return "{0}€{1}".format(base, cents)

class USACurrencyFormatter(CurrencyFormatter):
    def format_currency(self, base, cents):
        base, cents = (str(x) for x in (base, cents))
        if len(cents) == 0:
            cents = "00"
        elif len(cents) == 1:
            cents = "0" + cents
        digits = []
        for i, c in enumerate(reversed(base)):
            if i and not i % 3:
                digits.append(",")
            digits.append(c)
        base = "".join(reversed(digits))
        return "${0}.{1}".format(base, cents)


# formatter factories

class USAFormatterFactory():
    def create_date_formatter(self):
        return USADateFormatter()

    def create_currency_formatter(self):
        return USACurrencyFormatter()

class FranceFormatterFactory():
    def create_date_formatter(self):
        return FranceDateFormatter()

    def create_currency_formatter(self):
        return FranceCurrencyFormatter()



# method I: have formatter factory determine which factory to create

class FormatterFactory:
    def __init__(self) -> None:
        # gets the country_code
        if country_code == "US":
            self.factory = USAFormatterFactory()
        elif country_code == "FR":
            self.factory = FranceFormatterFactory()

    def create_date_formatter(self):
        return self.factory.create_date_formatter()
    
FormatterFactory().create_date_formatter().format_date("21", "11", "15")


# method II: have client code determine which factory to create

country_code = "US"

factory_map = {"US": USAFormatterFactory, "FR": FranceFormatterFactory}
formatter_factory = factory_map.get(country_code)()

formatter_factory.create_date_formatter().format_date("21", "11", "15")



