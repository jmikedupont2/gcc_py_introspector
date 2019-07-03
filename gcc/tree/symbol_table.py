# global symbol table
import pprint

nodes_seen = {}


def declare_node(value):
    """Declare a nodes values after the line is finished parsing in the tu file"""
    value.to_json()
    _id = value._id
    if _id not in nodes_seen:
        raise Exception(_id)
    else:
        if nodes_seen[_id] == "declared":
            nodes_seen[_id] = value
        else:
            raise Exception(_id)
