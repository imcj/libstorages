from cloudstore.backends.oss import Adapter
from cloudstore import Bucket, OSSConfig
from mock_oss_api import MockOssAPI
from mock_handler import MockOSSBucketXMLContentHandler, MockOSSObjectXMLContentHandler, MockSaxParserFactory
from mock_assembly import MockAssembly
from pdb import set_trace as bp 

class TestOSSAdapter:
	def setUp ( self ):
		self.adapter = Adapter ( OSSConfig ( None, None, None ) )
		self.adapter.oss = MockOssAPI ( )
		self.adapter.assembly = MockAssembly ( )


	def test_get_all_buckets ( self ):
		buckets = self.adapter.get_all_buckets ( )
		assert len ( buckets ) > 1


	def test_get_all_objects ( self ):
		objects = self.adapter.get_all_objects ( Bucket ( 'bucket1' ) )
		assert objects[0].name == "prefix1"
		assert objects[1].name == "object1"