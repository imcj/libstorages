import xml.sax
from cloudstore import Object, CommonPrefix, Bucket
from dateutil.parser import parser
from pdb import set_trace as bp

class OSSHandlerFactory:
    def createBucketHandler ( self ):
        return OSSBucketXMLContentHandler ( )

    def createObjectHandler ( self, bucket ):
        return OSSObjectXMLContentHandler ( bucket )

class OSSBucketXMLContentHandler ( xml.sax.ContentHandler ):
    def __init__ ( self ):
        self.bucket  = None
        self.buckets = []

        self.flag_name = False
        self.flag_creation_date = False

    def _createAndFillBucket ( self, name = "", creation_date = "" ):
        return Bucket ( ) 

    def characters ( self, content ):
        if self.flag_name:
            self.bucket.name = content

        if self.flag_creation_date:
            self.bucket.creation_date = content

    def startElement ( self, name, attrs ):
        if "Bucket" == name:
            self.bucket = self._createAndFillBucket ( )

        if "Name" == name:
            self.flag_name = True

        if "CreationDate" == name:
            self.flag_creation_date = True

    def endElement ( self, name ):
        if "Bucket" == name:
            self.buckets.append ( self.bucket )

        if "Name" == name:
            self.flag_name = False

        if "CreationDate" == name:
            self.flag_creation_date = False

class OSSObjectXMLContentHandler ( xml.sax.ContentHandler ):
    def __init__ ( self, bucket ):
        self.bucket   = bucket
        self.object   = None
        self.objects  = []
        self.prefix   = None
        self.prefixes = []

        self.flag_contents        = False
        self.flag_key             = False
        self.flag_last_modified   = False  
        self.flag_etag            = False
        self.flag_size            = False
        self.flag_common_prefixes = False
        self.flag_prefix          = False

    def startElement ( self, name, attrs ):
        if "Contents" == name:
            self.object = Object ( name = "", bucket = self.bucket )
        elif "Key" == name:
            self.flag_key = True
        elif "LastModified" == name:
            self.flag_last_modified = True
        elif "ETag" == name:
            self.flag_etag = True
        elif "Size" == name:
            self.flag_size = True
        elif "CommonPrefixes" == name:
            self.flag_common_prefixes = True
        elif "Prefix" == name:
            self.flag_prefix = True

    def endElement ( self, name ):
        if "Contents" == name:
            self.objects.append ( self.object )
        elif "Key" == name:
            self.flag_key = False
        elif "LastModified" == name:
            self.flag_last_modified = False
        elif "ETag" == name:
            self.flag_etag = False
        elif "Size" == name:
            self.flag_size = False
        elif "CommonPrefixes" == name:
            self.flag_common_prefixes = False
        elif "Prefix" == name:
            self.flag_prefix = False
        elif "ListBucketResult" == name:
            self.objects = self.prefixes + self.objects

    def characters ( self, content ):
        if self.flag_key:
            self.object.name = content
        elif self.flag_last_modified:
            self.object.last_modified = parser ( ).parse ( content )
        elif self.flag_etag:
            self.object.etag = content
        elif self.flag_size:
            self.object.size = int ( content )
        elif self.flag_prefix:
            self.prefixes.append ( CommonPrefix ( content ) )