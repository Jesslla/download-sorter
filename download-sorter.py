import os
import sys
import getopt
    
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
	

usersjesslla = 'c:/Users/Jesslla'
destpathprefix = 'z:/'

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hi:")
    except getopt.GetoptError:
        downloadsdir = 'c:/Users/Jesslla/Downloads'
        print "Using default directory of", downloadsdir
        
        
    for opt, arg in opts:
        if opt == '-i':
            print "Using", arg
            downloadsdir = arg
            print "Downloads dir is set to", downloadsdir
            for i in os.listdir(downloadsdir):
                z = i.split('.')
                end = z[-1]
                if end in filetypes:
                    sourcepath = os.path.join(downloadsdir, i)
                    destpath = os.path.join(destpathprefix, filetypes[end], i)
                    destdir = os.path.join(destpathprefix, filetypes[end])
                    print 'Destpath: ', destpath
                    print 'Destdir: ', destdir
                    if os.path.exists(destdir):
                        print 'Moving ', i, 'to', destdir
                        os.rename(sourcepath, destpath)
                    else:
                        print destdir, "does not exist. Creating."
                        os.mkdir(destdir)
        elif opt == '-h':
            print "Usage: download-sorter.py -i input_directory ", 
            sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])

            