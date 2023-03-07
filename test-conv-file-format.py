import mritopng
import os

# mritopng.convert_file('C:\\data\\knuch-wrongct\\7119\\FILE0000.dcm', 'C:\\data\\tmp\\FILE0000.png')

# mritopng.convert_file('C:\data\knuch-wrongct\7119\FILE0000.dcm', 'C:\data\tmp\FILE0000.dcm')
targetdir = 'c:\\data\\tmp\\7119'
# targetdir = 'c:\\data\\tmp'

#if not os.path.exists(  targetdir ):
#   os.mkdir ( targetdir ) # , exist_ok=True )

mritopng.convert_folder('C:\\data\\knuch-wrongct\\7119', targetdir )

