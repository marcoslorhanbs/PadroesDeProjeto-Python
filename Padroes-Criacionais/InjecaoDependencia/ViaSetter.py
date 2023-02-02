class Client:
    def __init__(self):
        self.foo = None
        self.bar = None

    def set_foo(self, foo: Foo):
        if foo is None:
            raise ValueError("foo must be provided")
        self.foo = foo

    def set_bar(self, bar: Bar):
        if bar is None:
            raise ValueError("foo must be provided")
        self.bar = bar

    def validate_dependencies(self):
        if self.foo is None:
            raise ValueError("foo has not been set")
        if self.bar is None:
            raise ValueError("bar has not been set")

    def do_something(self):
        self.validate_dependencies()

        self.foo.do_something()
        self.bar.do_something_else()
