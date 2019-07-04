import pprint as orig

def pprint(*argv, **kvargs):
    if argv:
        orig.pprint(argv)
    if kvargs:
        orig.pprint(kvargs)

    pass


def pformat(*argv, **kvargs):
    # raise Exception('')
    return orig.pformat([argv,kvargs])


def pformat2(*argv, **kvargs):
    return orig.pformat([argv,kvargs])
    pass


def dprint(*argv, **kvargs):
    if argv:
        orig.pprint(argv)
    if kvargs:
        orig.pprint(kvargs)

    pass
