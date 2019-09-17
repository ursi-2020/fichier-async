from src.app_dic import get_path

class File_manager():
    def __init__(self, app, path):
        self.app = app
        self.path_to_read = path

    def write_to_distant(self, content):
        f = open(get_path(self.app))
        f.write(content)
        f.close()
        return False

    def write(self):
        try:
            f = open(self.path_to_read, "w+")
            content = f.read()
            f.close()
            return write_to_distant(content)
        except Exception:
            print(self.path_to_read + ' error, maybe bad access or directory not available')
            return False
