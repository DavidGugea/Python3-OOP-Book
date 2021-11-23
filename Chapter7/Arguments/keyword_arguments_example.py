class Options:
    default_options = {
        'port': 21,
        'host': 'localhots',
        'username': None,
        'password': None,
        'debug': False
    }

    def __init__(self, **kwargs):
        self.options = dict(Options.default_options)
        self.options.update(kwargs)

    def __getitem__(self, key):
        return self.options[key]


options = Options(username="test_username", password="test_password", debug=True)
print(options["debug"])
print(options["port"])
print(options["username"])
print(options)
