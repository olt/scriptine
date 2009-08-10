import sys
import re
import inspect
from distutils.core import Command
from scriptine import log

class DistutilsCommand(Command):
    user_options = []
    def initialize_options(self): pass
    def finalize_options(self): pass

def dict_to_options(d):
    d = Options(d)
    for k, v in d.iteritems():
        if isinstance(v, dict):
            d[k] = dict_to_options(v)
    return d

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


# --- begin decorator ---
##########################     LICENCE     ###############################
      
##   Redistributions of source code must retain the above copyright 
##   notice, this list of conditions and the following disclaimer.
##   Redistributions in bytecode form must reproduce the above copyright
##   notice, this list of conditions and the following disclaimer in
##   the documentation and/or other materials provided with the
##   distribution. 

##   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
##   "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
##   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
##   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
##   HOLDERS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
##   INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
##   BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
##   OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
##   ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
##   TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
##   USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
##   DAMAGE.

"""
Decorator module, see http://pypi.python.org/pypi/decorator
for the documentation.
"""

# basic functionality
class FunctionMaker(object):
    """
    An object with the ability to create functions with a given signature.
    It has attributes name, doc, module, signature, defaults, dict and
    methods update and make.
    """
    DEF = re.compile('\s*def\s*([_\w][_\w\d]*)\s*\(')
    def __init__(self, func=None, name=None, signature=None,
                 defaults=None, doc=None, module=None, funcdict=None):
        if func:
            # func can also be a class or a callable, but not an instance method
            self.name = func.__name__
            if self.name == '<lambda>': # small hack for lambda functions
                self.name = '_lambda_' 
            self.doc = func.__doc__
            self.module = func.__module__
            if inspect.isfunction(func):
                self.signature = inspect.formatargspec(
                    formatvalue=lambda val: "", *inspect.getargspec(func))[1:-1]
                self.defaults = func.func_defaults
                self.dict = func.__dict__.copy()
        if name:
            self.name = name
        if signature is not None:
            self.signature = signature
        if defaults:
            self.defaults = defaults
        if doc:
            self.doc = doc
        if module:
            self.module = module
        if funcdict:
            self.dict = funcdict
        # check existence required attributes
        assert hasattr(self, 'name')
        if not hasattr(self, 'signature'):
            raise TypeError('You are decorating a non function: %s' % func)

    def update(self, func, **kw):
        "Update the signature of func with the data in self"
        func.__name__ = self.name
        func.__doc__ = getattr(self, 'doc', None)
        func.__dict__ = getattr(self, 'dict', {})
        func.func_defaults = getattr(self, 'defaults', None)
        callermodule = sys._getframe(3).f_globals.get('__name__', '?')
        func.__module__ = getattr(self, 'module', callermodule)
        func.__dict__.update(kw)
 
    def make(self, src_templ, evaldict=None, addsource=False, **attrs):
        "Make a new function from a given template and update the signature"
        src = src_templ % vars(self) # expand name and signature
        evaldict = evaldict or {}
        mo = FunctionMaker.DEF.match(src)
        if mo is None:
            raise SyntaxError('not a valid function template\n%s' % src)
        name = mo.group(1) # extract the function name
        reserved_names = set([name] + [
            arg.strip(' *') for arg in self.signature.split(',')])
        for n, v in evaldict.iteritems():
            if n in reserved_names:
                raise NameError('%s is overridden in\n%s' % (n, src))
        if not src.endswith('\n'): # add a newline just for safety
            src += '\n'
        try:
            code = compile(src, '<string>', 'single')
            exec code in evaldict
        except:
            print >> sys.stderr, 'Error in generated code:'
            print >> sys.stderr, src
            raise
        func = evaldict[name]
        if addsource:
            attrs['__source__'] = src
        self.update(func, **attrs)
        return func

def decorator(caller, func=None):
    """
    decorator(caller) converts a caller function into a decorator;
    decorator(caller, func) decorates a function using a caller.
    """
    if func is None: # returns a decorator
        fun = FunctionMaker(caller)
        first_arg = inspect.getargspec(caller)[0][0]
        src = 'def %s(%s): return _call_(caller, %s)' % (
            caller.__name__, first_arg, first_arg)
        return fun.make(src, dict(caller=caller, _call_=decorator),
                        undecorated=caller)
    else: # returns a decorated function
        fun = FunctionMaker(func)
        src = """def %(name)s(%(signature)s):
    return _call_(_func_, %(signature)s)"""
        return fun.make(src, dict(_func_=func, _call_=caller), undecorated=func)

# --- end decorator ---

def dry(message, func, *args, **kw):
    log.info(message)
    
    if not options.dry:
        return func(*args, **kw)

@decorator
def log_call(func, *args, **kw):
    _log_function_call(func, *args, **kw)
    return func(*args, **kw)

def _log_function_call(func, *args, **kw):
    message = func.__name__
    if args:
        message += ' ' + ' '.join(map(str, args))
    if kw:
        kw_str = ' '.join(['%s %r' % (k, v) for k, v in kw.iteritems()])
        message += '(' + kw_str + ')'
    log.info(message)

@decorator
def dry_guard(func, *args, **kw):
    _log_function_call(func, *args, **kw)
    if not options.dry:
        return func(*args, **kw)
