import os
import sys
import getopt
import shutil
import stat

# These files will be sorted into new directories. 
filetypes = {
    'pat' : '9 - Cross Stitch Patterns',
    'torrent': '2 - Documents/Torrents', 
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
                
    for sourcedir in sourcedirs:
        process_dir(sourcedir)
        
def colorize_string(color, string_to_color):
    return "%s%s%s" % (color, string_to_color, neutral)

    
def process_subdir(subdir):
    print "Subdir is: %s" % (subdir)
    for subdir_item in os.listdir(subdir):
        subdir_filename_fields = subdir_item.split('.')
        subdir_filename_extension = subdir_filename_fields[-1]
        print "subdir, subdir_item = %s" % (os.path.join(subdir, subdir_item))
        if os.path.isdir(os.path.join(subdir, subdir_item)):
            continue
        if subdir_filename_extension not in filetypes:
            print "Extension Unknown"
            continue
        destpath = os.path.join(destpathprefix, filetypes[subdir_filename_extension], os.path.basename(subdir))
     
        
        print "Destpath = %s" % (destpath)
        target_attempt_number = 0
        orig_destpath = destpath
        while( os.path.isdir(destpath)):
            target_attempt_number += 1
            destpath = orig_destpath+'-%s' % (target_attempt_number)
            print 'File %s exists. Renaming %s to %s' % (colorize_string(green, destpath), colorize_string(yellow, subdir), colorize_string(yellow, destpath))
        shutil.copytree(subdir, destpath)
        break
            
def process_dir(input_dir):
    downloadsdir = input_dir
    print "%s %s" % (colorize_string(red, 'Using'), downloadsdir)
    for dir_item in os.listdir(downloadsdir):
        if os.path.isdir(os.path.join(downloadsdir, dir_item)):
            process_subdir(os.path.join(input_dir, dir_item))
        else:
            filename_fields = dir_item.split('.')
            dir_item_extension = filename_fields[-1]
            if not dir_item_extension in filetypes:
                continue
            sourcepath = os.path.join(downloadsdir, dir_item)
            destpath = os.path.join(destpathprefix, filetypes[dir_item_extension], dir_item)
            destdir = os.path.join(destpathprefix, filetypes[dir_item_extension])
            
            print  '%s %s' % (colorize_string(purple, 'Destpath'), destpath)
            print  '%s %s' % (colorize_string(purple, destdir), destdir)
            
            if not os.path.exists(destdir):
                print "%s does not exist. Creating. %s" % (colorize_string(red, destdir), destdir)
                os.mkdir(destdir)
            target_attempt_number = 0
            orig_destpath = destpath
            while( os.path.isfile(destpath)):
                target_attempt_number += 1
                split_destpath = orig_destpath.split('.')
                destpath = '.'.join(split_destpath[:-1])+'-%s' % (target_attempt_number)+'.%s' % (split_destpath[-1])
                print 'DEBUG: ', filename_fields
                print 'File %s exists. Renaming %s to %s' % (colorize_string(green, destpath), colorize_string(yellow, dir_item), colorize_string(yellow, destpath))
            print 'Moving %s to %s' % (colorize_string(yellow, destpath), colorize_string(yellow, destdir))
            os.rename(sourcepath, destpath)

def usage():
    print '%s %s -i input_directory' % (colorize_string(purple, 'Usage:'), sys.argv[0])
            
if __name__ == "__main__":
    main()

            