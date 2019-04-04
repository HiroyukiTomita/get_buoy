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
 if (buoy_category == 'TAO' or buoy_category == 'TRITON' or buoy_category == 'PIRATA' or buoy_category == 'RAMA'):
   buoy_org_fn = 'met' + buoy_id + '_hr.ascii'
 if (buoy_category == 'NDBC'):
   buoy_org_fn = buoy_id + 'h'+ year + '.txt'
 if (buoy_category == 'OCS'):
   buoy_org_fn = '-'
 return(buoy_org_fn)

def org_bp_fn(buoy_category, buoy_id, year):
 if (buoy_category == 'TAO' or buoy_category == 'TRITON' or buoy_category == 'PIRATA' or buoy_category == 'RAMA'):
   buoy_org_fn = 'bp' + buoy_id + '_hr.ascii'
 if (buoy_category == 'NDBC'):
   buoy_org_fn = buoy_id + 'h'+ year + '.txt'
 if (buoy_category == 'OCS'):
   buoy_org_fn = '-'
 return(buoy_org_fn)

def org_fn10m(buoy_category, buoy_id, year):
 if (buoy_category == 'TAO' or buoy_category == 'TRITON' or buoy_category == 'PIRATA' or buoy_category == 'RAMA'):
   buoy_org_fn = 'met' + buoy_id + '_10m.ascii'
 if (buoy_category == 'NDBC'):
   buoy_org_fn = buoy_id + 'h'+ year + '.txt'
 if (buoy_category == 'OCS'):
   buoy_org_fn = '-'
 return(buoy_org_fn)

