from scriptine.misc import dry_guard, options
from scriptine import path

def test_guard():
    
    @dry_guard
    def guarded_func(foo):
        return True
    
    assert guarded_func('hello')
    
    options.dry = True
    assert not guarded_func('hello')
    
def test_path_guard():
    
    options.dry = True
    
    path('/tmp/foobarbaz.txt').install('hello', chmod=0644)
    

def teardown_module():
    options.dry = False