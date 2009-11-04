from scriptine.misc import dry_guard, log_call
import subprocess

@dry_guard
def call(command):
    """
    Call `command`. `command` should be a list of the executable and
    all arguments.
    
    >>> call(['some_command', '-v', some_argument]) # doctest: +SKIP
    
    :returns: return code of the command
    """
    return subprocess.call(command)

@dry_guard
def sh(command):
    """
    Call `command` in a new shell. `command` should be a string with
    all arguments.
    
    >>> call('some_command -v arg') # doctest: +SKIP
    
    :returns: return code of the command
    """
    return subprocess.call(command, shell=True)

def backtick(command):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, bufsize=-1)
    return p.stdout.read()

backtick_ = log_call(backtick)
backtick_.__doc__ = """
Like `backtick` function, but the `command` will be called even in dry-run mode.
"""

backtick = dry_guard(backtick)
backtick.__doc__ = """
Call `command` and return the stdout from the command call as a string.
"""

