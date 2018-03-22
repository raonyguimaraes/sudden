#!/usr/bin/env python3

from subprocess import call

class Sudden:

    def __init__(self):
        self.update = True
    def main(self):
        print('Main Hello World!')
    def update(self):
        call('sudo apt update', shell=True)
        call('sudo apt upgrade', shell=True)
    def install(self, tools):
        print('install {}'.format(tools))
        for tool in tools:
            print(tool)
            if tool == 'conda':
                call("wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh", shell=True)
                call("bash Miniconda3-latest-Linux-x86_64.sh", shell=True)

if __name__ == '__main__':
    sudden = Sudden()
    sudden.main()