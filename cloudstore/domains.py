#! -*- encoding:utf-8 -*-

from pdb import set_trace as bp 

class ObjectList ( list ):
    def __init__ ( self, collection = [], marker = "", max_keys = 1000 ):
        self += collection
        self.marker = marker

class CommonPrefix:
    """
    通用前缀 

    也就是代表目录，只有读取的操作用到，写操作根据名字来分割，自己不用管。

    :ivar name: 目录名
    :ivar bucket: 目录所属的Bucket对象
    """
    def __init__ ( self, name = "", bucket = None ):
        self.name = name
        self.bucket = bucket

    def __repr__ ( self ):
        return "<CommonPrefix: \"%s\">" % self.name

    @property
    def short_name ( self ):
        try:
            shortname = self.name [ self.name[:-2].rindex ( "/" ) + 1 : ]
        except ValueError:
            shortname = self.name # TODO 
        return shortname

class Object:
    def __init__ ( self, name = "", bucket = None, last_modified = None, etag = "", size = "" ):
        self.name = name
        self.bucket = bucket
        self.last_modified = last_modified
        self.size = size
        
    @property
    def short_name ( self ):
        try:
            shortname = self.name [ self.name.rindex ( "/" ) + 1 : ]
        except ValueError:
            shortname = self.name # TODO 
        return shortname

    def __repr__ ( self ):
        return "<Object: %s>" % self.name

class Bucket:
    def __init__ ( self, name = "", creation_date = None ):
        self.name = name
        self.creation_date = creation_date

    def __repr__ ( self ):
        return "<Bucket: %s>" % ( self.name )
