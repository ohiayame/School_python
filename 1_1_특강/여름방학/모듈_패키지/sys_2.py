import sys 
import os

# 현재 sys.path출력
print("Current sys.pash:")
for path in sys.path:
    print(path)

# 새로운 경로 추가
my_module = os.getcwd() + "\sub_module"
sys.path.append(my_module)

# 경로 추ㅜ가 후 sys.path출력
print("\nUpdated sys.path:")
for path in sys.path:
    print(path)