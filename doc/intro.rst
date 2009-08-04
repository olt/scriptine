Python shell scripting made easy
================================

The primary goal of ``scriptine`` is to make it easy to write shell scripts
with python.

Scriptine does two things to solve this goal:
 
 * Make it easy to create scripts and commands.
 * Make it easy to work with files, directories and other shell commands.

To create commands with scriptine, you just create a normal python function for each command of your script and scriptine handles the rest. It creates command line option parser and calls the right function with the right options.

The second part of scriptine is a bunch of convenience classes and functions that make it easy to work with files, directories and other shell commands.
It abstracts the different python modules like :mod:`os`, :mod:`os.path`, :mod:`shutil` and :mod:`subprocess` and offers a simple and easy to use interface.



``scriptine`` scripts contain one ore more commands. Each command is
associated with a python function. ``scriptine`` handles all the command line parsing and creates nice help text for every command.

Here is a simple ``scriptine`` example:

.. literalinclude:: example_hello.py

This is all you need for a simple script with a ``hello`` command. 

Scriptine brings all the rest you expect from a good shell script::
    
    % ./example_hello.py hello --help
    Usage: example_hello.py hello [options] name

    Print nice greetings.

    Options:
      -h, --help     show this help message and exit
      --print-counter
      --repeat=10
      -n, --dry-run  don't actually do anything
    
    % ./example_hello.py hello World --repeat 3
    Hello, World!
    Hello, World!
    Hello, World!
    % ./example_hello.py hello World --repeat 3 --print-counter
    1 Hello, World!
    2 Hello, World!
    3 Hello, World!
    

This example shows some nice things that scriptine handles for you for free.
You don't need to parse the command-line manually or create a parser with
:mod:`getopt` ot :mod:`optparser`. scriptine handles the parsing and creates
formated help-text. ``bool``, ``int`` and ``float`` options behave as you
might expect.

Features
--------

* Easy command creation. Each command is just 
    * Automatic command parsing
    * Automatic help text (``--help``)

* Log handling (with ``-v``, ``--verbose`` and ``-q``, ``--quite`` handling)

* Testing scripts in `dry-mode`. All destructive functions/methods are wrapped and will
  not be called when the ``-n`` or ``--dry-run`` option is set.

