import sys

__all__ = ['warn', 'error', 'debug', 'info']

L_DEBUG = -1
L_INFO = 0
L_MARK = 1
L_WARN = 2
L_ERROR = 3

_level = 0

def inc_log_level():
    global _level
    _level -= 1

def dec_log_level():
    global _level
    _level += 1
    
def log(msg, *args):
    print msg % args
    sys.stdout.flush()

def mark(msg, *args):
    if _level <= L_MARK:
        log('---> ' + msg, *args)

def info(msg, *args):
    if _level <= L_INFO:
        log('INFO: ' + msg, *args)

def warn(msg, *args):
    if _level <= L_WARN:
        log('WARN: ' + msg, *args)

def error(msg, *args):
    if _level <= L_ERROR:
        log('ERROR: ' + msg, *args)

def fatal(msg, *args):
    log('ERROR: ' + msg, *args)
    log('aborting script...')
    sys.exit(1)


def debug(msg, *args):
    if _level <= L_DEBUG:
        log('DEBUG: ' + msg, *args)
