from sqlalchemy.types import TypeDecorator
from sqlalchemy import String
from datetime import datetime
from decimal import Decimal

class MyTime(TypeDecorator):
    # Decorator: design pattern - wrap up some code so whenever we
    # use it, some extra stuff is run
    "Convert datetime to strings and vice versa."

    impl = String

    cache_ok = True

    def __init__(self, length=None, format="%Y-%m-%d", **kwargs):
        super().__init__(length, **kwargs)
        self.format = format

    def process_literal_param(self, value, dialect):
        # allow passing string or time to column
        if isinstance(value, str):
            value = datetime.strptime(value, self.format).time()

        # convert python time to sql string
        return value.strftime(self.format) if value is not None else None

    process_bind_param = process_literal_param

    def process_result_value(self, value, dialect):
        # convert sql string to python time
        return datetime.strptime(value, self.format).date() if value is not None else None





class MyDecimal(TypeDecorator):
    "Convert Decimal to strings and vice versa."

    impl = String

    cache_ok = True

    def __init__(self, length=None, **kwargs):
        super().__init__(length, **kwargs)
        self.format = format

    def process_literal_param(self, value, dialect):
        # convert python Decimal to sql string
        return str(value) if value is not None else None

    process_bind_param = process_literal_param

    def process_result_value(self, value, dialect):
        # convert sql string to python Decimal
        return Decimal(value) if value is not None else None