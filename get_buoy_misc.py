def print_header(version):
 print('---------------------')
 print(' GET_BUOY')
 print('  version', version)
 print('---------------------')

def org_fn(buoy_category, buoy_id):
 if (buoy_category == 'TAO'):
   buoy_org_fn = 'met' + buoy_id + '_hr.ascii'
   return(buoy_org_fn)
 
