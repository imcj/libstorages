#! -*- encoding:utf-8 -*-

from libstorages import pybcs, Key, Bucket, Storage, KeyList
from libstorages.errors import BucketNameDuplication, BucketCanNotCreate, \
ObjectNotExists
from libstorages.pybcs.httpc import HTTPException
from pdb import set_trace as bp
from StringIO import StringIO

import simplejson

class BucketAssembly:
    def __init__ ( self ):
        pass

class BCSKey ( Key ):
    def __init__ ( self, bcs_object, *args, **kwargs ):
        self.bcs_object = bcs_object
        self.reading = False
        self.response = None

        if not kwargs.has_key ( "name" ):
            kwargs['name'] = self.bcs_object.object_name
        super ( BCSKey, self ).__init__ ( *args, **kwargs )

    def create ( self, data ):
        self.bcs_object.put ( data )

    def create_from_buffer ( self, buff ):
        self.bcs_object.put ( buff )

    def create_from_file ( self, filepath ):
        self.bcs_object.put ( open ( filepath, 'r' ) )

    def delete ( self ):
        try:
            self.bcs_object.delete ( )
            return true
        except HTTPException, e:
            if 404 == e.status:
                raise ObjectNotExists ( self.name[1:] )

    def exists ( self ):
        pass

    def read ( self, size = None ):
        if not self.reading:
            self.reading = not self.reading
            try:
                self.response = self.bcs_object.get ( )
            except HTTPException, e:
                if 404 == e.status:
                    raise ObjectNotExists ( self.name[1:] )
        
        return self.response['body'].read ( size )

    def __repr__ ( self ):
        return "<Key: %s>" % self.name[1:]

class BCSBucket ( Bucket ):
    def __init__ ( self, bcs, *args, **kwargs ):
        self.bcs = bcs
        super ( BCSBucket, self ).__init__ ( *args, **kwargs )

    def get_key ( self, key ):
        return BCSKey ( )

    def create ( self ):
        raise BucketCanNotCreate ( )

class BCSStorage ( Storage ):
    def __init__ ( self, config ):
        self.config = config
        self.bcs = pybcs.BCS ( self.config.host, self.config.access_key, \
                               self.config.secret_key, pybcs.HttplibHTTPC  )

    def _factory_create_bucket ( self, bucket ):
        return BCSBucket ( self.bcs, bucket )

     def _factory_create_key ( self, bucket, key, upload_callback = None ):
        return BCSKey ( self.bcs.bucket ( bucket ).object ( "/" + key, upload_callback ) )

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

    def create_key ( self, bucket, key, data, upload_callback = None ):
        bcs_object = BCSKey ( \
            self._factory_create_key ( bucket, key, upload_callback ) )
        bcs_object.create ( data )

        return bcs_object

    def create_key_from_file ( self, bucket, key, file_path, \
                                  upload_callback = None ):
        return self.create_key ( bucket, key, open ( file_path, 'r' ), \
                                    upload_callback )

    def create_key_from_stream ( self, bucket, key, stream, \
                                    upload_callback = None ):
        # TODO 修改bcs的代码，使其支持 file 对象。
        self.create_object ( bucket, key, stream, upload_callback )


    def get_key ( self, bucket, key ):
        try:
            return BCSKey ( self.bcs.bucket ( bucket ) \
                   .object ( "/" + key ) )
        except pybcs.httpc.HTTPException, e:
            if 404 == e.status:
                raise ObjectNotExists ( )

    def delete_key ( self, bucket, key ):
        self._factory_create_key ( bucket, key ).delete  ( )

    def get_all_key ( self, bucket, prefix = "", marker = "", \
                      delimiter = "", max_keys = 1000 ):
        keys = [ BCSKey ( bcs_object ) for bcs_object in \
            self.bcs.bucket ( bucket ).\
            list_objects ( prefix, marker, max_keys )
        ]
        keys.sort ( )
        keys = KeyList ( keys, marker )
        return keys
