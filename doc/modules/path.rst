:mod:`scriptine.path` -- work with files and directories
========================================================

Module Contents
---------------

.. module:: scriptine

.. class:: path

.. .. automethod:: path.__repr__
.. .. automethod:: path.__add__
.. .. automethod:: path.__radd__
.. .. automethod:: path.__div__
.. .. automethod:: path.__rdiv__

Operations on path
^^^^^^^^^^^^^^^^^^
.. automethod:: path.cwd
.. automethod:: path.isabs
.. automethod:: path.abspath
.. automethod:: path.normcase
.. automethod:: path.normpath
.. automethod:: path.realpath
.. automethod:: path.expanduser
.. automethod:: path.expandvars
.. automethod:: path.dirname
.. automethod:: path.basename
.. autoattribute:: path.parent
.. autoattribute:: path.name
.. autoattribute:: path.namebase
.. autoattribute:: path.ext
.. autoattribute:: path.drive
.. automethod:: path.expand
.. .. automethod:: path._get_namebase
.. .. automethod:: path._get_ext
.. .. automethod:: path._get_drive
.. automethod:: path.splitpath
.. automethod:: path.splitdrive
.. automethod:: path.splitext
.. automethod:: path.stripext
.. .. automethod:: path.splitunc
.. .. automethod:: path._get_uncshare
.. automethod:: path.joinpath
.. automethod:: path.splitall
.. automethod:: path.relpath
.. automethod:: path.relpathto
.. automethod:: path.as_working_dir


Listing, searching, walking, and matching
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. automethod:: path.listdir
.. automethod:: path.dirs
.. automethod:: path.files
.. automethod:: path.walk
.. automethod:: path.walkdirs
.. automethod:: path.walkfiles
.. automethod:: path.fnmatch
.. automethod:: path.glob

Reading and writing files
^^^^^^^^^^^^^^^^^^^^^^^^^
.. automethod:: path.open
.. automethod:: path.bytes
.. automethod:: path.write_bytes
.. .. automethod:: path._write_bytes
.. automethod:: path.text
.. automethod:: path.write_text
.. automethod:: path.lines
.. automethod:: path.write_lines
.. automethod:: path.read_md5

Querying the filesystem
^^^^^^^^^^^^^^^^^^^^^^^
.. automethod:: path.exists()
.. automethod:: path.isdir()
.. automethod:: path.isfile()
.. automethod:: path.islink()
.. automethod:: path.ismount()
.. automethod:: path.samefile(other)
.. automethod:: path.atime()
.. automethod:: path.mtime()
.. automethod:: path.ctime()
.. automethod:: path.newer
.. automethod:: path.size()
.. automethod:: path.access
.. automethod:: path.stat
.. automethod:: path.lstat
.. automethod:: path.statvfs
.. automethod:: path.pathconf

Modifying files and directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. automethod:: path.utime
.. automethod:: path.chmod
.. automethod:: path.chown
.. automethod:: path.rename
.. automethod:: path.renames

Create/delete directories
^^^^^^^^^^^^^^^^^^^^^^^^^
.. automethod:: path.mkdir
.. automethod:: path.makedirs
.. automethod:: path.rmdir
.. automethod:: path.removedirs

Modify files
^^^^^^^^^^^^
.. automethod:: path.touch
.. automethod:: path.remove
.. automethod:: path.unlink
.. automethod:: path.link
.. automethod:: path.symlink
.. automethod:: path.readlink
.. automethod:: path.readlinkabs

Shell utils
^^^^^^^^^^^
All methods except :meth:`path.install` come from :mod:`shutil`.

.. automethod:: path.copyfile
.. automethod:: path.copymode
.. automethod:: path.copystat
.. automethod:: path.copy
.. automethod:: path.copy2
.. automethod:: path.copytree
.. automethod:: path.move
.. automethod:: path.rmtree
.. automethod:: path.install

Other methods
^^^^^^^^^^^^^

.. automethod:: path.chroot
.. .. automethod:: path.startfile