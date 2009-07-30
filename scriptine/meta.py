import scriptine
from scriptine import path

def version_command():
    print 'scriptine ver.%s' % scriptine.__version__

def zipdist_command():
    print 'creating scriptine.zip'
    if __file__ is None:
        print 'ERROR: creating zipdist from zipped scriptine is not supported.'
        return 1
    from zipfile import ZipFile, ZIP_DEFLATED
    zipfile = ZipFile('scriptine.zip', 'w', compression=ZIP_DEFLATED)
    scripyt_src = path(__file__).dirname()
    for filename in path(scripyt_src).files('*.py'):
        arcname = path().joinpath(*filename.splitall()[-2:])
        zipfile.write(filename, arcname)
    zipfile.close()

if __name__ == '__main__':
    import sys
    if sys.argv[0] is None:
        sys.argv[0] = 'python -m scriptine.meta'
    scriptine.run()