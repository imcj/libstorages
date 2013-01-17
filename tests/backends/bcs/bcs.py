#! -*- encoding: utf-8 -*-

__doc__="""
>>> from libstorages import env, Storage, BUCKET_PUBLIC, TEST_BUCKET_CREATE
>>> from StringIO import StringIO
>>> from pdb import set_trace as bp 
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
>>> storage.create_key ( BUCKET_PUBLIC, "hello", "hello, world!!!", \
upload_callback = upload_callback )
<Key: hello>
>>> total
15
>>> loaded
[15]
>>> storage.create_key ( BUCKET_PUBLIC, "hello2", \
StringIO ( "hello, world!!!" ) )
<Key: hello2>
>>> temp = tempfile.NamedTemporaryFile ( )
>>> temp.file.write ( "hello, world!!!" )
>>> temp.file.close ( )
>>> storage.create_key_from_file ( BUCKET_PUBLIC, "hello3", \
temp.name )
<Key: hello3>
>>> hello = storage.get_key ( BUCKET_PUBLIC, "hello" )
>>> hello.read ( 10 )
'hello, wor'
>>> hello.read ( 10 )
'ld!!!'
>>> storage.get_key ( BUCKET_PUBLIC, "hello2" ).read ( )
'hello, world!!!'
>>> storage.get_key ( BUCKET_PUBLIC, "hello3" ).read ( )
'hello, world!!!'
>>> storage.create_bucket ( TEST_BUCKET_CREATE )
Traceback (most recent call last):
    ...
BucketCanNotCreate
>>> storage.get_all_buckets ( )
[<Bucket: libstorages-cj-private>, <Bucket: libstorages-cj-public>, \
<Bucket: cloudstore-test-create>, <Bucket: bukaopu2>, <Bucket: bukaopu>]
>>> keys = storage.get_all_key ( BUCKET_PUBLIC )
>>> keys
[<Key: hello>, <Key: hello2>, <Key: hello3>]
>>> keys[0].read ( 5 )
'hello'
"""

