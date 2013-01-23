from libstorages import Bucket, Key, CommonPrefix
from pdb import set_trace as bp



class MockOSSHandlerFactory:
    def createBucketHandler ( self ):
        return MockOSSBucketXMLContentHandler ( )

    def createObjectHandler ( self, bucket ):
        return MockOSSKeyXMLContentHandler ( bucket )

        
class MockSaxParser:
	def setContentHandler ( self, handler ):
		pass

	def parse ( self, fd ):
		pass

class MockSaxParserFactory:
	def create ( self ):
		return MockSaxParser ( ) 

class MockCommonHandler:

	def setDocumentLocator ( self, *args, **kwargs ):
		pass

	def startDocument ( self, *args, **kwargs ):
		pass

	def __getattr__ ( self, *args,  **kwargs ):
		pass


class MockOSSBucketXMLContentHandler ( MockCommonHandler ):
	def __init__ ( self ):
		self.buckets = [
			Bucket ( "bucket1" ),
			Bucket ( "bucket2" )
		]


class MockOSSKeyXMLContentHandler ( MockCommonHandler ):
	def __init__ ( self, bucket ):
		self.bucket = bucket

		self.objects = [
			CommonPrefix ( name = "prefix1", bucket = bucket ),
		    Key ( name = "object1", bucket = bucket )
		]
