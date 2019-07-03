import re
import gcc.tree.attributes
#from attributes import node_type
import gcc.tree.pprint2
#import gcc
#import gcc.tree
#import pprinto


class NodeBase:
    def nid(self):
        
        i = self.node_id
        if type (i) == str:
            return i
        else:
            return i.nid()
        #pprint.pprint(type(i))
         #   pprint.pprint(dir(i))
          #  pprint.pprint(i)
          #  raise Exception (i)
        
        
    
    def __init__(self, nid, ntype):
        #print "node id %s" % nid
        self.node_id = nid
        self.node_type = ntype
        #self.vals=vals

    # def keys(self):
        
    #     if (self.vals):
    #         if isinstance(self.vals, list):
    #             return  [
    #                 self.node_type, 
    #                 [
    #                     x.keys() for x in self.vals if x.keys()
    #                 ], 
    #                 [
    #                     x.values() for x in self.vals if x.values()
    #                 ]
    #             ]
    #         else:
    #             return [
    #                 self.node_type, 
    #                 #[self.vals.keys()], 
    #                 #[self.vals.values()]
    #             ]
    #     else:
    #         return  [
    #             self.node_type, 
    #                 [], 
    #                 []
    #             ]
                
    # def __str__(self):
    #     val=""
    #     if (self.vals):
    #         if isinstance(self.vals, list):
    #             #print "CHECK node type %s" % str(self.node_type)
    #             #print "CHECK node id %s" % str(self.node_id)
    #             #print "CHECK VALS %s" % str(self.vals)
    #             #print "CHECK VALS2 %s" % str( [attr.type for attr in self.vals]                )
    #             #print "CHECK VALS3 %s" % str( [str(attr) for attr in self.vals]               )
                
    #             #val="|".join(sorted([attr.type for attr in self.vals]))
    #             val="|".join(["Val:%s %s" % (str(attr.type), attr) for attr in self.vals])
    #         else:
    #             #print "CHECK VAL TYPE %s" % str(self.vals.type)
    #             #val="Val %s %s" % (self.vals.type, self.vals),
    #             pass
    #     return "T|%s|%s"  % (self.node_type,val)

node_dict = {}

class Node(NodeBase):
    def __init__(self, nid, ntype ):
        NodeBase.__init__(self,nid, ntype)
        global node_dict
        # save the node dictionary
        node_dict[nid]=self


class ExprBase(Node):
    pass

# class AddrExpr(ExprBase):
#     def __init__(self, ntype, nid, op_0):
#         ExprBase.__init__(self,ntype, nid,[])
#         self.op_0=op_0

#     def __str__(self):
# #        return "T|%s|OP_0|%s"  % (self.node_type,self.op_0)
#         return "T|%s|OP_0" % self.node_type

# class AddrExprTyped(AddrExpr):
#     def __init__(self, ntype, nid, op_0, expr_type):
#         AddrExpr.__init__(self,ntype, nid, op_0)
#         self.expr_type=expr_type

#     def __str__(self):
#         #return "T|%s|OP_0|%s|TYPE|%s"  % (self.node_type,self.op_0, self.expr_type)
#         return "T|%s|OP_0|TYPE"  % (self.node_type)
    

# class NodeConstructor(NodeBase):

#     def __init__(self, ntype, nid, vals):
#         NodeBase.__init__(self,nid, ntype, vals)


class Value(object):
    """
    Base class for all field attributes
    """
    def __init__(self, v):
#        assert(v)
        self.val = v

    def keys(self):
        pass

    def values(self):
        return self.val

class Link(Value):

    def __init__(self, v):
        Value.__init__(self, v)


class VConstructor(Value):

    def __init__(self, v):
        Value.__init__(self, v)


class Struct(Value):

    def __init__(self, v):
        Value.__init__(self, v)


class Signed(Value):

    def __init__(self, v):
        Value.__init__(self, v)


class Artificial(Value):

    def __init__(self, v):
        Value.__init__(self, v)


class Qual(Value):

    def __init__(self, v):
        Value.__init__(self, v)


class Lang(Value):

    def __init__(self, v):
        Value.__init__(self, v)


class NodeRef(Value):

    def __init__(self, v):
        #assert(v)
        #print "create node ref %s" % v
        Value.__init__(self, v)

    def keys(self):
        return self.val

    def values(self):
        pass



class NodeRefSpec(NodeRef):

    def __init__(self, v, v2):
        NodeRef.__init__(self, v)
        self.spec = v2


class PseudoTempl(Value):

    def __init__(self, v, v2):
        Value.__init__(self, v)
        self.v2 = v2


class Op(Value):

    def __init__(self, v):
        Value.__init__(self, v)


class AccVal(Value):

    def __init__(self, v):
        Value.__init__(self, v)

class AccSpec(AccVal):

    def __init__(self, v, v2):
        AccVal.__init__(self, v)
        self.spec = v2


class Spec(Value):
    def __init__(self, v):
        Value.__init__(self, v)


class Member(Value):
    def __init__(self, v):
        Value.__init__(self, v)


class Float(Value):

    def __init__(self, v):
        Value.__init__(self, v)


