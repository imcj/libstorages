import xml.sax

class SaxParserFactory:
	def create ( self ):
		return xml.sax.make_parser ( )