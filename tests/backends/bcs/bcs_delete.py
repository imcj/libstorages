#! -*- encoding: utf-8 -*-

__doc__="""
>>> from libstorages import env, Storage, BUCKET_PUBLIC, TEST_BUCKET_CREATE
>>> from StringIO import StringIO
>>> from pdb import set_trace as bp 
>>> import tempfile
>>> import os
>>> storage = env ( "bcs" )
>>> storage.create_key ( BUCKET_PUBLIC, "hello", "hello, world!!!" )
<Key: hello>
>>> storage.delete_key ( BUCKET_PUBLIC, "hello" )
>>> storage.get_key ( BUCKET_PUBLIC, "hello" ).read ( )
Traceback (most recent call last):
    ...
ObjectNotExists: hello
"""
