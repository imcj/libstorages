libstorages: 简单的云存储接口
=============================

.. image:: https://travis-ci.org/bukaopu/cloudstore.png

libstorages 提供简单统一的云存储API接口。

通常云储存厂商会提供各种不同的API借口，本着方便你我他的态度，整合一下。

支持厂商
--------

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

不要直接扔到Python里面执行。

>>> storages = libstorages.env ( "oss" )
>>> storages.create_object ( "bukaopu", "hello", "hello, world !!!" )

.. note::

    不要直接扔到Python里面执行，完整执行的代码还需要两步::

    - ``import libstorages``
    - ``env``方法需要设置环境变量``OSS_ACCESS_KEY``和``OSS_SECRET_KEY``

安装
----

使用 `pip <http://www.pip-installer.org/>`_ 安装。

    $ pip install libstorages

或者 `easy_install <http://pypi.python.org/pypi/setuptools>`_

    $ easy_install libstorages



贡献
----

libstorages 正在积极的开发当中，欢迎社会各界人士的参与和贡献。

- 在issue中可能有很多未解决的bug或者新功能的讨论，希望能帮助修复bug或者对有价值的新功能进行开发。

- 从GitHub `Fork <https://github.com/imcj/libstorages>`_ 源码并建立新的分支。

- 编写一个测试用例，通过测试用例来了解你解决的Bug或者开发的新功能的情况。

- Send a pull request it gets merged and published.
- 记得把你的名字写入 `作者 <https://github.com/imcj/libstorages/blob/master/AUTHORS.rst>`_。
