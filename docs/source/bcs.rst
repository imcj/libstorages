===============
BCS - 百度云存储
===============

----
实例
----

注意，如果没有设置环境变量这个`doctest`肯定会跑不起来。

>>> import os
>>> BUCKET_PUBLIC  = "cloudstore-cj-public"
>>> BUCKET_PRIVATE = "cloudstore-cj-private"
>>> AK = os.getenv ( "BAIDU_ACCESS_KEY" )
>>> SK = os.getenv ( "BAIDU_SECRET_KEY" )

以上是一些配置，如果想跑这个测试，必须修改为自己的参数。

>>> from cloudstore import pybcs
>>> from pdb import set_trace as bp
>>> import simplejson
>>> bcs = pybcs.BCS ( "http://bcs.duapp.com", AK, SK, pybcs.HttplibHTTPC )
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

---------------
Bucket的权限控制
---------------
>>> bcs.bucket ( BUCKET_PUBLIC ).get_acl ( )['status']
200
>>> bcs.bucket ( BUCKET_PRIVATE ).make_private_to_user ( "psp" )

-------
上传对象
-------

上传文件名必须是"/"开头。


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
>>> first.head ( )['status']
200
>>> found = None

------------------
对象权限控制的默认值
------------------

默认为私有的Bucket。

>>> private = bcs.bucket ( "cloudstore-cj-private" ).object ( "/PRIVATE").\
... put ( "PRIVATE")
>>> acl = bcs.bucket ( "cloudstore-cj-private" ).object ( "/PRIVATE")\
... .get_acl ( )
>>> statements = simplejson.loads ( acl['body'] )['statements']
>>> statements[0]['user']
['psp:']

默认ACL是公开读的Buket。

>>> pubilc  = bcs.bucket ( "cloudstore-cj-public" ).object ( "/PUBLIC").\
... put ( "PUBLIC")
>>> acl = bcs.bucket ( "cloudstore-cj-public" ).object ( "/PUBLIC")\
... .get_acl ( )
>>> statements = simplejson.loads ( acl['body'] )['statements']
>>> statements[0]['user']
['psp:']

根据上面可见，百度BCS的Bucket默认ACL并不影响其下面的对象的ACL。

-------
读取对象
-------

>>> resp = first.get ( )
>>> resp['body']
'test'

-------
删除对象
-------

>>> for key in bcs.bucket ( "bukaopu" ).list_objects ( prefix="/0." ):
...     resp = key.delete ( )