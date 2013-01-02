#! -*- encoding: utf-8 -*-

__doc__ = """
>>> from pdb import set_trace as bp
>>> from libstorages.factory import StoreFactory
>>> factory = StoreFactory ( )
>>> store = factory.env ( "oss" )
>>> # 以上为配置store对象。
>>> # 如果是文件路径，请自行使用 open 传入 file 对象。
>>> store.put_object ( 'bukaopu', 'hello', 'hello' )
"""