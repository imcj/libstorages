from pdb import set_trace as bp

class Store:
    """
    """

    def __init__ ( self, config ):
        self.config = config
        if not config.adapter:
            raise StandardError ( "Missing adapter." )

    def create_bucket ( self, bucket_name ):
        pass

    def get_all_buckets ( self ):
        return self.config.adapter.get_all_buckets ( )

    def put_object ( self, bucket_name, object_name, data ):
        pass

    def get_object ( self, bucket_name, object_name ):
        pass

    def get_all_objects ( self, bucket_name, prefix="", marker = "", delimiter = "", max_keys = 1000 ):
        return self.config.adapter.get_all_objects ( bucket_name, prefix, marker, delimiter, max_keys )