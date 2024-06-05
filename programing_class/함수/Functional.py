# 키보드로 부터 N개의 정수를 입력 받아 리스트에 저장
def getInputValue(areNumOfInputValue):
    tempInputValueList = []
    for index in range(areNumOfInputValue):
        inputValue = input(str(index + 1) + "번째 입력 값")
        tempInputValueList.append(int(inputValue))
    
    return tempInputValueList

# 리스트에 저장된 정수 값을 오름 차순으로 정렬
def myBubbleSort(argList, asscend = True):
    for iCount in range(len(argList) - 1):
        for jCOunt in range(len(argList) - iCount - 1):
            comparisonResult = \
                argList[jCOunt] > argList[jCOunt + 1] if asscend else argList[jCOunt] < argList[jCOunt] + 1
            
            if comparisonResult:
                temp = argList[jCOunt + 1]
                argList[jCOunt + 1] = argList[jCOunt]
                argList[jCOunt] = temp

# N개의 정수를 입력 받아 오름 차순으로 정렬

# 5개의 정수를 키보드로부터 입력 후 리스트 생성
inputValueList = getInputValue(5)

# 리스트 값 정렬
myBubbleSort(inputValueList)

# 리스트 값 출력
print(inputValueList)