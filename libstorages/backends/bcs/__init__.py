#! -*- encoding:utf-8 -*-

from libstorages import pybcs, Object, Bucket
from libstorages.errors import BucketNameDuplication, BucketCanNotCreate, \
ObjectNotExists
from pdb import set_trace as bp
from StringIO import StringIO

import simplejson

class BucketAssembly:
    def __init__ ( self ):
        pass

class BCSObject ( Object ):
    def __init__ ( self, bcs_object, *args, **kwargs ):
        self.bcs_object = bcs_object
        self.reading = False
        self.response = None
        super ( BCSObject, self ).__init__ ( *args, **kwargs )

    def create ( self, data ):
        self.bcs_object.put ( data )

    def create_from_buffer ( self, buff ):
        self.bcs_object.put ( buff )

    def create_from_file ( self, filepath ):
        self.bcs_object.put ( open ( filepath, 'r' ) )

    def delete ( self ):
        self.bcs_object.delete ( )

    def exists ( self ):
        pass


    def read ( self, size = None ):
        if not self.reading:
            self.reading = not self.reading
            self.response = self.bcs_object.get ( )
        
        return self.response['body'].read ( size )

class BCSBucket ( Bucket ):
    def __init__ ( self, bcs, *args, **kwargs ):
        self.bcs = bcs
        super ( BCSBucket, self ).__init__ ( *args, **kwargs )

    def create ( self ):
        raise BucketCanNotCreate ( )
        try:
            self.bcs.bucket ( self.name ).create ( )
        except pybcs.httpc.HTTPException, e:
            if 403 == e.status:
                raise BucketNameDuplication ( )

class Adapter:
    def __init__ ( self, config ):
        self.config = config
        self.bcs = pybcs.BCS ( self.config.host, self.config.access_key, \
                               self.config.secret_key, pybcs.HttplibHTTPC  )


    def create_bucket ( self, bucket ):
        return BCSBucket ( self.bcs, bucket ).create ( )

    def delete_bucket ( self, bucket ):
        self.bcs.bucket ( bucket ).delete ( )

    def get_all_buckets ( self ):
        buckets = self.bcs.list_buckets ( )
        return [\
            BCSBucket ( self.bcs, bcs_bucket.bucket_name ) for bcs_bucket \
            in buckets
        ]

    def _factory_create_object ( self, bucket, key, upload_callback = None ):
        return self.bcs.bucket ( bucket ).object ( "/" + key, upload_callback )

    def create_object ( self, bucket, key, data, upload_callback = None ):
        bcs_object = BCSObject ( \
            self._factory_create_object ( bucket, key, upload_callback ) )
        bcs_object.create ( data )

        return bcs_object

    def create_object_from_file ( self, bucket, key, file_path, \
                                  upload_callback = None ):
        return self.create_object ( bucket, key, open ( file_path, 'r' ), \
                                    upload_callback )

    def create_object_from_stream ( self, bucket, key, stream, \
                                    upload_callback = None ):
        # TODO 修改bcs的代码，使其支持 file 对象。
        self.create_object ( bucket, key, stream, upload_callback )


    def get_object ( self, bucket, key ):
        try:
            return BCSObject ( self.bcs.bucket ( bucket ) \
                   .object ( "/" + key ) )
        except pybcs.httpc.HTTPException, e:
            if 404 == e.status:
                raise ObjectNotExists ( )

    def delete_object ( self, bucket, key ):
        self._factory_create_object ( bucket, key ).delete  ( )

    def get_all_objects ( self, bucket, prefix = "", marker = "", \
                          delimiter = "", max_keys = 1000 ):
        return [ BCSObject ( bcs_object ) for bcs_object in \
            self.bcs.bucket ( bucket ).\
            list_objects ( prefix, marker, max_keys )
        ]
