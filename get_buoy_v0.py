#!/usr/bin/env python3
#
# get_buoy.py ---Buoy data download tool for QCS
#
# CHANGES:
#    V1.0.0: 2016.12.01
#-------------------------------------------------- 
# IMPORT MODULES
#-------------------------------------------------- 
import sys
import os
import get_buoy_misc
import get_buoy_ftp

#-------------------------------------------------- 
# SCRIPT SETUP
#-------------------------------------------------- 
version="V1.0.0"
buoy_category="TAO"
buoy_id=input(">>")

# Home directory
get_buoy_home="../"

# BUOY original data directory
buoy_org_dir="../ORG/" + buoy_category + "/" 

#-------------------------------------------------- 
# INIT. 
#-------------------------------------------------- 
pid = os.getpid()

#-------------------------------------------------- 
# set Original file
#-------------------------------------------------- 
buoy_org_fn = get_buoy_misc.org_fn(buoy_category, buoy_id)
print (buoy_org_fn)

#-------------------------------------------------- 
# FTP
#-------------------------------------------------- 
get_buoy_ftp.get(buoy_category, buoy_org_fn)

