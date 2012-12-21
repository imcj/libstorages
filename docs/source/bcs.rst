===============
BCS - 百度云存储
===============

----
实例
----


>>> from cloudstore import pybcs
>>> import os
>>> from pdb import set_trace as bp
>>> AK = os.getenv ( "BAIDU_ACCESS_KEY" )
>>> SK = os.getenv ( "BAIDU_SECRET_KEY" )
>>> bcs = pybcs.BCS ( "http://bcs.duapp.com", AK, SK,\
...  pybcs.HttplibHTTPC )
>>> buckets = bcs.list_buckets ( )
>>> len ( buckets ) > 0
True
>>> has_bukaopu2 = [ bucket for bucket in buckets if bucket.bucket_name \
... == "bukaopu2" ]
>>> bucket_bukaopu = bcs.bucket ( "bukaopu" )
>>> bucket_bukaopu.get_acl ( )['status']
200
----------
删除Bucket
----------
>>> if has_bukaopu2:
...     bucket = bcs.bucket ( "bukaopu2" )
...     try:
...         delete_resp = bucket.delete ( )
...     except:
...         pass


----------
创建Bucket
----------
>>> bucket = bcs.bucket ( "bukaopu2" )
>>> if not has_bukaopu2:
...    bucket.create ( )['status']
>>> isinstance ( bucket, pybcs.Bucket )
True


-------
上传对象
-------

利用上传文件名必须是"/"开头。


>>> import random
>>> for i in range ( 2 ):
...     object = bucket_bukaopu.object ( "/" + str ( random.random ( ) ) )
...     d = object.put ( 'test' )
...     d = object.make_public ( )
>>> objects_bukaopu = bucket_bukaopu.list_objects ( "/" )
>>> found = [ obj.object_name for obj in objects_bukaopu \
... if obj.object_name.startswith ( "/0." ) ]
>>> len ( found ) >= 1
True
>>> first = objects_bukaopu[0]
>>> first.get_acl ( )
>>> 
>>> first.head ( )['status']
200
>>> found = None

-------
删除对象
-------

>>> for i in found:
...     object = bucket_bukaopu.object ( i )
...     resp = object.delete ( )