... QINIU

===========
七牛存储库
===========

-------
初始化
-------

>>> import os
>>> BUCKET_PUBLIC = 'bucketcjpublic'
>>> ACCESS_KEY = os.getenv ( "QINIU_ACCESS_KEY" )
>>> SECRET_KEY = os.getenv ( "QINIU_SECRET_KEY" )

>>> from pdb import set_trace as bp
>>> import urllib
>>> import mimetypes
>>> import simplejson
>>> import cloudstore
>>> import cloudstore.qbox
>>> import cloudstore.qbox.rs
>>> import cloudstore.qbox.rscli
>>> import cloudstore.qbox.uptoken
>>> import cloudstore.qbox.digestoauth
>>> from StringIO import StringIO
>>> cloudstore.qbox.config.ACCESS_KEY = ACCESS_KEY
>>> cloudstore.qbox.config.SECRET_KEY = SECRET_KEY
>>> qn = cloudstore.qbox.rs.Service ( cloudstore.qbox.digestoauth.Client ( ),\
... "b" )
>>> qn.Mkbucket ( "bukaopu" )
True
>>> qn.Buckets ( )
[u'bukaopu']
>>>


------------
添加bucket
------------

添加的bucket暂时还没有删除的API.

>>> qn = cloudstore.qbox.rs.Service ( cloudstore.qbox.digestoauth.Client ( ),\
... BUCKET_PUBLIC )
>>> qn.Mkbucket ( BUCKET_PUBLIC )
True

---------
上传文件
---------

以存在的文件会抛出异常。

>>> token = cloudstore.qbox.uptoken.UploadToken ( BUCKET_PUBLIC ).\
... generate_token ( )
>>> upload_response = cloudstore.qbox.rscli.UploadFile (\
... BUCKET_PUBLIC, 'requirements.txt', 'image/jpg', \
... 'requirements.txt', \
... '', '', token )
>>> upload_response = simplejson.loads ( upload_response )
>>> upload_response['hash']
u'FgC2TiaMDJQSxY9WSSsiLDokLT2B'
>>> upload_response = cloudstore.qbox.rscli.upload_with_file (\
... BUCKET_PUBLIC, 'hello.txt', mimetypes.types_map['.txt'], \
... StringIO ( 'hello' ), \
... '', '', token )
>>> simplejson.loads ( upload_response )['hash']
u'Fqr0xh3cxeii2r7eDztILNmuqUNN'

-------------
读取文件信息
-------------

真心建议七牛把`mimeType`改为`mime_type`.

>>> info = qn.Stat ( 'hello.txt' )
>>> info['mimeType']
u'text/plain'
>>> info['hash']
u'Fqr0xh3cxeii2r7eDztILNmuqUNN'

---------
读取文件
---------

response是一个json，其中包含键url，url为临时的下载地址，有时效为键expires，
这里就不下载文件演示了。 

>>> response = qn.Get ( 'hello.txt', 'hello.txt' )
>>> urllib.urlopen ( response['url'] ).read ( )
'hello'

---------
删除文件
---------

>>> qn.Delete ( "requirements.txt" )
True


------------
Drop Bucket
------------

删除Bucket.

>>> qn.Drop ( BUCKET_PUBLIC )
True