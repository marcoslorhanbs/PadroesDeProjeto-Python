class Client:
    def do_something(self, foo: Foo, bar: Bar):
        if foo is None:
            raise ValueError("foo must be provided")
        if bar is None:
            raise ValueError("bar must be provided")
        
        foo.do_something()
        bar.do_something_else()
