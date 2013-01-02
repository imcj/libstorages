from libstorages.config import Config, BCSConfig

class TestConfig:
    def test_constractor ( self ):
        config = Config ( '1', '1' )
        assert config.access_key == '1'
        assert config.secret_key == '1'


class TestBCSConfig:
    def test_constractor ( self ):
        config = BCSConfig ( '1', '1' )
        assert config.host == "bcs.duapp.com"
