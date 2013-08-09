# -*- coding: utf-8 -*-

import shlex

def main():
    try:
        username = sys.argv[1]
    except Exception as e:
        print(e, file=sys.stderr)

class Shell(object):
    def __init__(self, username, command_line, repositories_root):
        
        self.username = username
        self.args = shlex.split(command_line)
        self.command = self.args[0]
        self.repositories_root = repositories_root

