import sys

__all__ = ['warn', 'error', 'debug', 'info', 'mark']

L_DEBUG = -1
L_INFO = 0
L_MARK = 1
L_WARN = 2
L_ERROR = 3

_level = 1

def inc_log_level(n=1):
    global _level
    _level -= n

def dec_log_level(n=1):
    global _level
    _level += n

def log(msg, *args):
    print >>sys.stderr, msg % args
    sys.stderr.flush()

def mark(msg, *args):
    "log a process step"
    if _level <= L_MARK:
        log('---> ' + msg, *args)

def info(msg, *args):
    "log an info message"
    if _level <= L_INFO:
        log('INFO: ' + msg, *args)

def warn(msg, *args):
    "log a warning message"
    if _level <= L_WARN:
        log('WARN: ' + msg, *args)

def error(msg, *args):
    "log an error message"
    if _level <= L_ERROR:
        log('ERROR: ' + msg, *args)

def fatal(msg, *args):
    "log an error message and abort the script"
    log('ERROR: ' + msg, *args)
    log('aborting script...')
    sys.exit(1)


def debug(msg, *args):
    "log a debug message"
    if _level <= L_DEBUG:
        log('DEBUG: ' + msg, *args)
