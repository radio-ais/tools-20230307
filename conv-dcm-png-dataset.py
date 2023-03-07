import glob
import sys , getopt
import mritopng
import re
from pathlib import Path
import os

def get_paientid_from_filename (  filename , rootpathname ) : 
  tmp = filename.replace ( rootpathname , '' )
#  re.sub( pattern, replacement, string, count=0, flags=0)
  tmp = re.sub( '^/+', '', tmp ) # , count=0, flags=0
  atkns = tmp.split ( '/')
  return atkns[ 0 ]

def main ( argv ):
  FILENAME = argv[ 0 ]
  try :
    opts ,_ = getopt.getopt ( argv [ 1: ] , 's:t:' , [ 'srcrootdir=','targetrootdir=' ] )
  except getopt.GetoptError :
    print ( 'err')
    sys.exit(2)
  srcrootdir = ''
  targetrootdir = ''
  for opt , arg in opts :
    if opt in ( '--srcrootdir' ) :
      srcrootdir = arg
    elif opt in ( '--targetrootdir' ) :
      targetrootdir = arg

  if len( srcrootdir )<1 or len (targetrootdir) < 1 :
    print ( 'syntax : ' , FILENAME, '--srcrootdir' , '[srcrootdir]' , '--targetrootdir', '[targetrootdir]' )    
    sys.exit( 2 )

  targetrootdir = re.sub ( '/+$' , '' , targetrootdir )
  targetrootdir = re.sub ( '\+$' , '' , targetrootdir )

  print ( 'srcrootdir' , srcrootdir , 'targetrootdir' , targetrootdir ) 
  if ( os.path.exists ( srcrootdir ) ): 
    pass
  else :
    print ( 'srcrootdir non existent!!!' , srcrootdir)  
    sys.exit( 2 )

  n_files_processed = 0
  for srcfilename in glob.iglob ( srcrootdir + '**\*.dcm' , recursive=True ) :
    patientid = get_paientid_from_filename ( srcfilename , srcrootdir ) 
    filenamebase = Path( srcfilename ).stem
    targetsubdir = targetrootdir + '/' + patientid

    n_files_processed = 1 + n_files_processed
    print ( n_files_processed , srcfilename , targetfilename )
    continue

    Path( targetsubdir ).mkdir(parents=True, exist_ok=True)
    targetfilename = targetsubdir + '/' + filenamebase + '.png'
    mritopng.convert_file( srcfilename , targetfilename )
    n_files_processed = 1 + n_files_processed
    print ( n_files_processed , srcfilename , targetfilename )

#    mritopng.convert_file('/home/user/DICOM/SCAN1', '/home/user/output.png', auto_contrast=True)

if __name__ == '__main__' : 
  main ( sys.argv )

# root_dir needs a trailing slash (i.e. /root/dir/)
# rootdir = 'C:\\data\\knuch-wrongct\\'
# i = 0
# for filename in glob.iglob ( rootdir + '**/*.dcm', recursive=True):
#   i = i + 1
#   print( i , filename )

# import os

# rootdir = 'C:\\data\\knuch-wrongct'
# for root, subdirs, files in os.walk(rootdir):
#   print ( files )

