def get(buoy_category, buoy_id , buoy_year, buoy_org_dir):
    import os
    from ftplib import FTP
    import get_buoy_misc
    if (buoy_category == "TAO" or buoy_category == "TRITON" or buoy_category == "PIRATA" or buoy_category == "RAMA"):
      site = 'ftp.pmel.noaa.gov'
      user = 'taopmelftp'
      key  = 'G10b@LCh@Ng3'
      dir  = '/high_resolution/ascii/hr'
      file = get_buoy_misc.org_fn(buoy_category, buoy_id, buoy_year) 
      file = file + '.gz'
    ftps = FTP(site,user,key)
    ftps.cwd(dir)
    command='RETR '+file
    f = open(file, 'wb')
    print(command)
    ftps.retrbinary(command,f.write)
    ftps.quit()
    f.close()
# move
    command = 'mv ' + file  + ' ' + buoy_org_dir
    os.system(command)
    fileb,ext = os.path.splitext(file)
    if (ext == ".gz"):
     command = 'gunzip ' + buoy_org_dir + file
     os.system(command)

def get_bp(buoy_category, buoy_id , buoy_year, buoy_org_dir):
    import os
    from ftplib import FTP
    import get_buoy_misc
    if (buoy_category == "TAO" or buoy_category == "TRITON" or buoy_category == "PIRATA" or buoy_category == "RAMA"):
      site = 'ftp.pmel.noaa.gov'
      user = 'taopmelftp'
      key  = 'G10b@LCh@Ng3'
      dir  = '/high_resolution/ascii/hr'
      file = get_buoy_misc.org_bp_fn(buoy_category, buoy_id, buoy_year) 
      file = file + '.gz'
    ftps = FTP(site,user,key)
    ftps.cwd(dir)
    command='RETR '+file
    f = open(file, 'wb')
    print(command)
    ftps.retrbinary(command,f.write)
    ftps.quit()
    f.close()
# move
    command = 'mv ' + file  + ' ' + buoy_org_dir
    os.system(command)
    fileb,ext = os.path.splitext(file)
    if (ext == ".gz"):
     command = 'gunzip ' + buoy_org_dir + file
     os.system(command)


def get10m(buoy_category, buoy_id , buoy_year, buoy_org_dir):
    import os
    from ftplib import FTP
    import get_buoy_misc
    if (buoy_category == "TAO" or buoy_category == "TRITON" or buoy_category == "PIRATA" or buoy_category == "RAMA"):
      site = 'ftp.pmel.noaa.gov'
      user = 'taopmelftp'
      key  = 'G10b@LCh@Ng3'
      dir  = '/high_resolution/ascii/10m'
      file = get_buoy_misc.org_fn10m(buoy_category, buoy_id, buoy_year) 
      file = file + '.gz'
    ftps = FTP(site,user,key)
    ftps.cwd(dir)
    command='RETR '+file
    f = open(file, 'wb')
    print(command)
    ftps.retrbinary(command,f.write)
    ftps.quit()
    f.close()
# move
    command = 'mv ' + file  + ' ' + buoy_org_dir
    os.system(command)
    fileb,ext = os.path.splitext(file)
    if (ext == ".gz"):
     command = 'gunzip ' + buoy_org_dir + file
     os.system(command)

