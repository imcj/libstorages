
__doc__="""
>>> from libstorages import env, Storage, BUCKET_PUBLIC, TEST_BUCKET_CREATE
>>> from StringIO import StringIO
>>> from pdb import set_trace as bp 
>>> import tempfile
>>> import os
>>> storage = env ( "bcs" )

>>> storage.get_all_buckets ( )
[<Bucket: libstorages-cj-private>, <Bucket: libstorages-cj-public>, \
<Bucket: cloudstore-test-create>, <Bucket: bukaopu2>, <Bucket: bukaopu>]
>>> keys = storage.get_all_key ( BUCKET_PUBLIC )
>>> keys
[<Key: hello3>, <Key: hello2>]
>>> keys[0].read ( 5 )
'hello'
"""

