... QINIU

=========
七牛存储库
=========

百度是不指望了，现在来看看七牛。

初始化
-----

>>> import os
>>> from pdb import set_trace as bp
>>> from qbox import digestoauth
>>> import qbox
>>> import qbox.rs
>>> import qbox.digestoauth
>>> ACCESS_KEY = os.getenv ( "QINIU_ACCESS_KEY" )
>>> SECRET_KEY = os.getenv ( "QINIU_SECRET_KEY" )
>>> qbox.config.ACCESS_KEY = ACCESS_KEY
>>> qbox.config.SECRET_KEY = SECRET_KEY
>>> qn = qbox.rs.Service ( qbox.digestoauth.Client ( ), "b" )
>>> qn.Mkbucket ( "bukaopu" )
True
>>> qn.Buckets ( )
[u'bukaopu']
>>>