import os
import maya.cmds as cmds

def load_modules():
    pass


def get_maya_scripts_path():
    docs_path = os.path.expanduser('~/Documents')
    return os.path.join(os.path.realpath(docs_path), 'maya', 'scripts')