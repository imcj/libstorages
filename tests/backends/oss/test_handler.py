import os
from libstorages.factory import SaxParserFactory
from libstorages.backends.oss.handler import OSSKeyXMLContentHandler, \
OSSBucketXMLContentHandler
from libstorages import Bucket, CommonPrefix, Key
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


class TestOSSKeyXMLContentHandler ( OSSXMLContentHandler ):

	def test_parse ( self ):
		handler = OSSKeyXMLContentHandler ( Bucket ( "bucket1" ) )
		self.parser.setContentHandler ( handler )
		self.parser.parse ( open ( os.path.join ( self.fixtures, "oss_bucket_bukaopu_delimiter_by_dash.xml" ), "r" ) )

		assert len ( handler.keys ) > 1
		found_common_prefix = False
		found_object = False
		for key in handler.keys:
			if isinstance ( key, CommonPrefix ):
				found_common_prefix = True
			if isinstance ( key, Key ):
				found_object = True

		assert found_common_prefix and found_object
