def print_header(version):
 print('---------------------')
 print(' GET_BUOY')
 print('  version', version)
 print('---------------------')

def usage():
 print('---------------------')
 print('USAGE:')
 print('  get_buoy  buoy_category  buoy_id  [year]')

def org_fn(buoy_category, buoy_id, year):
 if (buoy_category == 'TAO'):
   buoy_org_fn = 'met' + buoy_id + '_hr.ascii'
 if (buoy_category == 'NDBC'):
   buoy_org_fn = buoy_id + 'h'+ year + '.txt'
 if (buoy_category == 'OCS'):
   buoy_org_fn = '-'
 
 return(buoy_org_fn)
 
