import datetime
from datetime import date


class AgeCalculator:
    """
    Expects dates as strings formatted like YYYY-MM-DD
    """
    def __init__(self, birthday):
        self.year, self.month, self.day = (
            int(x) for x in birthday.split("-")
        )

    def calculate_age(self, date):
        year, month, day = (int(x) for x in date.split("-"))
        age = year - self.year
        if (month, day) < (self.month, self.day):
            age -= 1
        return age



a = AgeCalculator("2020-10-15")
a.calculate_age("2021-11-03")


class DateAgeAdapter():
    def _str_date(self, date):
        return date.strftime("%Y-%m-%d")

    def __init__(self, birthday):
        birthday = self._str_date(birthday)
        self.calculator = AgeCalculator(birthday)

    def get_age(self, date):
        date = self._str_date(date)
        return self.calculator.calculate_age(date)
        

def client_code():
    # ....
    my_birthday = datetime.datetime.strptime("2020-10-15", "%Y-%m-%d")

    a = DateAgeAdapter(my_birthday)
    a.get_age(datetime.datetime.today())

    # ....





















# another approach that makes date objects work with the original code
# note that there is a typo in our book where it repeatedly refers to the split method here as strip
# This is probably more confusing and thus harder to maintain than the adapter
class AgeableDate(datetime.date):
    def split(self, char):
        return self.year, self.month, self.day
