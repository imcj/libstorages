#! -*- encoding:utf-8 -*-

from pdb import set_trace as bp 

class KeyList ( list ):
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

class Key ( object ):
    BUFFER_SIZE = 8192

    def __init__ ( self, name = "", bucket = None, last_modified = None, \
                   etag = "", md5 = "", content_type = "", size = "", \
                   write_progress_callback = None, read_progress_callback = \
                   None ):
        self.name = name
        self.bucket = bucket
        self.last_modified = last_modified
        self.etag = etag
        self.md5  = md5
        self.content_type = content_type
        self.size = size
        self.write_progress_callback = write_progress_callback
        self.read_progress_callback  = read_progress_callback

    def delete ( self ):
        raise NotImplementedError ( )

    def exists ( self ):
        raise NotImplementedError ( )

    def read ( self, size = None ):
        size = not size and self.BUFFER_SIZE or size
        raise NotImplementedError ( )

    def create ( self, data ):
        raise NotImplementedError ( )

    def create_from_buffer ( self, buff ):
        raise NotImplementedError ( )

    def create_from_file ( self, filepath ):
        raise NotImplementedError ( )
        
    @property
    def short_name ( self ):
        try:
            shortname = self.name [ self.name.rindex ( "/" ) + 1 : ]
        except ValueError:
            shortname = self.name
        return shortname

    def __repr__ ( self ):
        return "<Key: %s>" % self.name

class Bucket ( object ):
    def __init__ ( self, name = "", creation_date = None ):
        self.name = name
        self.creation_date = creation_date

    def create ( self ):
        raise NotImplementedError ( )

    def delete ( self ):
        raise NotImplementedError ( )

    def get_key ( self, key ):
        raise NotImplementedError ( )

    def __repr__ ( self ):
        return "<Bucket: %s>" % ( self.name )
