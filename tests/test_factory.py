#!/usr/bin/env python

from libstorages import Store, OSSConfig
from libstorages.backends.oss import Adapter
from libstorages.factory import AdapterFactory, StoreFactory
from libstorages import env, create

class TestAdapterFactory:
    def test_create ( self ):
        adapter_factory = AdapterFactory ( )
        adapter = adapter_factory.create ( "oss", OSSConfig ( "1", "1" ) )
        assert isinstance ( adapter, Adapter )


class TestStoreFactory:
    def test_create ( self ):
        vender_id = "oss"
        store = StoreFactory ( ).env ( vender_id )

        assert isinstance ( store, Store )

def test_create ( ):
    assert isinstance ( create ( "oss", "access key", "secret key" ), Store )

def test_env ( ):
    assert isinstance ( env ( "oss" ), Store )