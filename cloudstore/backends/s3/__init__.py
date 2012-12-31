import boto
import boto.s3.connection
from cloudstore import Bucket, Object, CommonPrefix
from dateutil.parser import parser
from pdb import set_trace as bp

class S3Assembly:
    def __init__ ( self ):
        pass

    def load_bucket ( self, bucket_boto ):
        return Bucket ( bucket_boto.name )

    def load_buckets ( self, buckets_boto ):
        return [ Bucket ( name = bucket.name, creation_date = bucket.creation_date ) for bucket in buckets_boto ]

    # TODO 
    def load_object ( self, name, bucket, size = 0, last_modified = None ):
        key = Object ( name, bucket, size = size, last_modified = parser ( ).parse ( last_modified ) )
        return key

    def load_objects ( self, bucket, objects_boto ):
        new_key = None
        objects = []
        for key in objects_boto:
            if isinstance ( key, boto.s3.key.Key ):
                new_key = self.load_object ( key.name, bucket, size = key.size, last_modified = key.last_modified )
            elif isinstance ( key, boto.s3.prefix.Prefix ):
                new_key = CommonPrefix ( key.name, bucket )

            objects.append ( new_key )

        return objects

class Adapter:
    def __init__ ( self, config ):
        self.location = config.location
        self.access_key = config.access_key
        self.secret_key = config.secret_key
        self.s3 = boto.connect_s3 ( \
            aws_access_key_id = self.access_key, \
            aws_secret_access_key = self.secret_key, \
        )
        self.assembly = S3Assembly ( )

    def get_all_buckets ( self ):
        return self.assembly.load_buckets ( self.s3.get_all_buckets ( ) )

    def get_all_objects ( self, bucket_name, prefix="", marker = "", delimiter = "", max_keys = 1000 ):
        bucket  = boto.s3.bucket.Bucket ( self.s3, name = bucket_name )
        objects = bucket.get_all_keys ( prefix = prefix, marker = marker, delimiter = delimiter, max_keys = max_keys )
        objects = self.assembly.load_objects ( self.assembly.load_bucket ( bucket ), objects )
        objects.sort ( key = lambda k: isinstance ( k, CommonPrefix ) and -1 or 0 )

        return objects

    def _factry_create_object ( self, bucket, key ):       
        remote = boto.s3.key.Key (
            boto.s3.bucket.Bucket ( self.s3, bucket ),
            key )

        return remote

    def create_object ( self, bucket, key, data ):
        remote = self._factry_create_object ( bucket, key )
        remote.set_content_from_string ( data )

    def create_object_from_stream ( self, bucket, key, data ):
        remote = self._factry_create_object ( bucket, key )
        remote.set_contents_from_file ( data )

    def create_object_from_file ( self, bucket, key, file_path ):
        remote = self._factry_create_object ( bucket, key )
        remote.set_contents_from_filename ( file_path )