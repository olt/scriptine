from distutils.core import Command
from scriptine import log

class DistutilsCommand(Command):
    user_options = []
    def initialize_options(self): pass
    def finalize_options(self): pass

class Options(dict):
    """
    Dictionary with attribute style access.
    
    >>> o = Options(bar='foo')
    >>> o.bar
    'foo'
    """
    def __repr__(self):
        args = ', '.join(['%s=%r' % (key, value) for key, value in
            self.iteritems()])
        return '%s(%s)' % (self.__class__.__name__, args)
    
    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError(name)
    
    __setattr__ = dict.__setitem__
    
    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError(name)

options = Options()
options.dry = False

def simple_decorator(decorator):
    """This decorator can be used to turn simple functions
    into well-behaved decorators, so long as the decorators
    are fairly simple. If a decorator expects a function and
    returns a function (no descriptors), and if it doesn't
    modify function attributes or docstring, then it is
    eligible to use this. Simply apply @simple_decorator to
    your decorator and it will automatically preserve the
    docstring and function attributes of functions to which
    it is applied."""
    def new_decorator(f):
        g = decorator(f)
        g.__name__ = f.__name__
        g.__doc__ = f.__doc__
        g.__dict__.update(f.__dict__)
        return g
    # Now a few lines needed to make simple_decorator itself
    # be a well-behaved decorator.
    new_decorator.__name__ = decorator.__name__
    new_decorator.__doc__ = decorator.__doc__
    new_decorator.__dict__.update(decorator.__dict__)
    return new_decorator

def dry(message, func, *args, **kw):
    log.info(message)
    
    if not options.dry:
        return func(*args, **kw)

@simple_decorator
def log_call(func):
    def _log_call(*args, **kw):
        _log_function_call(func, *args, **kw)
        return func(*args, **kw)
    return _log_call

def _log_function_call(func, *args, **kw):
    message = func.func_name
    if args:
        message += ' ' + ' '.join(map(str, args))
    if kw:
        kw_str = ' '.join(['%s %r' % (k, v) for k, v in kw.iteritems()])
        message += '(' + kw_str + ')'
    log.info(message)

@simple_decorator
def dry_guard(func):
    def _dry_guard(*args, **kw):
        _log_function_call(func, *args, **kw)
        if not options.dry:
            return func(*args, **kw)
    return _dry_guard