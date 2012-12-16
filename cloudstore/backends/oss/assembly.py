import xml.sax
from cloudstore.backends.oss import handler
from cloudstore.factory import SaxParserFactory
from pdb import set_trace as bp

class OSSAssembly:
    def __init__ ( self ):
        self.handler_factory = handler.OSSHandlerFactory ( )
        self.parser_factory  = SaxParserFactory ( )

    def load_buckets ( self, response ):
        parser = self.parser_factory.create ( )
        handler = self.handler_factory.createBucketHandler ( )
        parser.setContentHandler ( handler )
        parser.parse ( response )
        return handler.buckets 


    def load_objects ( self, bucket, response ):
        parser = self.parser_factory.create ( )
        handler = self.handler_factory.createObjectHandler ( bucket )
        parser.setContentHandler ( handler )
        parser.parse ( response )
        return handler.objects