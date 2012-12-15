from cloudstore.oss.oss_api import OssAPI
from cloudstore.backends.oss.assembly import OSSAssembly
from cloudstore import Bucket

class OSSAdapter:
    def __init__ ( self, access_key, secret_key, host ):
        self.host = host
        self.access_key = access_key
        self.secret_key = secret_key
        self.oss = OssAPI ( self.host, self.access_key, self.secret_key )
        self.assembly = OSSAssembly ( )

    def get_all_buckets ( self ):
        res =  self.oss.list_all_my_buckets ( )
        return self.assembly.load_buckets ( res )

    def get_all_objects ( self, bucket_name, prefix="", marker = "", delimiter = "", max_keys = 1000 ):
        res = self.oss.list_bucket ( bucket_name, prefix, marker, delimiter, max_keys )
        return self.assembly.load_objects ( Bucket ( bucket_name ), res )