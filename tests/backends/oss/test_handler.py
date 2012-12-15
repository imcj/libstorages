import os
from cloudstore.factory import SaxParserFactory
from cloudstore.backends.oss.handler import OSSObjectXMLContentHandler, OSSBucketXMLContentHandler
from cloudstore import Bucket, CommonPrefix, Object
from pdb import set_trace as bp

FIXTUES_DIR = os.path.join ( os.path.dirname ( os.path.abspath ( __file__ ) ), "../", "../", "fixtures" )

class OSSXMLContentHandler:
	def __init__ ( self ):
		sax_parser_factory = SaxParserFactory ( )
		self.parser = sax_parser_factory.create ( )
		self.fixtures = FIXTUES_DIR

class TestOSSBucketXMLContentHandler ( OSSXMLContentHandler ):
	def test_parse ( self ):
		pass


class TestOSSObjectXMLContentHandler ( OSSXMLContentHandler ):

	def test_parse ( self ):
		handler = OSSObjectXMLContentHandler ( Bucket ( "bucket1" ) )
		self.parser.setContentHandler ( handler )
		self.parser.parse ( open ( os.path.join ( self.fixtures, "oss_bucket_bukaopu_delimiter_by_dash.xml" ), "r" ) )

		assert len ( handler.objects ) > 1
		found_common_prefix = False
		found_object = False
		for key in handler.objects:
			if isinstance ( key, CommonPrefix ):
				found_common_prefix = True
			if isinstance ( key, Object ):
				found_object = True

		assert found_common_prefix and found_object
