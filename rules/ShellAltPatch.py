# Copyright (c) 2018 Ansible, Inc.
# All Rights Reserved.

from ansiblelint import AnsibleLintRule


class ShellAltPatch(AnsibleLintRule):
    id = '306GAL'
    shortdesc = 'Use patch module'
    description = ''
    tags = ['command-shell']

    def matchtask(self, file, task):
        if task['action']['__ansible_module__'] not in ['shell', 'command']:
            return False
        if 'patch' in task['action']['__ansible_arguments__']:
            return True
        return False
