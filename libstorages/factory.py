#! -*- encoding:utf-8 -*-

import os
import xml.sax

from pdb import set_trace as bp
import libstorages
import libstorages.backends

class SaxParserFactory:
	def create ( self ):
		return xml.sax.make_parser ( )

class StorageFactory:
    """
    格式 (VENDER_ID)_ACCESS_KEY (VENDER_ID)_SECRET_KEY 厂商id的大写。
    两个环境变量获得初始默认的配置
    """

    instance = None

    def __init__ ( self ):
        pass

    @staticmethod
    def get_instance ( ):
        if not StorageFactory.instance:
            StorageFactory.instance = StorageFactory ( )

        return StorageFactory.instance;

    def create ( self, vender_id, access_key, secret_key ):
        if not vender_id in libstorages.config.VENDER:
            raise StandardError ( "Not implement this vender." )

        config_class_name  = "%sConfig" % vender_id.upper ( )
        has_specify_config = hasattr ( libstorages.config, config_class_name )

        if not has_specify_config:
            config = Config ( access_key = access_key,
                              secret_key = secret_key )
        else:
            config = getattr ( libstorages.config, config_class_name ) \
                             ( access_key = access_key, \
                               secret_key = secret_key )

        adapter_module_name = "libstorages.backends.%s" % vender_id.lower ( )
        backends = __import__ ( adapter_module_name )
        adapter_module = getattr ( libstorages.backends, vender_id.lower ( ) )
        return getattr ( adapter_module , "%sStorage" % vender_id.upper ( ) ) \
        ( config ) 

    def env ( self, vender_id ):
        ACCESS_KEY = os.getenv ( "%s_ACCESS_KEY" % vender_id.upper ( ) )
        SECRET_KEY = os.getenv ( "%s_SECRET_KEY" % vender_id.upper ( ) )

        return self.create ( vender_id, ACCESS_KEY, SECRET_KEY )

def create ( vender_id, access_key, secret_key ):
    return StorageFactory.get_instance ( ) \
                       .create ( vender_id, access_key, secret_key )

def env ( vender_id ):
    return StorageFactory.get_instance ( ).env ( vender_id )
