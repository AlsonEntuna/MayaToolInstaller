import maya.cmds as cmds


def main():
    # TODO: generate loading module here...
    print('HELLO WORLD')
scriptJobNum = cmds.scriptJob(event = ['NewSceneOpened', main])