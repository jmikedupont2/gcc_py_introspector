import pprint

class Leaf:
    def to_dict(self):
        #pprint.pprint({ 's': self, 'd': self.__dict__ })
        return self.__dict__
    def append_list(self, alist):
        alist.append(self.to_dict())
    def to_list(self):
        ret = []
        self.append_list(ret)
        return ret

class Field(Leaf):
    def __init__(self, **kwargs):
        #pprint.pprint({"Field":kwargs})
        self.__dict__ = kwargs

class IntegerCst:
    def __init__(self, type_node, value):
        self.type_node = type_node
        self.value = value
    def to_dict(self):
        #pprint.pprint(self.__dict__)
        return {
            'type':self.type_node.to_dict()['type'],
            'value':self.value
        }
        return self.__dict__
        
class Something:
    def __init__(self, **kwargs):
        #pprint.pprint({'smg':kwargs})
        raise Exception()
        self._data = kwargs

    @property
    def _id(self):
        if "_id" in self._data:
            return self._data["_id"]
        else:
            # pprint.pprint(self._data)
            return None

    @property
    def _type(self):
        if "_type" in self._data:
            return self._data["_type"]
        else:
            # pprint.pprint(self._data)
            return None


class Attr:
    def __init__(self, d):
        #pprint.pprint({'attr':d})
        self.d = d


class StringAttrs:
    def __init__(self, strattrs, alist=None):
        self.string = strattrs
        self._list = alist
        
    def to_string(self):
        #pprint.pprint({'string': self.string, 'alist':self._list})
        return self.string.to_string()
    
    def append_list(self, alist):
        self.string.append_list(alist)
        if self._list :
            self._list.append_list(alist)

class List:
    def __init__(self, attrs, _list):
        #pprint.pprint({'attr': attrs, 'alist':_list})
        self.attrs = attrs
        self._list = list
    def to_list(self):
        ret = []
        self.attrs.append_list(ret)
        self._list.append_list(ret)
        return ret

    def to_dict(self):
        values = {}
        for x in self.to_list():
            values.update(x)
        return values


class Add:
    pass


class PlusEqual:
    pass


class Operator:
    pass
class Artificial(Leaf):
    """Note: artificial"""
    
class ConstructorItem(Leaf):
    def __init__(self, idx, val):
        if isinstance( idx, str):
            raise Exception()
        self.idx=idx
        self.val=val

    def to_dict(self):
        # pprint.pprint({'s':self, 'd':self.__dict__})
        return {
            'idx' : self.idx.to_dict(),
            'val' : self.val.to_dict()

        }

class ConstructorList:
    def __init__(self, node, llen, llist):
        self.node=node
        self.llen=llen
        self.llist=llist

class ConstructorListChain:
    def __init__(self, head, tail):
        self.head=head
        self.tail=tail
    def to_list(self):
        ret = []
        #pprint.pprint(self.__dict__)

        self.head.append_list(ret)
        self.tail.append_list(ret)
        return ret
    
    def append_list(self, alist):

        self.head.append_list(alist)
        self.tail.append_list(alist)
    def to_dict(self):
        values = {}
        for x in self.to_list():
            values.update(x)
        return values

class BitField(Leaf):
    pass

class NodeRef(Leaf):
    def __init__(self, node, name):
        self.node = node
        self.name = name
    def to_dict(self):
        return { self.name : self.node }

class AttrList:
    def __init__(self, attr, _list=None):
#        pprint.pprint({"debug attr":attr})
        self.attr = attr
        self._list = _list
    def append_list(self, alist):
        self.attr.append_list(alist)
        if self._list:
            self._list.append_list(alist)
    def to_list(self):
        ret = []
        self.attr.append_list(ret)
        if self._list:
            self._list.append_list(ret)
        return ret
    def to_dict(self):
        values = {}
        for x in self.to_list():
            values.update(x)
        return values


class List:
    def __init__(self, attr, _list):
        self.attr = attr
        self._list = _list

    def to_list(self):
        ret = []
        self.attr.append_list(ret)
        self._list.append_list(ret)
        return ret
    def to_dict(self):
        #return { 'somelist' : self.to_list() }
        values = {}
        for x in self.to_list():
            values.update(x)
        return values

    def append_list(self, alist):
        #import pdb
        #pdb.set_trace()
        # pprint.pprint(
        #     {
        #         's':self, 'd': self.__dict__,
        #         'a' :self.attr,
        #         'ad': self.attr.__dict__,
        #         'ap': self.attr.append_list,
        #         'l': alist,
        #     }
        # )
        self.attr.append_list(alist)
        if self._list:
            self._list.append_list(alist)
class SomeLen(Leaf):
    def __init__(self, va):
        self.va = va
class ConstructorList2(Leaf):
    def __init__(self, l):
        self.l = l
class FakeConstructor(Leaf):
    ""
