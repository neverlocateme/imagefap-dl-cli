#!/usr/bin/python
# -*- coding: utf-8 -*-

import os.path
import sys
import config
import IFUser
import queue
import gallery
import time

version = '0.5'

def choochoochoose():
    config.LoadConfig('IFLoad.config')
    print 'ImageFap Gallery Downloader '+version
    print 'CLI fork by neverlocateme'
    try:
        testargs = sys.argv[1]
    except IndexError:
        print 'No arguments passed. Closing.'
        sys.exit(1)    
    if sys.argv[1] == '-f' and os.path.isfile(sys.argv[2]):
        filemain()
    elif sys.argv[1] == '-f' and not os.path.isfile(sys.argv[2]):
        print 'You passed the file (-f) option but the file specified does not exist. Exiting.'
        sys.exit(1)
    else:
        argmain()

### this feels dirty
def filemain():
    infile = sys.argv[2]
    listurl = []
    print 'Reading URLs from file: %s' % (infile)
    with open(infile, 'r') as nudielist:
        nudespls = [line.rstrip('\n') for line in nudielist]
        for line in nudespls:
            fileurl = line
            "'%s'" % fileurl
            listurl.append(fileurl)
        for content in listurl:
            print 'Processing URL: %s' % (content)
            queue.ProcessURL(content)
        if len(queue.queue):
            gallery.DownloadGallery()
        else:
            print 'Something broke.'
            sys.exit(1)

def argmain():    
    urlcount = len(sys.argv[1:])
    print 'Beginning to process %i URL(s)' % (urlcount)
    if len(sys.argv) != 0:
        for argurl in sys.argv[1:]:
            print 'Processing URL: %s' % (argurl)
            queue.ProcessURL(argurl)
            ### verify the URL was processed and is now queued, then run
            if len(queue.queue):
                gallery.DownloadGallery()
            else:
                ### Whoops. You done fucked up. Exit.
                print 'URL failed to process!'
                print 'URL: %s' % (argurl)
                print 'Exiting.'
                sys.exit(1)


choochoochoose()
