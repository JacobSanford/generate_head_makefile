#!/usr/bin/env python
""" Generates a drush makefile-compliant module list referencing hashes
    instead of branch heads.
"""
import subprocess

# Import module list here.
from UnbScholarModules import repo_list as repo_list

for project_name, repo_data in repo_list.iteritems():
    repo_uri = repo_data['repo_uri']
    repo_branch = repo_data['repo_branch']
    get_hash_command = [
        'git',
        'ls-remote',
        repo_data['repo_uri'],
        'refs/heads/' + repo_data['repo_branch'],
    ]
    cur_hash = subprocess.check_output(get_hash_command).split()[0]

    print """projects[%(project_name)s][type] = "module"
projects[%(project_name)s][download][type] = "git"
projects[%(project_name)s][download][url] = "%(repo_uri)s"
projects[%(project_name)s][download][revision] = "%(cur_hash)s"
""" % vars()
