import os
from cloudstore import CommonPrefix, Object, S3Config
from cloudstore.backends.s3 import Adapter
from pdb import set_trace as bp

class TestStore:
    def setUp ( self ):
        self.access_key = os.getenv ( "AWS_ACCESS_KEY" )
        self.secret_key = os.getenv ( "AWS_SECRET_KEY" )
        self.adapter = Adapter ( S3Config ( self.access_key, self.secret_key, "oss.aliyuncs.com" ) )
        self.bucket  = self.adapter.get_all_buckets ( )[0]

    def test_get_all_buckets ( self ):
        buckets = self.adapter.get_all_buckets ( )
        assert len ( buckets ) > 0


    def test_get_all_objects ( self ):
        found_common_prefix = True
        found_object        = True

        for key in self.adapter.get_all_objects ( self.bucket.name, delimiter = "/" ):
            if isinstance ( key, CommonPrefix ):
                found_common_prefix  =True

            elif isinstance ( key, Object ):
                found_object = True


        assert found_common_prefix and found_object