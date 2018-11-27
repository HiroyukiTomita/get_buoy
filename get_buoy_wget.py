def get(buoy_category, file):
    import os
    if (buoy_category == "NDBC"):
      site = 'http://www.ndbc.noaa.gov/data/historical/stdmet/'

    command = 'wget ' + site + file + '.gz'
    os.system(command)
    

 
    
 
