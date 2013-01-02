from libstorages.domains import CommonPrefix, Object, Bucket, ObjectList
from config import OSSConfig, S3Config
from libstorages.store import Store
from libstorages.factory import env, create


__version__ = "0.0.2"


BUCKET_PUBLIC  = "libstorages-cj-public"
BUCKET_PRIVATE = "libstorages-cj-private" 

TEST_BUCKET_CREATE = 'libstorages-test-create'
