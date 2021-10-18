import filedatastorage
import logging

from fileobjects import DisplayInfo
from fileobjects import UploadedFile


def save_file(filename, url):
    logging.info('Saving url %s with filename %s' % (filename, url))
    uploaded_file = UploadedFile(filename, url)
    filedatastorage.save_uploaded_file(uploaded_file)


def get_uploaded_file_display(filename):
    di = DisplayInfo('File')
    di.p['name'] = filename

    if filename:
        uploaded_file = filedatastorage.get_uploaded_file(filename)
        if uploaded_file:
            di.p['url'] = uploaded_file.url
        else:
            di.add_error('No file was found for filename "%s"' % (filename))
    else:
        di.add_error('No filename provided.')

    return di
