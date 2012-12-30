#! -*- encoding: utf-8 -*-

from pdb import set_trace as bp

class Store:
    """
    .. module:: cloudstore

    `cloudstore` 的所有接口全部集中在，:class:`cloudstore.store.Store` ，提供对
    :class:`Bucket` 和 :class:`Object` 的控制。
    """

    def __init__ ( self, config ):
        self.config = config
        if not config.adapter:
            raise StandardError ( "Missing adapter." )

    def create_bucket ( self, bucket ):
        """创建一个 :class:`Bucket` 对象

        会提交创建到远程，如果希望获得一个Bucket对象，请通过构造函数实例化对象。

        :param bucket: Bucket的名称 必须是一个合法的文件名。
        :type bucket: `string`
        :rtype: :class:`Bucket`
        :return: :class:`Bucket`
        """
        self.config.adapter.create_bucket ( bucket )

    def delete_bucket ( self, bucket ):
        """
        删除 Bucket 对象

        :param bucket: Bucket对象
        :type bucket: string
        """
        self.config.adapter.delete_bucket ( bucket )

    def get_all_buckets ( self ):
        return self.config.adapter.get_all_buckets ( )

    def create_object ( self, bucket, key, data ):
        """ 创建对象

        上传数据到远程服务器，部分厂商需要创建后设置acl。否则默认为私有。
        
        类: :class:`StoreFactory`

        >>> store = cloudstore.factory.StoreFactory.create ( "oss" )
        >>> store.create_object ( "bucket1", "object1", "helloworld" )

        >>> store.create_object_from_file ( "bucket1", "object1",
        ... "/media/hello.mp4" )

        :param bucket: Bucket的名子
        :type bucket: `string`
        :param key: 对象名，因为小写 object 重名所以改叫key
        :type key: string
        :param data: :class:`file`
        :type data: :class:`file` or :class:`string`
        :param file_path: 本地文件路径，如果指定file_path那么data就会实效
        :type file_path: string
        """

        if isinstance ( data, basestring ):
            self.config.adapter.create_object ( bucket, key, data )
        elif hasattr ( data, "read" ):
            self.config.adapter \
            .create_object_from_stream ( bucket, key, data )

    def create_object_from_file ( self, bucket, key, file_path ):
        """ 创建对象

        :meth:`cloudstore.store.Store.create_object` 的别名。

        :param bucket: Bucket的名子
        :type bucket: `string`
        :param key: 对象名，因为小写 object 重名所以改叫key
        :type key: string
        :param file_path: 本地文件路径，如果指定file_path那么data就会实效
        :type file_path: string

        """
        self.config.adapter.create_object_from_file ( bucket, key, file_path )

    def get_object ( self, bucket, key ):
        return self.config.adapter.get_object ( bucket, key )

    def delete_object ( self, bucket, key ):
        self.config.adapter.delete_object ( bucket, key )

    def get_all_objects ( self, bucket_name, prefix="", marker = "",\
                          delimiter = "", max_keys = 1000 ):
        return self.config.adapter.get_all_objects ( bucket_name, prefix, marker, delimiter, max_keys )
