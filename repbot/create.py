from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
from github import Github
import os
import platform


def create(title, private, u):
    if private == 'Yes':
        repo = u.create_repo(title, private=True)
        print('%s was created.' % title)

        if os.name == 'posix':
            os.chdir('mnt/c/Users/Bobby/Documents/Github')
            os.system("git clone https://github.com/robaboyd/%s.git" %
                      (title))
        else:
            os.chdir('C:/Users/Bobby/Documents/Github')
            os.system("git clone https://github.com/robaboyd/%s.git" %
                      (title))
    else:
        repo = u.create_repo(title, private=False)
        print('%s was created.' % title)
        if os.name == 'posix':
            os.chdir('mnt/c/Users/Bobby/Documents/Github')
            os.system("git clone https://github.com/robaboyd/%s.git" %
                      (title))
        else:
            os.chdir('C:/Users/Bobby/Documents/Github')
            os.system("git clone https://github.com/robaboyd/%s.git" %
                      (title))
