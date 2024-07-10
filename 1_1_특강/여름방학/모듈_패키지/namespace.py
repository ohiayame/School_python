# namespace는 식별자(변수, 함수, 클래스)가 속한 영역(scope)을 의미
# 네임스페이스 유형
# - Global(전역 네임스페이스), Local(로컬 네임스페이스), Enclosing(포함 네임스페이스), Built-in(빌트인 네임스페이스)
# 전역 네임스페이스
x = 'global x'

def outer_function():
    # Enclosing 네임스페이스
    x = 'enclosing x'
    
    def inner_function():
        # 로컬 네임스페이스
        x = 'local x'
        
        def print_values():
            # LEGB 규칙*에 따라 가장 가까운 로컬 네임스페이스에서 'x'를 찾는다
            print(x)
        
        print_values()
    inner_function()
outer_function()

# 전역 네임스페이스의 'global x' 출력
print(x)

# 'print()' 함수는 Built-in 네임스페이스에서 찾아서 호출된다



# *LEGB규칙이란

# LEGB : 파이썬은 변수를 참조할 때 다음과 같은 순서로 네임스페이스 탐색
# 1) 로컬(Local) : 현재 함수나 메서드 내의 네임스페이스
# 2) 전역(Enclosing) : 현재 함수나 메서드를 감싸고 있는 외부 함수들의 네임스페이스(중첩 함수에서 사용)
# 3) 전역(Global): 모듈 수준의 네임스페이스
# 4) 빌트인(Built-in): 파이썬이 제공하는 빌트인 네임스페이스