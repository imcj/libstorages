#!/usr/bin/env python

from cloudstore import Store, OSSConfig
from cloudstore.backends.oss import Adapter
from cloudstore.factory import AdapterFactory, StoreFactory

class TestAdapterFactory:
    def test_create ( self ):
        adapter_factory = AdapterFactory ( )
        adapter = adapter_factory.create ( "oss", OSSConfig ( "1", "1" ) )
        assert isinstance ( adapter, Adapter )


class TestStoreFactory:
    def test_create ( self ):
        vender_id = "oss"
        store = StoreFactory ( ).create ( vender_id )

        assert isinstance ( store, Store )