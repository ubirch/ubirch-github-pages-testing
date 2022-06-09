class API(object):
    """! The example API """

    def __init__(self, api_key: str, debug=True) -> None:
        """!
        @param api_key has to be in format xxxxx-xxxxx-xxxxx-xxxxx
        @param debug should print debug statements
        """
        super().__init__()
        self.key = api_key

        if debug:
            print(api_key)


    def get_url(self, stage="test") -> str:
        """!
        @param stage has to be one of [test, prod]
        @return API access URL
        """
        return "https://example.com/" + stage + "/" + self.key
