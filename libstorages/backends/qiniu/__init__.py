import urllib
import mimetypes
import simplejson
import libstorages
import libstorages.qbox
import libstorages.qbox.rs
import libstorages.qbox.rscli
import libstorages.qbox.uptoken
import libstorages.qbox.digestoauth

from libstorages import Bucket
from StringIO import StringIO
from pdb import set_trace as bp

class QINIUStorage:
    def __init__ ( self, config ):
        self.host = config.host
        self.access_key = config.access_key
        self.secret_key = config.secret_key
        self.oss = OssAPI ( self.host, self.access_key, self.secret_key )
        self.qn = libstorages.qbox.rs.Service (\
             libstorages.qbox.digestoauth.Client ( ),\
             bucket )

    def create_bucket ( self, bucket ):
        self.qn.Mkbucket ( bucket )

    def delete_bucket ( self, bucket ):
        self.qn.Drop ( bucket )

    def get_all_buckets ( self ):
        return [ Bucket ( bucket ) for bucket in self.qn.Buckets ( ) ]

    def create_object ( self, bucket, key, data, file_path = None ):
        token = libstorages.qbox.uptoken.UploadToken ( bucket ).\
                generate_token ( )

        mime_type = mimetypes.guess_type ( key )[0]

        if not mime_type:
            mime_type = 'application/octet-stream'

        if file_path:
            upload_response = libstorages.qbox.rscli.UploadFile ( \
                bucket, key, mime_type, file_path, '', '', token )
        else:
            upload_response = libstorages.qbox.rscli.upload_with_file ( \
                bucket, key, mime_type, \
                StringIO ( data ), '', '', token )
        
    def create_object_from_file ( self, bucket, key, file_path ):
        self.create_object ( self, bucket, key, None, file_path )

    def delete_object ( self, key ):
        self.qn.Delete ( key )

    def get_object ( self, bucket, key ):
        self.qn.Bucketname = bucket
        info = self.qn.Stat ( key, key )
        return urllib.urlopen ( info )

    def get_all_objects ( self, bucket_name, prefix="", marker = "",\
                          delimiter = "", max_keys = 1000 ):
        return []
