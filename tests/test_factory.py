#!/usr/bin/env python

from libstorages import Storage, OSSConfig
from libstorages.factory import StorageFactory
from libstorages import env, create

class TestStorageFactory:
    def test_create ( self ):
        vender_id = "bcs"
        storage = StorageFactory ( ).env ( vender_id )

        assert isinstance ( storage, Storage )

def test_create ( ):
    assert isinstance ( create ( "bcs", "access key", "secret key" ), Storage )

def test_env ( ):
    assert isinstance ( env ( "bcs" ), Storage )
