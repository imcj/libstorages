import urllib
import mimetypes
import simplejson
import cloudstore
import cloudstore.qbox
import cloudstore.qbox.rs
import cloudstore.qbox.rscli
import cloudstore.qbox.uptoken
import cloudstore.qbox.digestoauth

from cloudstore import Bucket
from StringIO import StringIO
from pdb import set_trace as bp

class Adapter:
    def __init__ ( self, config ):
        self.host = config.host
        self.access_key = config.access_key
        self.secret_key = config.secret_key
        self.oss = OssAPI ( self.host, self.access_key, self.secret_key )
        self.qn = cloudstore.qbox.rs.Service (\
             cloudstore.qbox.digestoauth.Client ( ),\
             bucket )

    def create_bucket ( self, bucket ):
        self.qn.Mkbucket ( bucket )

    def delete_bucket ( self, bucket ):
        self.qn.Drop ( bucket )

    def get_all_buckets ( self ):
        return [ Bucket ( bucket ) for bucket in self.qn.Buckets ( ) ]

    def create_object ( self, bucket, key, data, file_path = None ):
        token = cloudstore.qbox.uptoken.UploadToken ( bucket ).\
                generate_token ( )

        mime_type = mimetypes.guess_type ( key )[0]

        if not mime_type:
            mime_type = 'application/octet-stream'

        if file_path:
            upload_response = cloudstore.qbox.rscli.UploadFile ( \
                bucket, key, mime_type, file_path, '', '', token )
        else:
            upload_response = cloudstore.qbox.rscli.upload_with_file ( \
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