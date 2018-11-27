#!/usr/bin/env python3
#
# get_buoy.py ---Buoy data download tool for QCS
#
# CHANGES:
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
version="V1.0.1"
buoy_category="TAO"
buoy_id="0n110w"
buoy_year=2015

# Home directory
get_buoy_home="../"

# BUOY original data directory
buoy_org_dir="../ORG/" + buoy_category + "/" 

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
elif len(sys.argv) == 3:
 arg1 = sys.argv[1]
 arg2 = sys.argv[2]
 buoy_year = 9999
elif len(sys.argv) == 4:
 arg1 = sys.argv[1]
 arg2 = sys.argv[2]
 arg3 = sys.argv[3]
 buoy_year = arg3

buoy_category = arg1
buoy_id = arg2

if len(sys.argv) == 4:
 buoy_year = arg3

#-------------------------------------------------- 
# set Original file
#-------------------------------------------------- 
#buoy_org_fn = get_buoy_misc.org_fn(buoy_category, buoy_id, buoy_year)
#print (buoy_org_fn)

#-------------------------------------------------- 
# Download buoy data file
#-------------------------------------------------- 
if (buoy_category == "TAO") or (buoy_category == "TRITON") or (buoy_category == "PIRATA") or (buoy_category == "RAMMA"):
 get_buoy_ftp.get(buoy_category, buoy_id, buoy_year)
elif buoy_category == "NDBC":
 get_buoy_wget.get(buoy_category, buoy_id, buoy_year)
elif buoy_category == "OCS":
 get_buoy_wget.get(buoy_category, buoy_id, buoy_year)
