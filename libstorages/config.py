from boto.s3.connection import Location
from pdb import set_trace as bp

VENDER = [ 's3', 'oss', 'bcs' ]

class Config ( dict ):
    def __init__ ( self, access_key, secret_key, host = None ):
        self.access_key = access_key
        self.secret_key = secret_key

        if not hasattr ( self, 'host' ):
            self.host = host

        super ( Config, self ).__init__ ( access_key = access_key, \
                                          secret_key = secret_key, \
                                          host = host )

class BCSConfig ( Config ):
    host = "bcs.duapp.com"

class SAES3Config ( Config ):
    pass

class OSSConfig ( Config ):
    host = "oss.aliyuncs.com"

class S3Config ( Config ):
    def __init__ ( self, access_key, secret_key, host = "", location = "" ):
        if "" == location:
            self.location = Location.DEFAULT
        super ( S3Config, self ).__init__ ( access_key, secret_key )
