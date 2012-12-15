from cloudstore.backends.oss import OSSAdapter
from cloudstore.backends.s3  import S3Adapter
from boto.s3.connection import Location

class Config ( dict ):
    def __init__ ( self, access_key, secret_key, host = "" ):
        super ( Config, self ).__init__ ( access_key = access_key, secret_key = secret_key, host = host )

class BCSConfig ( Config ):
    pass

class SAES3Config ( Config ):
    pass

class OSSConfig ( Config ):

    DEFAULT_HOST = "oss.aliyuncs.com"
    DEFAULT_ADAPTER = OSSAdapter

    def __init__ ( self, access_key, secret_key, host = "" ):
        if "" == host:
            host = self.DEFAULT_HOST

        self.adapter = self.DEFAULT_ADAPTER ( access_key, secret_key, host )
        super ( OSSConfig, self ).__init__ ( access_key, secret_key, host )

class S3Config ( Config ):
    def __init__ ( self, access_key, secret_key, host = "", location = "" ):
        if "" == location:
            location = Location.DEFAULT
        self.adapter = S3Adapter ( access_key, secret_key, location )
        super ( S3Config, self ).__init__ ( access_key, secret_key )