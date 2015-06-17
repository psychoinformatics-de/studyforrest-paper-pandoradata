from mvpa2.mappers.zscore import zscore

def fx(ds):
    zscore(ds, chunks_attr=None)
    return ds
