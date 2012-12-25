from cloudstore.oss.oss_api import OssAPI
from cloudstore.backends.oss.assembly import OSSAssembly
from cloudstore import Bucket
from pdb import set_trace as bp
from StringIO import StringIO

class Adapter:
    def __init__ ( self, config ):
        self.host = config.host
        self.access_key = config.access_key
        self.secret_key = config.secret_key
        self.oss = OssAPI ( self.host, self.access_key, self.secret_key )
        self.assembly = OSSAssembly ( )

    def put_object ( self, bucket, key, data ):

        if isinstance ( data, basestring ):
            data = StringIO ( data )
        return self.oss.put_object_from_fp ( bucket, key,\
            data )


    def get_all_buckets ( self ):
        res =  self.oss.list_all_my_buckets ( )
        return self.assembly.load_buckets ( res )

    def get_all_objects ( self, bucket_name, prefix="", marker = "", delimiter = "", max_keys = 1000 ):
        def filter ( keys, bucket_name, prefix = "", marker = "", delimiter = "", max_keys = 1000 ):
            new_keys = []
            prefix_len = len ( prefix )

            for key in keys:
                if key.name == prefix:
                    continue
                new_keys.append ( key )

            return new_keys
        res = self.oss.list_bucket ( bucket_name, prefix, marker, delimiter, max_keys )
        keys = self.assembly.load_objects ( Bucket ( bucket_name ), res )
        return filter ( keys, bucket_name, prefix, marker, delimiter, max_keys )