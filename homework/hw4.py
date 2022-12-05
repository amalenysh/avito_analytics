import json
from collections import namedtuple
from keyword import iskeyword


class JsonToPyth:
    """
    Rewrite JSON-objects в python-objects
    """

    def __call__(self, obj: object, dictionary: dict):
        for key, value in dictionary.items():
            if iskeyword(key):
                key += '_'

            if type(value) is dict:
                key_type = namedtuple(f'{key}', value.keys())
                setattr(obj, key, key_type(**value))
                self.__call__(getattr(obj, key), value)

            elif not hasattr(obj, key):
                setattr(obj, key, value)


class BaseAdvert:
    """
    Here is all information about advertisement
    """

    def __init__(self, mapping: dict):
        json_unpacked = JsonToPyth()
        json_unpacked(self, mapping)
        self._title_check()

    def _title_check(self):
        if not hasattr(self, 'title'):
            raise ValueError('Ad does not have title')

    def _price_check(self, price):

        price = self._price if price is None else price
        
        if type(price) is not int:
            raise ValueError('Type has to be integer')

        if price < 0:
            raise ValueError('Price can not be negative')

    @property
    def price(self) -> int:
        return getattr(self, '_price', 0)

    @price.setter
    def price(self, value):
        self._price_check(value)
        self._price = value

    def __repr__(self):
        return f"{getattr(self, 'title')} | {self.price} ₽"


class ColorizeMixin:
    """
    you can change color of the text
    """
    repr_color_code = 32

    def __repr__(self):
        color: int = self.repr_color_code
        repr_str = super().__repr__()
        return f"\033[1:{color}:48m{repr_str}\033[00m"


class Advert(ColorizeMixin, BaseAdvert):
    def __init__(self, mapping: dict):
        super().__init__(mapping)
        self.name_attr = None

    """
    Merging ColorizeMixin and BaseAdvert classes
    """
    pass


iphone_dict = """{
    "title": "iPhone X",
    "location": {
        "address": "город Самара, улица Мориса Тореза, 50",
        "metro_stations": ["Спортивная", "Гагаринская"]}}"""
if __name__ == "__main__":
    check = json.loads(iphone_dict)
    iphone = Advert(check)
    print(iphone.__str__())
    print(iphone.__dict__)
