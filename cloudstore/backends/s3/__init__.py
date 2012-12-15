import boto
from cloudstore import Bucket, Object, CommonPrefix
from dateutil.parser import parser

class S3Assembly:
    def __init__ ( self ):
        pass

    def load_bucket ( self, bucket_boto ):
        return Bucket ( bucket_boto.name )

    def load_buckets ( self, buckets_boto ):
        return [ Bucket ( name = bucket.name, creation_date = bucket.creation_date ) for bucket in buckets_boto ]

    def load_object ( self, name, bucket, last_modified = None ):
        key = Object ( name, bucket, last_modified = parser ( ).parse ( last_modified ) )
        return key

    def load_objects ( self, bucket, objects_boto ):
        new_key = None
        objects = []
        for key in objects_boto:
            if isinstance ( key, boto.s3.key.Key ):
                new_key = self.load_object ( key.name, bucket, last_modified = key.last_modified )
            elif isinstance ( key, boto.s3.prefix.Prefix ):
                new_key = CommonPrefix ( key.name, bucket )

            objects.append ( new_key )

        return objects

class S3Adapter:
    def __init__ ( self, access_key, secret_key, location ):
        self.location = location
        self.access_key = access_key
        self.secret_key = secret_key
        self.s3 = boto.connect_s3 ( aws_access_key_id = access_key, aws_secret_access_key = secret_key )
        self.assembly = S3Assembly ( )

    def get_all_buckets ( self ):
        return self.assembly.load_buckets ( self.s3.get_all_buckets ( ) )

    def get_all_objects ( self, bucket_name, prefix="", marker = "", delimiter = "", max_keys = 1000 ):
        bucket  = boto.s3.bucket.Bucket ( self.s3, name = bucket_name )
        objects = bucket.get_all_keys ( prefix = prefix, marker = marker, delimiter = delimiter, max_keys = max_keys )
        objects = self.assembly.load_objects ( self.assembly.load_bucket ( bucket ), objects )
        objects.sort ( key = lambda k: isinstance ( k, CommonPrefix ) and -1 or 0 )

        return objects