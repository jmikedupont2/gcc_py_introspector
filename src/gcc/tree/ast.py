import pprint


class Something:
    def __init__(self, **kwargs):
        pprint.pprint(kwargs)
        self._data = kwargs

    @property
    def _id(self):
        if "_id" in self._data:
            return self._data["_id"]
        else:
            pprint.pprint(self._data)
            return None

    @property
    def _type(self):
        if "_type" in self._data:
            return self._data["_type"]
        else:
            pprint.pprint(self._data)
            return None


class Attr:
    def __init__(self, d):
        self.d = d


class StringAttrs:
    def __init__(self, strattrs, alist=None):
        self.string = strattrs
        self._list = alist


class List:
    def __init__(self, attrs, _list):
        self.attrs = attrs
        self._list = list

    def collapse(self):
        # todo
        ""


class Add:
    pass


class PlusEqual:
    pass


class Operator:
    pass
