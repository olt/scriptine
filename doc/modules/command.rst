:mod:`scriptine.command` -- run scripts with commands
=====================================================

Module Contents
---------------

.. module:: scriptine.command

.. autofunction:: run


Command decorators
^^^^^^^^^^^^^^^^^^

These decorators set options on command functions.

.. function:: no_help
    
    Disable the ``--help`` option for this command.

.. function:: no_verbosity
    
    Disable the ``--verbose`` and ``--quite`` options for this command.

.. function:: non_strict
    
    Disable strict argument parsing. Does not report an error
    when the command is called with unknown options.

.. function:: fetch_all(arg_name)

    Pass all arguments that the parser did not matche to an options or argument
    to this named ``arg_name``.
    
    Use this decorator when you are interessted in all arguments::
    
        @fetch_all('args')
        def foo_command(required_arg, the_rest):
            print '|'.join(the_rest)
    
    The result when calling this command::
        
        % example.py foo arg1 arg2 arg3
        arg2|arg3
    
    If you are interessted in aditional options (e.g. ``--bar``) use :func:`fetch_all`
    together with the :func:`non_strict` decorator.