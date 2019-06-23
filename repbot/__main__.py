# url
from __future__ import print_function, unicode_literals
from .create import create
import sys
from PyInquirer import prompt, print_json
from github import Github
import os
import platform

api = 'b4a74543e5cbdf4916c387797547322f91af86e1'


questions = [
    {
        'type': 'input',
        'name': 'repo_name',
        'message': 'Name your repo'
    },
    {
        'type': 'confirm',
        'name': 'private',
        'message': 'Is this repo private? '
    }
]

answers = prompt(questions)

title = answers['repo_name']
private = answers['private']

g = Github(api)

u = g.get_user()


def main():
    print('🤖: Hello')
    args = sys.argv[1:]
    for arg in args:
        print('passed argument :: {}'.format(arg))


create(title, private, u)

if __name__ == '__main__':
    main()
