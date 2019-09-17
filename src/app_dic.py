
app_dict = {
    "name" : "path"
}


def add_app_to_dict(name, path) :
    app_dict[name] = path

def get_path(name_app):
    return app_dict[name_app]
