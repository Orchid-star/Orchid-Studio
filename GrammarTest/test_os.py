import os


def list_dir(root, level=0):
    for path, dirs, files in os.walk(root):
        if level == 0:
            print('    ' * level + path)
        for file in files:
            print('    ' * level + '  |___' + file)
        for sub_dir in dirs:
            print('    ' * level + '  |___' + sub_dir)
            if sub_dir[0] != '.':
                list_dir(os.path.join(path, sub_dir), level + 1)
        break


list_dir('E:\\temp\\MyClient')
