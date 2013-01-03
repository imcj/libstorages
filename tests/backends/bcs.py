#! -*- encoding: utf-8 -*-

__doc__="""
>>> from libstorages import env, Store, BUCKET_PUBLIC, TEST_BUCKET_CREATE
>>> from StringIO import StringIO
>>> from pdb import set_trace as bp 
>>> import tempfile
>>> import os
>>> store = env ( "bcs" )
>>> isinstance ( store, Store )
True
>>> loaded = []
>>> total  = 0
>>> def upload_callback  ( l, t ):
...     global loaded
...     global total
...     loaded.append ( l )
...     total = t
>>> store.create_object ( BUCKET_PUBLIC, "hello", "hello, world!!!", \
upload_callback = upload_callback )
>>> total
15
>>> loaded
[15]
>>> store.create_object ( BUCKET_PUBLIC, "hello2", \
StringIO ( "hello, world!!!" ) )
>>> temp = tempfile.NamedTemporaryFile ( )
>>> temp.file.write ( "hello, world!!!" )
>>> temp.file.close ( )
>>> store.create_object_from_file ( BUCKET_PUBLIC, "hello3", \
temp.name )
>>> hello = store.get_object ( BUCKET_PUBLIC, "hello" )
>>> hello.read ( 10 )
'hello, wor'
>>> hello.read ( 10 )
'ld!!!'
>>> store.get_object ( BUCKET_PUBLIC, "hello2" ).read ( )
'hello, world!!!'
>>> store.get_object ( BUCKET_PUBLIC, "hello3" ).read ( )
'hello, world!!!'
>>> store.create_bucket ( TEST_BUCKET_CREATE )
Traceback (most recent call last):
    ...
BucketCanNotCreate
>>> store.delete_object ( BUCKET_PUBLIC, "hello" )
>>> store.get_object ( BUCKET_PUBLIC, "hello" ).read ( )
Traceback (most recent call last):
    ...
ObjectNotExists
>>> store.get_all_buckets ( )
[<Bucket: libstorages-cj-private>, <Bucket: libstorages-cj-public>, \
<Bucket: cloudstore-test-create>, <Bucket: bukaopu2>, <Bucket: bukaopu>]
>>> store.get_all_objects ( BUCKET_PUBLIC )
"""
