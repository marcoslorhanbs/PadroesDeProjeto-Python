class Client:
    def __init__(self, foo: Foo, bar: Bar):
        if foo is None:
            raise ValueError("foo must be provided")
        if bar is None:
            raise ValueError("bar must be provided")
        self.foo = foo
        self.bar = bar
        
    def do_something(self):
        self.foo.do_something()
        self.bar.do_something_else()
