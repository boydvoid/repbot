# url
from __future__ import print_function, unicode_literals
from .create import create
from .settings import setup
from os import path
import sys
from PyInquirer import prompt, print_json
from github import Github
import os
import platform
import json

def main():

    print('Hello')

    if path.exists("data.txt"):
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

        with open('data.txt') as json_file:
            data = json.load(json_file)
            for p in data['account']:
                user = p['username']
                password = p['password']

        g = Github(user, password)
        u = g.get_user()

        create(title, private, u)

    else:
        questions = [
            {
                'type': 'input',
                'name': 'username',
                'message': 'What is your Github Username?'
            },
            {
                'type': 'password',
                'name': 'password',
                'message': 'What is your Github Password'
            }
        ]
        answers = prompt(questions)
        setup(answers['username'], answers['password'])


if __name__ == '__main__':
    main()
