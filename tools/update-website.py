#!/usr/bin/env python

import os
import sys
library_dir = os.path.abspath ( os.path.join ( \
    os.path.dirname ( os.path.abspath ( __file__ ) ), \
    ".." ) )

sys.path.insert ( 0, library_dir )

import libstorages
from pdb import set_trace as bp

build_html = os.path.abspath ( os.path.join ( \
    os.path.dirname ( os.path.abspath ( __file__ ) ), \
    "..", "docs", "build", "html" ) )

store = libstorages.env ( "s3" )

for path in os.walk ( build_html ):
    for file_path in path[2]:
        local_file = os.path.join ( path[0], file_path )
        remote_object_name = local_file [ len ( build_html ) + 1:] \
                             .replace ( "\\", "/" )

        store.create_object_from_file ( \
            "libstorages.bukaopu.us", \
            remote_object_name, \
            local_file )

        print "Upload <%s> finish." % remote_object_name