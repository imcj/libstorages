libstorages: 简单的云存储接口
====================================

.. image:: https://travis-ci.org/bukaopu/libstorages.png

libstorages 提供简单统一的云存储API接口。

通常云储存厂商会提供各种不同的API借口，本着方便你我他的态度，整合一下。

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

>>> import libstorages
>>> store = libstorages.env ( "oss" )
>>> store.create_object ( "bukaopu", "hello", "hello, world !!!" )
>>> # OR 通过文件上传
>>> store.create_object_from_file ( "bukaopu", "hello", "/etc/resolve" )


用户指南
---------

这部分文档重点介绍如何立即使用 libstorages。

.. toctree::
   :maxdepth: 2

   user/intro
   user/install
   user/quickstart

社区
----

关于社区的相关信息。

.. toctree::
   :maxdepth: 1

   community/faq
   community/support
   community/article

API
----

查看详细的类、方法和模块的使用手册。

.. toctree::
   :maxdepth: 2

   api

捐赠
----

如果你有兴趣贡献一些代码或视觉方面的内容。

.. toctree::
   :maxdepth: 1

   dev/help
   dev/authors
