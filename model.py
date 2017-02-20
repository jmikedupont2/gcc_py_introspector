import django
from django.db import models

    
class SourceFile(models.Model):
    filename = models.CharField(max_length=228)
    
class Node(models.Model):
    source_file= models.ForeignKey(SourceFile)
    nid= models.IntegerField()
    
    class Meta:
        unique_together = (('source_file', 'node_id'),)
        
    refs_argt = models.IntegerField()
    refs_prms = models.IntegerField()
    attrs_string = models.CharField(max_length=228)
    refs_domn = models.IntegerField()
    refs_retn = models.IntegerField()
    refs_bpos = models.IntegerField()
    refs_max = models.IntegerField()
    refs_csts = models.IntegerField()
    refs_valu = models.IntegerField()
    refs_min = models.IntegerField()
    refs_name = models.IntegerField()
    refs_size = models.IntegerField()
    refs_type = models.IntegerField()
    refs_unql = models.IntegerField()
    refs_val = models.IntegerField()
    refs_args = models.IntegerField()
    refs_elts = models.IntegerField()
    refs_refd = models.IntegerField()
    refs_low = models.IntegerField()
    refs_body = models.IntegerField()
    refs_purp = models.IntegerField()
    refs_chan = models.IntegerField()
    type = models.IntegerField()
    refs_cnst = models.IntegerField()
    attrs_type_name = models.CharField(max_length=3)
    refs_fn = models.IntegerField()
    refs_chain = models.IntegerField()
    refs_ptd = models.IntegerField()
    refs_mngl = models.IntegerField()
    nid = models.IntegerField()
    refs_cond = models.IntegerField()
    refs_vars = models.IntegerField()
    refs_OP0 = models.IntegerField()
    refs_OP1 = models.IntegerField()
    refs_OP2 = models.IntegerField()
    refs_E = models.IntegerField()
    attrs_note = models.CharField(max_length=4)
    refs_idx = models.IntegerField()
    refs_scpe = models.IntegerField()
    refs_flds = models.IntegerField()
    attrs_type_size = models.CharField(max_length=35)
    refs_init = models.IntegerField()
    refs_expr = models.IntegerField()
    attrs_addr = models.CharField(max_length=12)
    refs_decl = models.IntegerField()
    refs_labl = models.IntegerField()
    attrs_type = models.CharField(max_length=21)