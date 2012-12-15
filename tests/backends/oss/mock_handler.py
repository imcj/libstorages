from cloudstore import Bucket, Object, CommonPrefix
from pdb import set_trace as bp



class MockOSSHandlerFactory:
    def createBucketHandler ( self ):
        return MockOSSBucketXMLContentHandler ( )

    def createObjectHandler ( self, bucket ):
        return MockOSSObjectXMLContentHandler ( bucket )

        
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


class MockOSSObjectXMLContentHandler ( MockCommonHandler ):
	def __init__ ( self, bucket ):
		self.bucket = bucket

		self.objects = [
			CommonPrefix ( name = "prefix1", bucket = bucket ),
			Object ( name = "object1", bucket = bucket )
		]