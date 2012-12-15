from StringIO import StringIO

class MockOssAPI:
	def list_all_my_buckets ( self ):
		return StringIO ( )

	def list_bucket ( self, *args ):
		return StringIO ( )