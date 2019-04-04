def get(buoy_category, buoy_id, buoy_year, buoy_org_dir):
    import os
    import get_buoy_misc

    if (buoy_category == "NDBC"):
      buoy_org_fn = get_buoy_misc.org_fn(buoy_category, buoy_id, buoy_year)
      site = 'https://www.ndbc.noaa.gov/data/historical/stdmet/'
      file = buoy_id + 'h' + buoy_year + '.txt'
      command1 = 'wget ' + site + file + '.gz'
      command2 = 'mv ' + file + '.gz ' + buoy_org_dir
      command3 = 'gunzip ' +  buoy_org_dir + file + '.gz'
    elif (buoy_category == "OCS"):
      if buoy_id == 'KEO':
       site = 'ftp://ftp.pmel.noaa.gov/keodata/hi_res/'
       command1 = 'wget ' + '-A .ascii -r -nd ' + site
       command2 = 'mv '  + '*.ascii ' + buoy_org_dir
       command3 = ' '
      elif buoy_id == 'PAPA':
       site = 'ftp://ftp.pmel.noaa.gov/papadata/hi_res/'
       command1 = 'wget ' + '-A .ascii -r -nd ' + site
       command2 = 'mv '  + '*.ascii ' + buoy_org_dir
       command3 = ' '
    os.system(command1)
    os.system(command2)
    os.system(command3)
    

 
    
 
