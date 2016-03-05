import os
import sys
import getopt

# These files will be sorted into new directories. 
filetypes = {
    'pat' : '9 - Cross Stitch Patterns',
    'torrent': 'Documents/Torrents', 
    'jpg': '5 - Pictures/jpgs',
	'png': '5 - Pictures/pngs',
	'gif': '5 - Pictures/gifs',
	'zip': 'Zips',
	'doc': '2 - Documents/docs',
	'xls': '2 - Documents/xls',
    'xlsx': '2 - Documents/xls',
	'pdf': '2 - Documents/pdfs',
	'docx': '2 - Documents/docs',
	'epub': '2 - Documents/epub',
	'html' : '2 - Documents/html',
	'csv' : '2 - Documents/xls',
	'exe' : '3 - Software',
	'JPG' : '5 - Pictures/jpgs',
	'PNG' : '5 - Pictures/pngs',
    'txt' : '2 - Documents/txt',
	}
	
# This is the destination path
destpathprefix = 'z:/'

# Colors for printing outputs
red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
light_purple = '\033[94m'
purple = '\033[95m'
neutral = '\033[0m'

def main():
     
    sourcedirs = []
    
    for arg in sys.argv[1:]:
        if arg == '-h' or arg == '--help':
            usage()
            sys.exit(1)
        else:
            sourcedirs.append(arg)
    if 1 > len( sourcedirs ):
        sourcedirs = [ 'c:/Users/Jesslla/Downloads' ]
    print "DEBUG: sourcedirs: %s" % ( repr( sourcedirs ))
            
    for sourcedir in sourcedirs:
        process_dir(sourcedir)
        
def process_dir(input_dir):
    downloadsdir = input_dir
    print red, "Using", neutral, downloadsdir
    for dir_item in os.listdir(downloadsdir):
        filename_fields = dir_item.split('.')
        dir_item_extension = filename_fields[-1]
        if not dir_item_extension in filetypes:
            continue
        sourcepath = os.path.join(downloadsdir, dir_item)
        destpath = os.path.join(destpathprefix, filetypes[dir_item_extension], dir_item)
        destdir = os.path.join(destpathprefix, filetypes[dir_item_extension])
        print purple, 'Destpath: ', neutral, destpath
        print purple, 'Destdir: ', neutral, destdir
        if not os.path.exists(destdir):
            print destdir, "\033[92mdoes not exist. Creating.\033[0m"
            os.mkdir(destdir)
        target_attempt_number = 0
        orig_destpath = destpath
        while( os.path.isfile(destpath)):
            target_attempt_number += 1
            split_destpath = orig_destpath.split('.')
            destpath = '.'.join(split_destpath[:-1])+'-%s' % (target_attempt_number)+'.%s' % (split_destpath[-1])
            print 'DEBUG: ', filename_fields
            print 'File', green, orig_destpath, neutral, 'exists. Renaming ', green, dir_item, neutral, 'to ', yellow, destpath, neutral
        print 'Moving', yellow, destpath, neutral, 'to', yellow, destdir, neutral
        os.rename(sourcepath, destpath)

def usage():
    print red, 'Usage:', yellow, "%s -i input_directory" % (sys.argv[0]), neutral
            
if __name__ == "__main__":
    main()

            