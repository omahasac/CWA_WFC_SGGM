import datetime

import numpy as np

from module.draw_griddata import DrawGriddataMap
from module.load_demo import load_demo_gfe0p01d_v2

def main():
    init_date = datetime.datetime(2022, 9, 15, 12)
    lon, lat, alt = load_demo_gfe0p01d_v2()
  
    Draw_obj_1 = DrawGriddataMap()
    Draw_obj_1.put_latlon(lat, lon)
    Draw_obj_1.put_data(alt)
    Draw_obj_1.set_info('GFE', 'ALT', init_date)
    Draw_obj_1.draw('alt_demo.png', 'elevation')
    
    Draw_obj_2 = DrawGriddataMap()
    Draw_obj_2.put_latlon(lat, lon)
    Draw_obj_2.put_data(alt)
    Draw_obj_2.set_info('GFE', 'ALT', init_date)
    Draw_obj_2.mask_sea_gfe1km()
    Draw_obj_2.draw_zoom_in('alt_zoom_in_demo.png', 'elevation', draw_max_tw=True)
    
    Draw_obj_3 = DrawGriddataMap()
    Draw_obj_3.put_latlon(lat, lon)
    Draw_obj_3.put_data(alt)
    Draw_obj_3.set_info('GFE', 'ALT', init_date)
    Draw_obj_3.draw_zoom_out('alt_zoom_out_demo.png', 'elevation')
    
    
if __name__ == '__main__':
    main()