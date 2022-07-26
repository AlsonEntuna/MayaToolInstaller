import os
MAYA_PREFS_PATH = 'maya'


def get_maya_prefs_path():
    docs_path = os.path.expanduser('~/Documents')
    return os.path.join(os.path.realpath(docs_path), MAYA_PREFS_PATH)