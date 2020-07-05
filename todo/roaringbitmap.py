from pyroaring import BitMap
bm1 = BitMap()
bm1.add(5)
bm1.add(1)
bm2 = BitMap([3,8,9])
print("bm1       = %s" % bm1)
print("bm2       = %s" % bm2)
print("bm1 & bm2 = %s" % (bm1&bm2))
print("bm1 | bm2 = %s" % (bm1|bm2))

how to encode from columns of tag1, tag2, tag3, ..., tag 10
down to 1, 0, 0, ..., 0 (2^10 bit)
to binary? 1000100000   (10 bit)
and then BitMap?
then can look at BitMap columns of binary?