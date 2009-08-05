from __future__ import with_statement
import sys
from scriptine import run
from contextlib import contextmanager
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

state = set()

@contextmanager
def stdout_capture():
    orig_stdout, orig_stderr = sys.stdout, sys.stderr
    sys.stderr.flush()
    sys.stdout.flush()
    
    sys.stdout, sys.stderr = StringIO(), StringIO()
    
    try:
        yield sys.stdout, sys.stderr
    finally:
        sys.stderr.flush()
        sys.stdout.flush()
        sys.stdout, sys.stderr = orig_stdout, orig_stderr
    

def foo1_command():
    state.add('foo1_command_called')

def foo2_command(required_arg):
    state.add('foo2_command_called')
    state.add('foo2_command_called_with_' + required_arg)

def test_foo1():
    run(args=['test_command.py', 'foo1'])
    assert 'foo1_command_called' in state

def test_foo2():
    with stdout_capture() as (stdout, stderr):
        try:
            run(args=['test_command.py', 'foo2'])
        except SystemExit:
            pass
        else:
            assert False, 'did not exit'
        stderr.seek(0)
        out = stderr.read()
        assert 'number of arguments does not match' in out
    assert 'foo2_command_called' not in state

def test_foo2_w_arg():
    run(args=['test_command.py', 'foo2', 'buzz'])
    assert 'foo2_command_called_with_buzz' in state
