from mock_handler import MockOSSBucketXMLContentHandler, MockOSSObjectXMLContentHandler, MockSaxParserFactory
from mock_assembly import MockOSSHandlerFactory
from cloudstore.backends.oss.assembly import OSSAssembly
from cloudstore import Bucket
from nose import with_setup
from pdb import set_trace as bp
from StringIO import StringIO

class TestOSSAssembly:
	def setUp ( self ):
		self.assembly = OSSAssembly ( )
		self.assembly.handler_factory = MockOSSHandlerFactory ( )
		self.assembly.parser_factory  = MockSaxParserFactory  ( )

	def test_load_buckets ( self ):
		buckets = self.assembly.load_buckets ( StringIO ( ) )
		assert "bucket1" == buckets[0].name
		assert "bucket2" == buckets[1].name

	def test_load_objects ( self ):
		objects = self.assembly.load_objects ( Bucket ( name = "bucket1" ), StringIO ( ) )
		assert "prefix1" == objects[0].name
		assert "object1" == objects[1].name