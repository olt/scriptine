scriptine - Python shell scripting made easy
============================================

:Author: Oliver Tonnhofer <olt@bogosoft.com>

Introduction
~~~~~~~~~~~~

The primary goal of ``scriptine`` is to make it easy to write shell scripts
with python.

Scriptine does two things to solve this goal:
 
* Make it easy to create scripts and commands.
* Make it easy to work with files, directories and other shell commands.

To create commands with scriptine, you just create a normal python function for each command of your script and scriptine handles the rest. It creates command line option parser and calls the right function with the right options.

The second part of scriptine is a bunch of convenience classes and functions that make it easy to work with files, directories and other shell commands.
It abstracts the different python modules like `os`, `os.path`, `shutil` and `subprocess` and offers a simple and easy to use interface. `scriptine` comes with an enhanced version of Jason Orendorff's path module.


Features
--------

* Easy command creation. Each command is just a function.

  * Automatic option parsing
  * Automatic help text (``--help``)
* Log handling (with ``-v``, ``--verbose`` and ``-q``, ``--quite`` handling)
* Testing scripts in `dry-mode`. All destructive functions/methods are wrapped and will
  not be called when the ``-n`` or ``--dry-run`` option is set.
* Easy execution of other shell scripts.
* Convenient working with files and directories.


Example
-------

Here is a small example script::

    import scriptine
    
    def example_command(name, countdown=False, repeat=10):
        """Show how scriptine works."""
        if countdown:
            for i in range(repeat, 0, -1):
                print i,
        print 'Hello, %s!' % name

    if __name__ == '__main__':
        scriptine.run()

Usage of our small script::

    % python test.py 
    Usage: test.py command [options]

    Options:
      -h, --help  show this help message and exit

    Commands:
      example  Show how scriptine works.
    % python test.py example Pete
    Hello, Pete!
    % python test.py example Pete --countdown --repeat 5
    5 4 3 2 1 Hello, Pete!
    

A more complex example::

    from scriptine import run, path, log
    from scriptine.shell import call

    def to_png_command(dirname, outdir='out', extension='jpeg'):
        """
        Convert all files with extension in dirname to .png.
        Only convert if result does not exists or is older.
        
        :param dirname: where to search for images
        :param outdir: where to store the results
        :param extension: file extension to convert
        """
        outdir = path(outdir)
        if not outdir.exists(): outdir.makedirs()
        log.mark('converting %s/*.%s to %s/*.png', dirname, extension, outdir)
        for f in path(dirname).files('*.'+extension):
            outfile = outdir / f.namebase + '.png'
            if not outfile.exists() or f.newer(outfile):
                call(['convert', f, outfile])

    if __name__ == '__main__':
        run()

The help text::
    
    % python convert.py to-png  --help
    Usage: test.py to-png [options] dirname

     Convert all files with extension in dirname to .png. Only
    convert if result does not exists or is older.

    Required arguments:
    dirname: where to search for images

    Options:
      -h, --help        show this help message and exit
      --outdir=out      where to store the results
      --extension=jpeg  file extension to convert
      -n, --dry-run     don't actually do anything
      -v, --verbose     be more verbose
      -q, --quite       be more silent

And the result::

    % python convert.py to-png ~/images/ --extension gif
    ---> converting /Users/olt/images/*.gif to out/*.png
    % python convert.py to-png ~/images/ --extension gif -v
    ---> converting /Users/olt/images/*.gif to out/*.png
    INFO: call ['convert', '/Users/olt/images/foo.gif', 'out/foo.png']
    INFO: call ['convert', '/Users/olt/images/bar.gif', 'out/foo.png']

Documentation
~~~~~~~~~~~~~

The documentation can be found at http://packages.python.org/scriptine/

Development
~~~~~~~~~~~

scriptine is still in development. Some parts will be changed and some more functionality will be added. Follow the development at http://bitbucket.org/olt/scriptine/ Comments and bug fixes are welcomed.