class String(Value):

    def __init__(self, v):
        Value.__init__(self, v)

    @property
    def type(self):
        return "STR"

    def keys(self):
        pass

    def values(self):
        return ["String",self.val]

class String2(Value):

    def __init__(self, v):
        m = re.match(r'(.*)lngt: (\d+)\s+addr:\s+([a-h0-9]+)$',v)
        if m :
            l = int(m.group(2))
            v2 = v[0:l]
            self.addr = m.group(3)
            Value.__init__(self, v2)
        else:
            Value.__init__(self, v)

    @property
    def type(self):
        return "STR"

    def keys(self):
        pass

    def values(self):
        return ["String",self.val]

    def __repr__(self):
        return "'%s'" % (self.val)

class Note(Value):

    def __init__(self, v):
        Value.__init__(self, v)


class FloatSpec(Float):

    def __init__(self, v, v2):
        self.spec = v2
        Float.__init__(self, v)


class AttrBase(object):

    @property
    def type(self):
        return "TODO(%s)" % self.__class__.__name__

    def keys(self):
        pass

    def values(self):
        pass


class MemberAttr(AttrBase):

    def __init__(self, value):
        self.value = value


class NoteAttr(AttrBase):

    def __init__(self, value):
        self.value = value


class Attr(AttrBase):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def keys(self):
        if isinstance(self.value, str):
            #return "Str: "+ self.value
            #return "Str: "+ self.value
            return None
        else:
            if list(self.value.keys()):
                return [self.name, list(self.value.keys())]
            else:
                return None

    def values(self):
        if isinstance(self.value, str):
            return self.value
        else:
            if list(self.value.values()):
                return [self.name, list(self.value.values())]
            else:
                return None

    @property
    def type(self):
        return self.name


class EmptyAttr(AttrBase):
    pass


class SpecAttrBase(AttrBase):

    @property
    def type(self):
        return "spec"

class SpecAttr2(SpecAttrBase):

    def __init__(self, value, value2):
        self.name = 'spec'
        self.value = value
        self.value2 = value2

    @property
    def type(self):
        return self.name

class SpecAttr3(SpecAttrBase):

    def __init__(self, value):
        self.name = 'spec'
        self.value = value

    @property
    def type(self):
        return self.name


class SpecAttr(SpecAttrBase):

    def __init__(self, name, value, value2):
        self.name = name
        self.value = value
        self.value2 = value2


class FilePos(Attr):

    def __init__(self, value):
        Attr.__init__(self, 'file', value)


class FileBuiltin(AttrBase):
    pass


class Decl(Node):
    pass

def pstack(o):
    r = ""
    #print "Stack:%s" % pprint2.pformat(self.o.stack)
    #pprint2.pprint(dir(self.o))
    #pprint2.pprint(self.o.__dict__)
    for s in o.stack:
        if s.type == '$end':
            pass
        else:
            s1= "[type:%s t2:%s value:%s]," % (s.type, type(s.value), s.value.node_id)
            r = r + s1
            #print "Stack",s,pprint2.pformat(s)
            #print "Stack",s,pprint2.pformat(dir(s))
            #print "Stack",s,pprint2.pformat(s.__dict__)
    return r


class FunctionDecl(Decl):
    def __init__(self, nodeid, nodetype , nodedata):
        #print "Nodetype '%s'" %nodetype
        #print "Nodeid '%s'" %nodeid.value
        Decl.__init__(self,nodeid.value(), nodetype)
        #self.value = nodedata.slice[-1].value.val
        #self.nodedata=nodedata
        #pprint2.pprint(nodedata.slice[-1].__dict__)
        #pprint2.pprint([nodeid.value,nodetype,nodedata.slice])
    def __str2__(self):
        return "FunctionDecl: %s %s " % (self.node_id, pprint2.pformat2(self.__dict__))
    def __repr2__(self):
        return "FunctionDecl: %s %s %s" % (self.node_id, pprint2.pformat2(self.__dict__),pstack(self.nodedata))
    
#@node_type('identifier_node')
class Identifier(Node):
    def __init__(self, nodeid, nodetype , nodedata):
        #print "Nodetype '%s'" %nodetype
        #print "Nodeid '%s'" %nodeid.value
        Node.__init__(self,nodeid, nodetype)

        #print 'SLICE:'
        #pprint.pformat(nodedata.slice)
        
        v = nodedata.slice[-1].value
        #pprint2.pprint ({'value':nodeid.value(), 'type': nodetype, 'v': v})
        if 'string' in v:
            self.value = v['string']
        else:
            if 'strattrs' in v:
                if 'string' in v['strattrs']:
                    self.value = v['strattrs']['string']
                else:
                    raise Exception(pprint.pformat(v))
            else:
                raise Exception(pprint.pformat(v))

        if 'addr' in v:
            self.addr = v['addr']
        
    def __str__(self):
        return "Identifier: %s %s " % (self.node_id, self.value)
#gcc.tree.attributes.register('identifier_node',Identifier)
#gcc.tree.attributes.register('function_decl',FunctionDecl)
