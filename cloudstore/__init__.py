from cloudstore.domains import CommonPrefix, Object, Bucket, ObjectList
from config import OSSConfig, S3Config
from cloudstore.store import Store
from cloudstore.factory import env, create


__version__ = "0.0.2"


BUCKET_PUBLIC  = "cloudstore-cj-public"
BUCKET_PRIVATE = "cloudstore-cj-private" 

TEST_BUCKET_CREATE = 'cloudstore-test-create'
