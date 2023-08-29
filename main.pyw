from subprocess import Popen, PIPE
from sys import executable
from json import load

p = Popen([
    executable, '-m', 'pip', 'list', '--outdated', '--format=json',
    '--disable-pip-version-check'
],
          stdout=PIPE).stdout
for i in load(p):
    Popen([executable, '-m', 'pip', 'install', '--upgrade', i['name']])