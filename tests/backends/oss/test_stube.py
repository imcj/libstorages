import os
from cloudstore import CommonPrefix, Object, OSSConfig
from cloudstore.backends.oss import Adapter
from pdb import set_trace as bp

class TestStore:
    def setUp ( self ):
        self.access_key = os.getenv ( "OSS_ACCESS_KEY" )
        self.secret_key = os.getenv ( "OSS_SECRET_KEY" )
        self.adapter = Adapter ( OSSConfig ( self.access_key, self.secret_key, "oss.aliyuncs.com" ) )
        self.bucket  = self.adapter.get_all_buckets ( )[1]

    def test_get_all_buckets ( self ):
        buckets = self.adapter.get_all_buckets ( )
        assert len ( buckets ) > 0


    def test_get_all_objects ( self ):
        found_common_prefix = True
        found_object        = True

        keys = self.adapter.get_all_objects ( self.bucket.name, delimiter = "/", prefix = "img/" )

        for key in keys:
            if isinstance ( key, CommonPrefix ):
                found_common_prefix  =True

            elif isinstance ( key, Object ):
                found_object = True


        assert found_common_prefix and found_object