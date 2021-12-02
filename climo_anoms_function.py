def climo(ds):
    ds_climo = ds.groupby('time.month').mean(dim='time')
    return ds_climo
def anoms(ds):
    ds_climo= ds.groupby('time.month').mean(dim='time')
    ds_anoms = ds.groupby('time.month')-ds_climo
    return ds_anoms
