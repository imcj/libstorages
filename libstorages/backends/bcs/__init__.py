#! -*- encoding:utf-8 -*-
import logging
logging.getLogger ( "pyhttpclient" ).setLevel ( logging.CRITICAL )

from libstorages import pybcs, Key, Bucket, Storage, KeyList
from libstorages.errors import BucketNameDuplication, BucketCanNotCreate, \
ObjectNotExists
from libstorages.pybcs.httpc import HTTPException
from pdb import set_trace as bp
from StringIO import StringIO

import time
import datetime
import simplejson

class BucketAssembly:
    def __init__ ( self ):
        pass

class BCSKey ( Key ):
    def __init__ ( self, bcs_object, *args, **kwargs ):
        self.bcs_object = bcs_object
        self.reading  = False
        self.loaded   = 0
        self.response = None

        if not kwargs.has_key ( "name" ):
            kwargs['name'] = self.bcs_object.object_name
        super ( BCSKey, self ).__init__ ( *args, **kwargs )

    def create ( self, data, content_type = None, \
                       metadata = None, expires = None, \
                       upload_callback = None ):

        content_type = not content_type and "binary/octet-stream"
        # TODO expires是否是格式正确的GMT时间
        header = { "Content-Type": content_type }
        if expires:
            header['Expires'] = expires
        
        if metadata:
            for metadata in metadata:
                try:
                    header['x-bcs-meta-%s' % metadata['key']] = \
                    metadata['value']
                except KeyError:
                    pass

        self.bcs_object.put ( data, header )

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

    def _parse_datetime ( self, baidu_datetime ):
        return datetime.datetime.strptime ( baidu_datetime, \
                                            "%a, %d %b %Y %H:%M:%S GMT" )

    def _parse_header ( self, header ):
        self.header = header
        self.content_type = self.header['content-type']
        self.size = int ( self.header['content-length'] )
        self.last_modified = self._parse_datetime ( \
            self.header['last-modified'] )
        self.etag = self.header['etag']
        self.md5  = self.header['content-md5']
        self.expires = self._parse_datetime ( self.header['expires'] )

        for key in self.header.keys ( ):
            try:
                if not 'x-bs-meta-' == key[:10]:
                    continue
                short_key = key[10:]
                if short_key == "crc32":
                    value = int ( self.header[key] )
                else:
                    value = self.header[key]

                self.meta[short_key] = value

            except ValueError:
                continue


    def read ( self, size = None ):
        if not self.reading:
            try:
                self.response = self.bcs_object.get ( )
                self.reading = True
                self._parse_header ( self.response['header'] )

            except HTTPException, e:
                if 404 == e.status:
                    raise ObjectNotExists ( self.name[1:] )

        size = not size and self.size or size
        self.loaded += size

        if not self.loaded < self.size:
            self.reading = False
            self.loaded  = 0

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
        return BCSKey ( self.bcs.bucket ( bucket ).object ( "/" + \
            key, upload_callback ) )

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

    def create_key ( self, bucket, key, data, content_type = None, \
                     metadata = None, expires = None, \
                     upload_callback = None ):
        bcs_object = self._factory_create_key ( bucket, key, upload_callback ) 
        bcs_object.create ( data )

        return bcs_object

    def create_key_from_file ( self, bucket, key, file_path, content_type = \
                               None, metadata = None, expires = None, \
                               upload_callback = None ):
        return self.create_key ( bucket, key, open ( file_path, 'r' ), \
                                    upload_callback )

    def create_key_from_stream ( self, bucket, key, content_type = None, \
                                 metadata = None, expires = None, \
                                 upload_callback = None ):
        # TODO 修改bcs的代码，使其支持 file 对象。
        self.create_key ( bucket, key, stream, upload_callback )


    def get_key ( self, bucket, key ):
        try:
            key = BCSKey ( self.bcs.bucket ( bucket ).object ( "/" + key ) )
            key.read ( 0 )
            return key
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
