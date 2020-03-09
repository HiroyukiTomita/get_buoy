#!/usr/bin/env python3
#
# get_buoy.py ---Buoy data download tool for QCS
#
# CHANGES:
#    V1.0.3: 2019.03.05
#    V1.0.2: 2019.01.07
#    V1.0.1: 2018.11.27
#    V1.0.0: 2016.12.01
#-------------------------------------------------- 
# IMPORT MODULES
#-------------------------------------------------- 
import sys
import os
import get_buoy_misc
import get_buoy_ftp
import get_buoy_wget

#-------------------------------------------------- 
# SCRIPT SETUP
#-------------------------------------------------- 
version="V1.0.3"
buoy_category="TAO"
buoy_id="0n110w"
buoy_year=2015

#-------------------------------------------------- 
# INIT. 
#-------------------------------------------------- 
pid = os.getpid()

#-------------------------------------------------- 
# command line arguments
#-------------------------------------------------- 
if len(sys.argv) == 1:
 get_buoy_misc.usage()
 sys.exit()
elif len(sys.argv) == 4:
 arg1 = sys.argv[1]
 arg2 = sys.argv[2]
 arg3 = sys.argv[3]
 buoy_year = 9999
elif len(sys.argv) == 5:
 arg1 = sys.argv[1]
 arg2 = sys.argv[2]
 arg3 = sys.argv[3]
 arg4 = sys.argv[4]
 buoy_year = arg4

opath = arg1
buoy_category = arg2
buoy_id = arg3

# BUOY original data directory
buoy_org_dir=opath + "/" + buoy_category + "/" 

#-------------------------------------------------- 
# set Original file
#-------------------------------------------------- 
#buoy_org_fn = get_buoy_misc.org_fn(buoy_category, buoy_id, buoy_year)
#print (buoy_org_fn)

#-------------------------------------------------- 
# Download buoy data file
#-------------------------------------------------- 
if buoy_category == "TAO" or buoy_category == "TRITON" or buoy_category == "PIRATA" or buoy_category == "RAMA" :
 if buoy_category == "TAO" or buoy_category == "PIRATA" or buoy_category == "RAMA":
   # get 10min data
   get_buoy_ftp.get10m(buoy_category, buoy_id, buoy_year, buoy_org_dir)
 get_buoy_ftp.get(buoy_category, buoy_id, buoy_year, buoy_org_dir)
 get_buoy_ftp.get_bp(buoy_category, buoy_id, buoy_year, buoy_org_dir)
elif buoy_category == "NDBC":
 get_buoy_wget.get(buoy_category, buoy_id, buoy_year, buoy_org_dir)
elif buoy_category == "OCS":
 get_buoy_wget.get(buoy_category, buoy_id, buoy_year, buoy_org_dir)

