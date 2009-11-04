from scriptine import path, log
import tarfile

import warnings
warnings.warn('scriptine.file module is still in development and will be changed')

class file_collection(object):
    def __init__(self):
        self.files = []
        self.base = path('.')

    def include(self, patterns, recursive=False):
        if isinstance(patterns, basestring): patterns = (patterns,)
        for pattern in patterns:
            if recursive:
                for dirname in self.base.dirs(pattern):
                    self.files.extend((f for f in dirname.walk()))
            else:
                self.files.extend((f for f in self.base.listdir(pattern)))
    
    def exclude(self, patterns):
        if isinstance(patterns, basestring): patterns = (patterns,)
        for pattern in patterns:
            self.files = [f for f in self.files if not f.fnmatch(pattern)]
    
    def __iter__(self):
        return iter(self.files)
    
    def tar(self, dest, archive_base=None):
        dest = path(dest)
        if archive_base is None:
            archive_base = path(self.dest.basename()).splitext()[0]
        tar = tarfile.open(dest, 'w:gz')
    
        for f in self:
            log.info('adding %s', f)
            tar.add(f, arcname=archive_base/f, recursive=False)
        tar.close()

