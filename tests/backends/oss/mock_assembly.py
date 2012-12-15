from mock_handler import MockOSSHandlerFactory, MockSaxParserFactory
from cloudstore.backends.oss.assembly import OSSAssembly
from StringIO import StringIO

class MockAssembly ( OSSAssembly ):
	def __init__ ( self ):
		self.handler_factory = MockOSSHandlerFactory ( )
		self.parser_factory = MockSaxParserFactory ( )