There are parts of the graph that represent themselves.

We find that in the tree.c there are string constants that represent parts of the tree in the dump.

```
grep string_cst *.tu  | grep component_ref
```

Example :
```
tree.c.001t.tu:@3135   string_cst       type: @3904   strg: component_ref  lngt: 14
```

We can extract all the strings:
```
grep string_cst tree.c.001t.tu | cut -d: -f 3-4| sort | uniq -c | sort  -n
```

Looking up how that is used we see :
```
grep -P -e '@3135\s' tree.c.001t.tu
```

The address is taken from the string
`@2349   addr_expr        type: @3091    op 0: @3135`

Then there is a nop 
`@1368   nop_expr         type: @679     op 0: @2349`


Which is referenced in an array, this is the type array whose index is the tree offset
`val : @1366    idx : @1367    val : @1368`

So 45 is the value of the component_ref
`@1367   integer_cst      type: @46     int: 45`

Looking in the context of the list we find the constructor of the array with 350 item
`grep -C100 -P -e 'val : @1368\s' tree.c.001t.tu`

`@960    constructor      lngt: 350      idx : @17      val : @1293`

trial and error gives us the values in the array :
`grep -A233 -P -e '@960    constructor' tree.c.001t.tu`

Extracting the first column of indexes
`grep -A235 -P -e '@960    constructor' tree.c.001t.tu | grep idx | cut -d: -f1-2 | grep 'idx :' | cut -d: -f2 | cut '-d ' -f2 | sort -n`

Gives us
`@19 @79 @85 @91 @491 @1309 @1315 @1321 @1327 @1333 @1339 @1345 @1351 @1357 @1363 @1369 @1375 @1381 @1387 @1393 @1399 @1126 @1410 @1416 @1422 @1428 @1434 @1440 @1446 @1452 @1458 @1464 @1470 @1476 @1482 @1488 @1494 @1500 @1506 @1512 @1518 @1524 @1530 @1535 @1541 @1547 @1553 @1559 @1565 @1571 @1577 @1583 @1589 @1595 @1601 @1607 @1613 @1619 @1625 @1631 @1637 @1643 @1649 @1655 @1661 @1667 @1673 @1679 @1685 @1691 @1697 @1703 @1709 @1715 @1721 @1727 @1733 @1739 @1745 @1751 @1757 @1763 @1769 @1775 @1781 @1787 @1793 @1799 @1805 @1811 @1817 @1823 @1829 @1835 @1841 @1847 @1853 @1859 @1865 @1871 @1877 @1883 @1889 @1895 @1901 @1907 @1913 @1919 @1925 @1931 @1937 @1943 @1949 @1955 @1961 @1967 @955`


the second column is by extracting 2-3 
`grep -A235 -P -e '@960    constructor' tree.c.001t.tu | grep idx | cut -d: -f2-3 | grep 'idx :' | cut -d: -f2 | cut '-d ' -f2 | xargs echo`



Third is 3-4
`grep -A235 -P -e '@960    constructor' tree.c.001t.tu | grep idx | cut -d: -f3-4 | grep 'idx :' | cut -d: -f2 | cut '-d ' -f2 | xargs echo`

