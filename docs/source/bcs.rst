... BCS

=============
BCS 库Example
=============

擦，不想了，百度只有在BAE中运行才是完整的，否则调试都是不可能的。

初始化
-----

>>> import os
>>> from pdb import set_trace as bp
>>> from cloudstore.pybcs import bcs
>>> ACCESS_KEY = os.getenv ( "BAIDU_ACCESS_KEY" )
>>> SECRET_KEY = os.getenv ( "BAIDU_SECRET_KEY" )
>>> bp ()
>>> bcs.BCS ( bcs.const.BCS_ADDR, ACCESS_KEY, SECRET_KEY )
>>> bcs.list_buckets ( )