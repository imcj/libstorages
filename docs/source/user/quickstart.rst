.. _quickstart:

快速指引
========

.. modules:: libstorages

从现在开始我假设你完成了 :ref:`安装 <install>` 步骤，开始使用 libstorages管理
你云端的数据。

store对象
---------

所有的操作都可以通过 store 对象完成。

    >>> import libstorages
    >>> store = libstorages.env ( "bcs" )

.. note:
    env 方法可以快速的创建Store对象，ACCESS_KEY和SECRET_KEY从环境变量中获取。
    格式是 (VENDER)_ACCESS_KEY 和 (VENDER)_SECRET_KEY，例如： BCS_ACCESS_KEY
    BCS_SECRET_KEY。

现在我们可以上传一些数据。

    >>> object = store.create_object ( "buket", "hello", "hello, world !!!" )

``object`` 是 :class:`Object` 的实例。

    >>> object = store.create_object_from_file ( "bucket", "hello", \
    "/etc/resolve" )

也可以通过文件上传内容。