So combining all three  :
`@21 @81 @87 @93 @493 @1311 @1317 @1323 @1329 @1335 @1341 @1347 @1353 @1359 @1365 @1371 @1377 @1383 @1389 @1395 @1401 @1406 @1412 @1418 @1424 @1430 @1436 @1442 @1448 @1454 @1460 @1466 @1472 @1478 @1484 @1490 @1496 @1502 @1508 @1514 @1520 @1526 @1532 @1537 @1543 @1549 @1555 @1561 @1567 @1573 @1579 @1585 @1591 @1597 @1603 @1609 @1615 @1621 @1627 @1633 @1639 @1645 @1651 @1657 @1663 @1669 @1675 @1681 @1687 @1693 @1699 @1705 @1711 @1717 @1723 @1729 @1735 @1741 @1747 @1753 @1759 @1765 @1771 @1777 @1783 @1789 @1795 @1801 @1807 @1813 @1819 @1825 @1831 @1837 @1843 @1849 @1855 @1861 @1867 @1873 @1879 @1885 @1891 @1897 @1903 @1909 @1915 @1921 @1927 @1933 @1939 @1945 @1951 @1957 @1963 @1969 @17 @23 @83 @89 @95 @495 @1313 @1319 @1325 @1331 @1337 @1343 @1349 @1355 @1361 @1367 @1373 @1379 @1385 @1391 @1397 @1403 @1408 @1414 @1420 @1426 @1432 @1438 @1444 @1450 @1456 @1462 @1468 @1474 @1480 @1486 @1492 @1498 @1504 @1510 @1516 @1522 @1528 @1127 @1539 @1545 @1551 @1557 @1563 @1569 @1575 @1581 @1587 @1593 @1599 @1605 @1611 @1617 @1623 @1629 @1635 @1641 @1647 @1653 @1659 @1665 @1671 @1677 @1683 @1689 @1695 @1701 @1707 @1713 @1719 @1725 @1731 @1737 @1743 @1749 @1755 @1761 @1767 @1773 @1779 @1785 @1791 @1797 @1803 @1809 @1815 @1821 @1827 @1833 @1839 @1845 @1851 @1857 @1863 @1869 @1875 @1881 @1887 @1893 @1899 @1905 @1911 @1917 @1923 @1929 @1935 @1941 @1947 @1953 @1959 @1965 @1971 @19 @79 @85 @91 @491 @1309 @1315 @1321 @1327 @1333 @1339 @1345 @1351 @1357 @1363 @1369 @1375 @1381 @1387 @1393 @1399 @1126 @1410 @1416 @1422 @1428 @1434 @1440 @1446 @1452 @1458 @1464 @1470 @1476 @1482 @1488 @1494 @1500 @1506 @1512 @1518 @1524 @1530 @1535 @1541 @1547 @1553 @1559 @1565 @1571 @1577 @1583 @1589 @1595 @1601 @1607 @1613 @1619 @1625 @1631 @1637 @1643 @1649 @1655 @1661 @1667 @1673 @1679 @1685 @1691 @1697 @1703 @1709 @1715 @1721 @1727 @1733 @1739 @1745 @1751 @1757 @1763 @1769 @1775 @1781 @1787 @1793 @1799 @1805 @1811 @1817 @1823 @1829 @1835 @1841 @1847 @1853 @1859 @1865 @1871 @1877 @1883 @1889 @1895 @1901 @1907 @1913 @1919 @1925 @1931 @1937 @1943 @1949 @1955 @1961 @1967 @955`

Collecting those ids gives us :
```
  grep -A235 -P -e '@960    constructor' tree.c.001t.tu | grep idx | cut -d: -f3-4 | grep 'idx :' | cut -d: -f2 | cut '-d ' -f2 > id.txt
  grep -A235 -P -e '@960    constructor' tree.c.001t.tu | grep idx | cut -d: -f1-2 | grep 'idx :' | cut -d: -f2 | cut '-d ' -f2 >> id.txt
  grep -A235 -P -e '@960    constructor' tree.c.001t.tu | grep idx | cut -d: -f2-3 | grep 'idx :' | cut -d: -f2 | cut '-d ' -f2 >> id.txt
```

for x in `cat id.txt`; do echo $x; grep -P -e "^$x\s" tree.c.001t.tu; done  | grep int: | cut -d: -f3 > values.txt
`sort -n values.txt`

`wc values.txt ` gives us 350 elements
 350  350 1640 values.txt

So now we have all the array values of the type indexes as node ids, lets look at the usages where they index something or are compared to something.


If we take the original one, 17, we find 742 nop_expr

`grep -P -e "\s@17\s" tree.c.001t.tu | cut -f2 "-d " | sort | uniq -c | sort -n`

Output:
```
      1 constructor
    742 nop_expr
   1287
```

Lets look at these nops, but @17 is the value zero so ambigious.
`grep -P -e "\s@17\s" tree.c.001t.tu | grep nop_expr`
`grep -P -e "\s@17\s" tree.c.001t.tu | grep nop_expr | cut -f1 "-d " > usage_nop_of_17.txt`

`for x in `cat usage_nop_of_17.txt`; do echo $x; grep -B1  -P -e "op 2: $x\s" tree.c.001t.tu; done   | cut -f2 "-d "  | sort | uniq -c | sort -n`

There is a cond expression, presumably checking the node type
`616 cond_expr`


Lets look at one of these, @228464 that is used in op2

```
@228378 cond_expr        type: @33      op 0: @228462(gmp_u ne gmp_w)  op 1: @228463 
                         op 2: @228464
```

op0 compares two parameters.

@228462 ne_expr          type: @781     op 0: @228547(nop (param __gmp_w))  op 1: @228377(parm_decl(__gmp_u))

op0 : @228547 nop_expr         type: @144225  op 0: @228289 (param __gmp_w)

so op0 is some parameter, and op1 as well
```
@228289 parm_decl        name: @134739(__gmp_w)  type: @201199  scpe: @228202 
                         srcp: gmp.h:1877              chain: @228377 
                         lang: C        argt: @201199  size: @31     
                         algn: 64       used: 1       
```

