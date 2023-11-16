import shutil
import os
from os import path
import time
#######PIP요구 시 이곳에 작성

#os.system()

############################

#
#옮길 파일들 이곳에 작성
#
file1 = 'hello.py'
direc1 = './asdf'
all1 = direc1+ '/'+ file1
print(all1)
#
#파일 중복 확인 과정
#
try:

    if path.exists(all1):
        print('Found duplication in target directory')
        os.remove(all1)
    else:
        print('No problem')
except:
    print('error in duplication check phase')

time.sleep(1)#파일 옮기기 준비...
#
#파일 옮기기
#
try:
    shutil.move(file1, direc1)
except:
    print('error was rasied while moving file ')



#스스로kill 명령어...

try:
    os.remove('readme.md')
except:
    print('README.md not found')
time.sleep(1)
os.remove('findme.py')
