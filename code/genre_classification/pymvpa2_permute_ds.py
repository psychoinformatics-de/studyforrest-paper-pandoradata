from mvpa2.generators.permutation import AttributePermutator
from mvpa2.mappers.zscore import zscore

def fx(ds):
    zscore(ds, chunks_attr=None)
    perm = AttributePermutator('condition', limit='chunks')
    ds = perm(ds)
    return ds
