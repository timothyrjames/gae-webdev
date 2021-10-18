class DisplayInfo(object):
    def __init__(self, title):
        self.title = title
        self.errors = []
        self.p = {}

    def add_error(self, error):
        self.errors.append(error)

    def set_param(self, key, value):
        self.p[key] = value


class UploadedFile(object):
    def __init__(self, filename, url):
        self.filename = filename
        self.url = url

