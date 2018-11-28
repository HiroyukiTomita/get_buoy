def get(buoy_category, file, year):
    from ftplib import FTP
    if (buoy_category == "TAO"):
      site = 'ftp.pmel.noaa.gov'
      user = 'your_user_id'
      key  = 'your_pass'
      dir  = '/high_resolution/ascii/hr'
    ftps = FTP(site,user,key)
    ftps.cwd(dir)
#    ftps.retrlines('LIST') 
    command='RETR '+file+'.gz'
    f = open(file+'.gz', 'wb')
    print(command)
    ftps.retrbinary(command,f.write)
    ftps.quit()
    f.close()
 
    
 
