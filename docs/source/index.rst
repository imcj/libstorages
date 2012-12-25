.. CloudStore documentation master file, created by
   sphinx-quickstart on Thu Dec 13 12:34:06 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

====================================
CloudStore: 统一云存储访问接口
====================================

为不同厂商云存储提供统一的API接口，易于学习，减少对象的数量使其尽可能的轻量级。

这个项目的完成度还非常的低，希望加入一起加速这个项目的同学可以直接Pull Request
给我。


特性：
-----

1. 方便更换云存储
2. 多点冗余更加方便

支持厂商
---------

* 七牛云存储
* 百度 - BCS

待支持厂商
-----------

* 盛大云
* SAE Storage
* S3
* 阿里云存储
* 又拍云存储

初始化对象
-----------

可通过StoreFactory.create创建获得 Store 对象， Store 对象提供了所有云存储控制
API 。或通过自行实例化 Config 构造 Store 对象。

对于大多数云存储厂商，常用的两个概念为 Bucket 和对象， Bucket 下可以有若干的对
象，Bucket也被大部分厂商作为计费和限制配额的基本单位，并提供有限的数量，而对象
则可以拥有无限多个。有时Bucket被叫做空间一类的名词，但通常都会提到Bucket。

>>> import os
>>> from StringIO import StringIO
>>> from cloudstore import Store, OSSConfig
>>> store = Store ( OSSConfig ( os.getenv ( "OSS_ACCESS_KEY" ), \
... os.getenv ( "OSS_SECRET_KEY" ) ) )

上传文件
---------

CloudStore 支持两种上传方式

1. 普通上传方式，单线程和一定的文件大小限制
2. 分块上传，特点时支持多线程和大小通常都在TB级别。

:py:meth:`Store.create_object` 方法第三个参数data可以接受字符串和file类型。 


>>> store.create_object ( "bukaopu", "hello", "hello, world !!!" )

>>> upload_data = StringIO ( "hello, world !!!" )
>>> store.create_object ( "bukaopu", "hello", upload_data )

上传本地文件

>>> store.create_object_from_file ( "bukaopu", "hello", "/etc/resolve" )

获取所有的Bucket
---------------
:doc:`对象参考 <ref/domains>`

>>> store.get_all_buckets ( )
[<Bucket: source1 created at 2012-05-24T09:52:16.000Z>, <Bucket: bukaopu created at 2012-11-30T14:48:31.000Z>]

获取所有的对象
-------------
:doc:`Store API 参考 <ref/store>`

>>> store.get_all_objects ( "bukaopu", delimiter = "/" )
[<CommonPrefix: "avatar/">, <CommonPrefix: "css/">, <CommonPrefix: "highlight/">, <CommonPrefix: "icons/">, <CommonPrefix: "img/">, <CommonPrefix: "js/">, <Object: .gitignore>, <Object: rubygems-1.3.6.tgz>]

Contents:

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

