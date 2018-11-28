def get(buoy_category, buoy_id , buoy_year):
    from ftplib import FTP
    import get_buoy_misc
    if (buoy_category == "TAO"):
      site = 'ftp.pmel.noaa.gov'
      user = 'your_user_id'
      key  = 'your_pass'
      dir  = '/high_resolution/ascii/hr'
      file = get_buoy_misc.org_fn(buoy_category, buoy_id, buoy_year) 
    ftps = FTP(site,user,key)
    ftps.cwd(dir)
#    ftps.retrlines('LIST') 
    command='RETR '+file+'.gz'
    f = open(file+'.gz', 'wb')
    print(command)
    ftps.retrbinary(command,f.write)
    ftps.quit()
    f.close()
 
    
 