```@228377 parm_decl        name: @139694(__gmp_u)  type: @139695  scpe: @228202 
                         srcp: gmp.h:1877              lang: C       
                         argt: @139695  size: @31      algn: 64      
                         used: 1       
```

Based on this information we find the code in tree.ii
```
# 1707 "/usr/include/x86_64-linux-gnu/gmp.h" 3 4
extern __inline__ __attribute__ ((__gnu_inline__)) void
__gmpz_abs (mpz_ptr __gmp_w, mpz_srcptr __gmp_u)
{
  if (__gmp_w != __gmp_u)
    __gmpz_set (__gmp_w, __gmp_u);
  __gmp_w->_mp_size = ((__gmp_w->_mp_size) >= 0 ? (__gmp_w->_mp_size) : -(__gmp_w->_mp_size));
}
```


Now lets look at @1367, which is the index of the type component_ref. It is not referenced.

We really want to find COMPONENT_REF which is the enum value. Lets look for that.

`@179032 identifier_node  strg: COMPONENT_REF           lngt: 13`


```@179033 const_decl       name: @179032  type: @3489    scpe: @3489   
                         srcp: tree.def:427            chain: @176838 
                         cnst: @123447```

We find another integer constant with the same value of 45 but different id.
@123447 integer_cst      type: @3489   int: 45

We find there are lots of the same number in the system :

```
mdupont@debian-build-speed:~/experiments/gcc-1/build/gcc$ grep 'int: 45$' tree.c.001t.tu
@1367   integer_cst      type: @46     int: 45
@29974  integer_cst      type: @2791   int: 45
@55341  integer_cst      type: @4703   int: 45
@64917  integer_cst      type: @235    int: 45
@81996  integer_cst      type: @3489   int: 45
@106697 integer_cst      type: @9321   int: 45
@118212 integer_cst      type: @5803   int: 45
@123447 integer_cst      type: @3489   int: 45
@179322 integer_cst      type: @9431   int: 45
@185498 integer_cst      type: @4683   int: 45
@192365 integer_cst      type: @9431   int: 45
@193492 integer_cst      type: @149164 int: 45
@194653 integer_cst      type: @13236  int: 45
@195023 integer_cst      type: @13593  int: 45
@198216 integer_cst      type: @24122  int: 45
@203817 integer_cst      type: @106913 int: 45
@207212 integer_cst      type: @83062  int: 45
@210696 integer_cst      type: @163838 int: 45
@221038 integer_cst      type: @210823 int: 45
@227640 integer_cst      type: @220968 int: 45
```

Now looking for constants of the same type 
``grep 'integer_cst' tree.c.001t.tu | grep @3489 > enum_values.txt``

gives us 404 values, so we can suppposed that not all the values of the tree type are used in this system.

We confirm this is the tree code enum
```
@3489   enumeral_type    name: @3950    size: @237     algn: 32      
                         prec: 32       sign: unsigned min : @779    
                         max : @780     csts: @3951   

@3950   type_decl        name: @4523    type: @3489    scpe: @3      
                         srcp: tree-core.h:131         note: artificial 
                         chain: @4524
@4523   identifier_node  strg: tree_code               lngt: 9       			 
```

So first finding/rule is, we want to Replace/Augment
R1. all node numbers with the names of the items if available to make reading the tree dump easier.
R2. all enum constants with the string values



```
@117292 call_expr        type: @393     fn  : @123446 (addr_expr type: @68717 op 0: (@55454  function_decl name:(build_nt) type: @61000   scpe: @3   srcp: tree.c:4668 args: @61002   link: extern   body: @61003  )  )  0   : @123447 
                         1   : @123448  2   : @123449  3   : @2816
```

```
@123632 call_expr        type: @393     fn  : (@129181 addr_expr type: @134501  op 0: (@87548  function_decl  name: (fold_build3_stat_loc) type: @45496   scpe: @3  srcp: fold-const.h:67) )  0   : @16458  
                         1   : @123447  2   : @129182  3   : @59396  
                         4   : @64987   5   : @2816
 ```

Looking at the code it seems that we can specialize many functions based on the types of nodes.
So it might make sense to evaluate each function given a types of node and generate specialized code for that one type and transform/push the switches into some vector.

Then we would generate a set of functions that operation only on one type.

We could also create an adjency graph for each field. Composing two field graphs together would be H = F + G to yield where they connect.

The domain of a field would be the type of objects that have that field + the set of fields that produce that domain.

