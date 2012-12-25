#!/usr/bin/env python

import os
import cloudstore

build_html = os.path.abspath ( os.path.join ( \
    os.path.dirname ( os.path.abspath ( __file__ ) ), \
    "..", "docs", "build", "html" ) )
for path in os.walk ( build_html ):
    for file_path in path[2]:
        local_file = os.path.join ( path[0], file_path )
        remote_object_name = local_file [ len ( build_html ) + 1:] \
                             .replace ( "\\", "/" )
        
        cloudstore.create_object ( \
            "cloudstore.bukaopu.us", \
            open ( remote_object_name ) )

        print "Upload <%s> finish." % remote_object_name