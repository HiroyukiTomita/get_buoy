def get(buoy_category, buoy_id, buoy_year):
    import os
    import get_buoy_misc

    if (buoy_category == "NDBC"):
      buoy_org_fn = get_buoy_misc.org_fn(buoy_category, buoy_id, buoy_year)
      site = 'http://www.ndbc.noaa.gov/data/historical/stdmet/'
      command = 'wget ' + site + file + '.gz'
    elif (buoy_category == "OCS"):
      if buoy_id == 'KEO':
       site = 'ftp://ftp.pmel.noaa.gov/keodata/hi_res/'
       command = 'wget ' + '-A .ascii -r -nd ' + site
      elif buoy_id == 'PAPA':
       site = 'ftp://ftp.pmel.noaa.gov/papadata/hi_res/'
       command = 'wget ' + '-A .ascii -r -nd ' + site
    os.system(command)
    

 
    
 
