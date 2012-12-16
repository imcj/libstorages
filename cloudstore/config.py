from boto.s3.connection import Location
from pdb import set_trace as bp

VENDER = [ 's3', 'oss' ]

class Config ( dict ):
    def __init__ ( self, access_key, secret_key, host = "" ):
        self.access_key = access_key
        self.secret_key = secret_key
        self.host       = host

        super ( Config, self ).__init__ ( access_key = access_key, secret_key = secret_key, host = host )


class BCSConfig ( Config ):
    pass

class SAES3Config ( Config ):
    pass

class OSSConfig ( Config ):
    DEFAULT_HOST = "oss.aliyuncs.com"

    def __init__ ( self, access_key, secret_key, host = "" ):
        if "" == host:
            host = self.DEFAULT_HOST

        super ( OSSConfig, self ).__init__ ( access_key, secret_key, host )

class S3Config ( Config ):
    def __init__ ( self, access_key, secret_key, host = "", location = "" ):
        if "" == location:
            self.location = Location.DEFAULT
        super ( S3Config, self ).__init__ ( access_key, secret_key )