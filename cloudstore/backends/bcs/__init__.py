#! -*- encoding:utf-8 -*-

from cloudstore import pybcs, Bucket
from cloudstore.errors import BucketNameDuplication, BucketCanNotCreate, \
ObjectNotExists
from pdb import set_trace as bp
from StringIO import StringIO

import simplejson

class BucketAssembly:
    def __init__ ( self ):
        pass

    def loads ( self, buckets ):
        return [ Bucket ( bucket.bucket_name ) for bucket in buckets ]

class BCSObject ( Object ):
    def __init__ ( self, config ):
        pass

class Adapter:
    def __init__ ( self, config ):
        self.config = config
        self.bcs = pybcs.BCS ( self.config.host, self.config.access_key, \
                               self.config.secret_key, pybcs.HttplibHTTPC  )
        self.bucket_assembly = BucketAssembly ( )

    def create_bucket ( self, bucket ):
        raise BucketCanNotCreate ( )
        try:
            self.bcs.bucket ( bucket ).create ( )
        except pybcs.httpc.HTTPException, e:
            if 403 == e.status:
                raise BucketNameDuplication ( )

    def delete_bucket ( self, bucket ):
        self.bcs.bucket ( bucket ).delete ( )

    def get_all_buckets ( self ):
        buckets = self.bcs.list_buckets ( )
        return self.bucket_assembly.loads ( buckets )

    def _factory_create_object ( self, bucket, key ):
        return self.bcs.bucket ( bucket ).object ( "/" + key )

    def create_object ( self, bucket, key, data ):
        self._factory_create_object ( bucket, key ).put ( data )

    def create_object_from_file ( self, bucket, key, file_path ):
        self._factory_create_object ( bucket, key ).put_file ( file_path )

    def create_object_from_stream ( self, bucket, key, stream ):
        # TODO 修改bcs的代码，使其支持 file 对象。
        self.create_object ( bucket, key, stream.read ( ) )


    def get_object ( self, bucket, key ):
        try:
            return StringIO ( self.bcs.bucket ( bucket ) \
                   .object ( "/" + key ).get ( )['body'] )
        except pybcs.httpc.HTTPException, e:
            if 404 == e.status:
                raise ObjectNotExists ( )

    def delete_object ( self, bucket, key ):
        self._factory_create_object ( bucket, key ).delete  ( )

    def get_all_objects ( self, bucket, prefix = "", marker = "", \
                          delimiter = "", max_keys = 1000 ):
        return self.bcs.bucket ( bucket ) \
            .list_objects ( prefix, marker, max_keys )
