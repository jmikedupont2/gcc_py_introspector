"""Read the json string and does some processing on it."""
import collections
import json
import sys


data = {"undefined": {"_type": "undefined"}}


# _type type_decl
# _string int
main = {
    "_string": 1,
    "_id": "77817",
    #    "_type": "tree_list",
    "srcp": "",
    "addr": "",  # many strings
    "val": "",  # many strings
    "value": "",
    "valu": "",
}

scalars = {
    "algn": {
        "32": 2188, "8": 2990,
        "128": 17, "64": 5629, "16": 211, "1": 102},
    "prec": {
        "32": 250,
        "8": 26,
        "128": 7,
        "64": 218,
        "16": 41,
        "80": 1,
        "1": 1,
        "2": 1,
        "4": 1,
        "59": 1,
        "40": 1,
        "31": 1,
        "5": 1,
        "14": 1,
        "7": 1,
        "24": 1,
        "0": 1,
        "30": 1,
        "48": 1,
        "52": 1,
    },
    "sign": {"signed": 209, "unsigned": 339},
    "tag": {"struct": 760, "union": 120},
    "link": {"extern": 4048, "static": 440},
    "qual": {"c ": 133, "v ": 14, "r ": 99, "cv ": 2},
    "used": {"1": 2194, "0": 66},
    "length": {
        "1": 176,
        "4": 5,
        "7": 11,
        "6": 12,
        "98": 1,
        "3": 53,
        "2": 126,
        "5": 29,
        "8": 1,
        "16": 2,
        "23": 1,
        "18": 1,
        "21": 1,
        "12": 1,
        "13": 1,
        "11": 1,
        "42": 1,
        "9": 1,
    },
}

remove = {
    "_id": 1,
}

clean = set(scalars.keys()).union(set(main.keys())).union(set(remove.keys()))
# print(clean)


fields = {
    "name": "77813",
    "type": "77808",
    # "chain": "1382",
    # "_string": "__divtc3",
    "size": "127",
    # "algn": 128, "prec": 32, "sign": "unsigned",
    "min": "28",
    "max": "29",
    # "value": "1248",
    "unql": "100",
    "elts": "1215",
    "domn": "10839",
    # "tag": "union",
    "flds": "77349",
    "ptd": "76426",
    # "srcp": "<built-in>:0",
    "scpe": "154",
    "bpos": "1367",
    "mngl": "77769",
    "body": "undefined",
    # "link": "extern",
    "retn": "77811",
    "prms": "77812",
    # "valu": "75148",
    #    "chan": "165",
    # "qual": "c ",
    "csts": "77230",
    "cnst": "1132",
    "purp": "77262",
    "args": "76066",
    "argt": "203",
    # "used": "1",
    "expr": "75501",
    "OP0 :": "76077",
    "OP1": "11725",
    "vars": "73454",
    "init": "73849",
    "E0": "76105",
    "E1": "1025",
    "E2": "76087",
    "OP2": "73303",
    "fn": "76104",
    "E3": "76097",
    "E4": "74695",
    "E5": "73030",
    "E6": "73031",
    "E7": "73032",
    "E8": "73033",
    "E9": "73034",
    "E10": "72687",
    "labl": "73304",
    "E11": "72084",
    "E12": "72085",
    "E13": "72086",
    "E14": "72087",
    # "addr": "sshd     ", "val": "sshd ",
    "decl": "73182",
    "cond": "70566",
    # "length": 2,
    "idx": "8400",
    "low": "9524",
    # "E15": "72088",
    "orig": "30807",
    # "E16": "72089", "E17":
    "refd": "139",
}

for x in clean:
    if x in fields:
        print("del", x)
        del fields[x]


def collect_scalars(d):
    """Collect scalar fieldnames from system.

    Used for one time analysis.
    """
    for f in d:
        v = d[f]
        if f in main:
            continue
        if f not in fields:
            if f not in scalars:
                scalars[f] = {v: 1}
            else:
                if v not in scalars[f]:
                    scalars[f][v] = 1
                else:
                    scalars[f][v] = scalars[f][v] + 1


# collect the data and the scalars

positions = [
    "SELF" "PARENT",  # 0  # 1
    "GRANDPARENT",  # 2
    "GREAT-GRANDPARENT",  # 3
]


def recurse_clean(dat, seen):
    """Recurse over the data and clean it up."""
    for x in dat:
        v = dat[x]
        if "DUP" in v:
            if "FORWARD" in v["DUP"]:
                _id = v["DUP"]["FORWARD"]
                v2 = seen[_id]
                # print(v2)
                dat[x] = v2

        elif "FORWARD" in v:
            _id = v["FORWARD"]
            v2 = seen[_id]
            # print(v2)
            dat[x] = v2
        else:
            if isinstance(v, dict):
                dat[x] = recurse_clean(v, seen)

    return dat


def recurse(_id, depth=0, seen={}, root=None):
    """Recurse over the nodes."""
    if root is None:
        root = []
    else:
        if _id in root:
            idx = root.index(_id)
            pos = len(root) - 1 - idx
            if pos < len(positions):
                pos = positions[pos]
            elif idx == 0:
                pos = "ROOT"
            else:
                pos = "GREAT({})-GRANDPARENT".format(pos - 3)
            return "{}".format(pos)

    if depth > 900:
        return "STACK"

    if _id in seen:
        return seen[_id]
    seen[_id] = {"FORWARD": _id}
    d = data[_id]
    newt = {
        "_type": d["_type"],
    }

    # if "_string" in d:
    #    newt["_string"] = d["_string"]

    for f in d:
        v = d[f]
        if f in fields:
            newroot = []
            newroot.extend(root)
            newroot.append(_id)
            ft = recurse(_id=v, depth=depth + 1, seen=seen, root=newroot)
            newt[f] = ft
            seen[f] = ft

        # else:
        # seen[f] = "SKIP{}".format(v)
        # now replace all the fowards?
    # iterate and replace all forwards now

    newt = recurse_clean(newt, seen)
    seen[_id] = newt
    return newt


def main(filename):
    """The main routine of the program does everything.""" # NOQA
    with open(filename) as inf:
        for l in inf:
            d = json.loads(l)
            data[d["_id"]] = d

    types2 = collections.Counter()

    # now look at the fields
    for _id in data:
        t = recurse(_id, depth=0, seen={})
        # print(_id, pprint.pformat(t))
        # print(t)

        types2[str(t)] += 1

    for x in types2.most_common(10):
        print(x)

    # print(json.dumps(data))
    # for x in types2:
    #    print(x, types2[x])


if __name__ == "__main__":
    main(sys.argv[1])
