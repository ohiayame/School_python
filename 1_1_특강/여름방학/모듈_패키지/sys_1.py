# 'sys.path'는 파이썬 인터프리터가 모듈을 찾을 때 참조하는 경로들의 리스트

import sys

print(type(sys.path)) # <class 'list'>

# sy.path 리스트에 있는 각 경로를 출력
for path in sys.path:
    print(path)