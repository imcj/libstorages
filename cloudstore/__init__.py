import os
import sys
from pdb import set_trace as bp

from cloudstore.domains import CommonPrefix, Object, Bucket, ObjectList
from config import OSSConfig, S3Config
from cloudstore.store import Store

__all__ =  [ 'CommonPrefix', 'Object', 'Bucket', 'ObjectList',
             'OSSConfig', 'S3Config',
             'Store' ]

STORE_DIR = os.path.dirname ( os.path.abspath ( __file__ ) )

if "__main__" == __name__:
    store =  Store ( OSSConfig ( "ka1ln69obmd2u0r98yph2aa4", "q7n338IBMEFnxm/6zNJAQbBmZo8=" ) )
    # store = Store ( S3Config ( "AKIAIRFW2EC2IMNLF4LA", "dhu2T1ap1K9h2aEXE3TBrqbMYN7N4wASBoAYZYCg" ) )
    print store.get_all_objects ( "bukaopu", delimiter = "/" )


__version__ = "0.0.2"