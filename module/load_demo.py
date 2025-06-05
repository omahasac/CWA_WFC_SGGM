import numpy as np

def load_demo_gfe0p01d_v2(ref_dir='ref'):
    lon = np.zeros(407281, 'f4').reshape(581, 701)
    lat = np.zeros(407281, 'f4').reshape(581, 701)
    alt = np.zeros(407281, 'f4').reshape(581, 701)
    tag = np.zeros(407281, 'i4').reshape(581, 701)
    gfe_info = np.load(f'{ref_dir}/GFEGridInfo_1km_Ext_OI.npz')
    lon[:] = gfe_info['lon'].reshape(581, 701)
    lat[:] = gfe_info['lat'].reshape(581, 701)
    alt[:] = gfe_info['alt'].reshape(581, 701)
    tag[:] = gfe_info['tag'].reshape(581, 701)
    return lon, lat, alt

    
