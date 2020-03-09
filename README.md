# get_buoy
gets surface buoy data for QCS  

## USAGE 
`get_buoy [buoy_category] [buoyid] [year]`

## Memo 
### BUOY CATEGORY
- TAO 
- TRITON 
- RAMMA 
- PIRATA 
- NDBC
- OCS (ARC, KEO, Papa)
- WHOI (Stratus, NTAS, WHOTS)
- OTHERS

### Data Provider Info.
1) NOAA PMEL: TAO/TRITON/PIRATA/RAMA  
- FTP:  ftp.pmel.noaa.gov 
- FILE: ex. met0n110w_hr.ascii  
  
2) NOAA NDBC: NDBC buoys 
- INFO: http://www.ndbc.noaa.gov/historical_data.shtml  
- WEB: http://www.ndbc.noaa.gov/data/historical/stdmet/  
- FILE: ex. 41013h2015.txt.gz  

3) NOAA PMEL: Ocean Climate Stations: ARC, KEO, Papa
- INFO: https://www.pmel.noaa.gov/ocs/
- FTP: ftp.pmel.noaa.gov
- FILE: ex. w32n145e_hr.ascii, w50n145w_hr.ascii 

4) WHOI: Ocean Reference Stations: Stratus, NTAS, WHOTS
- INFO: http://uop.whoi.edu/ReferenceDataSets/index.html
- WEB: http://uop.whoi.edu/ReferenceDataSets/stratusreference.html
- FILE: ex. OS_Stratus_200010-201007_D_MLTS-1H.nc
