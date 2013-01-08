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

使用
----

>>> storages = libstorages.env ( "oss" )
>>> storages.create_object ( "bukaopu", "hello", "hello, world !!!" )

.. note::

    不要直接扔到Python里面执行，完整执行的代码还需要两步::

    - ``import libstorages``
    - ``env``方法需要设置环境变量``OSS_ACCESS_KEY``和``OSS_SECRET_KEY``


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

贡献
----

项目还在孵化阶段，需要贡献更多的后端。

- 从GitHub `Fork <https://github.com/imcj/libstorages>`_ 项目然后建立 `新的分支 <http://www.ruanyifeng.com/blog/2012/07/git.html>`_ 。

- 编码

- Pull Request

- 把你的名字填入 `作者 <https://github.com/imcj/libstorages/blob/master/AUTHORS.rst>`_ 。


.. toctree::
   :maxdepth: 1

   dev/help
   dev/authors

License
--------

`Apache 2.00 <https://raw.github.com/imcj/libstorages/master/LICENSE>`_ 

Member of `OSS Manifesto <http://ossmanifesto.org>`_
