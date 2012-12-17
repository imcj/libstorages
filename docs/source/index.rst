.. CloudStore documentation master file, created by
   sphinx-quickstart on Thu Dec 13 12:34:06 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

====================================
CloudStore: 提供统一的存储云访问接口
====================================

.. image:: https://travis-ci.org/bukaopu/cloudstore.png

为各种云提供统一的访问接口，一是方便切换存储云，二让多点冗余更加方便，几行简单的代码就能搞定。

这个项目的完成度还非常的低，希望加入一起加速这个产品的同学可以联系我，或者直接Pull & Request给我。

列表Bucket
----------
:doc:`对象参考 <ref/domains>`

>>> import os
>>> from cloudstore import Store, OSSConfig
>>> store = Store ( OSSConfig ( os.getenv ( "OSS_ACCESS_KEY" ), os.getenv ( "OSS_SECRET_KEY" ) ) )
>>> store.get_all_buckets ( )
[<Bucket: source1 created at 2012-05-24T09:52:16.000Z>, <Bucket: bukaopu created at 2012-11-30T14:48:31.000Z>]

列出对象
----------
:doc:`Store参考 <ref/store>`

>>> import os
>>> from cloudstore import Store, OSSConfig
>>> store = Store ( OSSConfig ( os.getenv ( "OSS_ACCESS_KEY" ), os.getenv ( "OSS_SECRET_KEY" ) ) )
>>> store.get_all_objects ( "bukaopu", delimiter = "/" )
[<CommonPrefix: "avatar/">, <CommonPrefix: "css/">, <CommonPrefix: "highlight/">, <CommonPrefix: "icons/">, <CommonPrefix: "img/">, <CommonPrefix: "js/">, <Object: .gitignore>, <Object: rubygems-1.3.6.tgz>]


创建对象
--------

>>> import os
>>> from cloudstore import Store, OSSConfig
>>> store = Store ( OSSConfig ( os.getenv ( "OSS_ACCESS_KEY" ), os.getenv ( "OSS_SECRET_KEY" ) ) )
>>> string_data = "hello, world !!!"

Contents:

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

