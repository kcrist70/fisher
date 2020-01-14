from contextlib import contextmanager

class Myresource:
    def query(self):
        print('query data')

@contextmanager
def make_myresoure():
    print('connect to resource')
    yield Myresource()
    print('close resource connection')


with make_myresoure() as r:
    r.query()

