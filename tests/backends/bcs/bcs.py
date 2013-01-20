#! -*- encoding: utf-8 -*-

__doc__="""
>>> from libstorages import env, Storage, BUCKET_PUBLIC, TEST_BUCKET_CREATE
>>> from StringIO import StringIO
>>> from pdb import set_trace as bp 
>>> import time
>>> import datetime
>>> import tempfile
>>> import os
>>> storage = env ( "bcs" )
>>> isinstance ( storage, Storage )
True
>>> loaded = []
>>> total  = 0
>>> def upload_callback  ( l, t ):
...     global loaded
...     global total
...     loaded.append ( l )
...     total = t
>>> expires = time.strftime ( \
"%a, %d %b %Y %H:%M:%S +0000", time.gmtime ( time.time ( ) + \
datetime.timedelta ( days = 5 ).total_seconds ( ) ) )
>>> storage.create_key ( BUCKET_PUBLIC, "hello", "hello, world!!!", \
upload_callback = upload_callback, content_type = "application/json", \
metadata = { "test" : "hello", "l": 0 }, expires = expires )
<Key: hello>
>>> total
15
>>> loaded
[15]
>>> hello = storage.get_key ( BUCKET_PUBLIC, "hello" )
>>> hello.content_type
'application/json'
>>> hello.metadata['crc32'] > 1
True
>>> hello.etag == hello.md5 and len ( hello.md5 ) == 32
True
>>> hello.read ( 10 )
'hello, wor'
>>> hello.read ( 10 )
'ld!!!'
>>> storage.create_key ( BUCKET_PUBLIC, "hello2", \
StringIO ( "hello, world!!!" ) )
<Key: hello2>
>>> temp = tempfile.NamedTemporaryFile ( )
>>> temp.file.write ( "hello, world!!!" )
>>> temp.file.close ( )
>>> storage.create_key_from_file ( BUCKET_PUBLIC, "hello3", \
temp.name )
<Key: hello3>
>>> storage.create_bucket ( TEST_BUCKET_CREATE )
Traceback (most recent call last):
    ...
BucketCanNotCreate
>>> storage.get_all_buckets ( )
[<Bucket: libstorages-cj-private>, <Bucket: libstorages-cj-public>, \
<Bucket: cloudstore-test-create>, <Bucket: bukaopu2>, <Bucket: bukaopu>]
>>> keys = storage.get_keys ( BUCKET_PUBLIC )
>>> keys
[<Key: hello3>, <Key: hello2>, <Key: hello>]
>>> keys[0].read ( 5 )
'hello'
"""

