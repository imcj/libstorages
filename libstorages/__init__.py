# !-*- encoding:utf-8 -*-

from libstorages.domains import CommonPrefix, Key, Bucket, KeyList
from config import OSSConfig, S3Config
from libstorages.factory import env, create


__version__ = "0.0.2"


BUCKET_PUBLIC  = "libstorages-cj-public"
BUCKET_PRIVATE = "libstorages-cj-private" 

TEST_BUCKET_CREATE = 'libstorages-test-create'

class Storage:
    """
    .. module:: libstorages

    `libstorages` 的所有接口全部集中在，:class:`libstorages.store.Store` ，提供对
    :class:`Bucket` 和 :class:`Object` 的控制。
    """

    def __init__ ( self, config ):
        self.config = config

    def create_bucket ( self, bucket ):
        """创建一个 :class:`Bucket` 对象

        会提交创建到远程，如果希望获得一个Bucket对象，请通过构造函数实例化对象。

        :param bucket: Bucket的名称 必须是一个合法的文件名。
        :type bucket: `string`
        :rtype: :class:`Bucket`
        :return: :class:`Bucket`
        """
        raise NotImplementedError ( )

    def delete_bucket ( self, bucket ):
        """
        删除 Bucket 对象

        :param bucket: Bucket对象
        :type bucket: string
        """
        raise NotImplementedError ( )

    def get_all_buckets ( self ):
        raise NotImplementedError ( )

    def create_key ( self, bucket, key, data, upload_callback = None ):
        """ 创建对象

        上传数据到远程服务器，部分厂商需要创建后设置acl。否则默认为私有。
        
        类: :class:`StoreFactory`

        >>> store = libstorages.factory.StoreFactory.create ( "oss" )
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
        raise NotImplementedError ( )

    def create_key_from_file ( self, bucket, key, file_path ):
        """ 创建对象

        :meth:`libstorages.store.Store.create_object` 的别名。

        :param bucket: Bucket的名子
        :type bucket: `string`
        :param key: 对象名，因为小写 object 重名所以改叫key
        :type key: string
        :param file_path: 本地文件路径，如果指定file_path那么data就会实效
        :type file_path: string

        """
        raise NotImplementedError ( )

    def get_key ( self, bucket, key ):
        raise NotImplementedError ( )

    def delete_key ( self, bucket, key ):
        raise NotImplementedError ( )

    def get_all_keys ( self, bucket_name, prefix="", marker = "",\
                          delimiter = "", max_keys = 1000 ):
        raise NotImplementedError ( )

    def get_key_metadata ( self, bucket, key, name ):
        """ 获得元信息

        :param bucket: Bucket的名子
        :type bucket: `string`
        :param key: 对象名，因为小写 object 重名所以改叫key
        :type key: string
        :param name: 元信息的键名
        :type name: string
        :rtype: string
        :return: string
        """
        self._factory_create_bucket ( bucket ).get_key ( key )\
            .get_metadata ( name )
        

    def set_key_metadata ( self, bucket, key, name, value ):
        """ 设置元信息

        :param bucket: Bucket的名子
        :type bucket: `string`
        :param key: 对象名，因为小写 object 重名所以改叫key
        :type key: string
        :param name: 元信息的键名
        :type name: string
        :param value: 元信息的键值
        :type value: string
        """

        self._factory_create_bucket ( bucket ).get_key ( key )\
            .set_metadata ( name, value )


