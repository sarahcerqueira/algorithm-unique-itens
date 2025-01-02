from app.uniqueElementsTemplate import *

class UniqueNaive(UniqueElementsTemplate):
    
    def hasUniqueElements(dataList:list)->bool:
        size = len(dataList)
        i = 0
    
        while i < size - 1:
            j = i + 1
            while j < size:
                if dataList[i] == dataList[j]:
                    return False
                j += 1
            i += 1
        return True

class UniqueSort(UniqueElementsTemplate):
    def hasUniqueElements(dataList:list)->bool:
        sortedList = sorted(dataList)
        size = len(sortedList)
        i = 1
    
        while i < size:
            if sortedList[i - 1] == sortedList[i]:
                return False
            i += 1
        return True

class UniqueHash(UniqueElementsTemplate):
    def hasUniqueElements(dataList: list) -> bool:
        elementsSet = set()
        size = len(dataList)
        i = 0
    
        while i < size:
            if dataList[i] in elementsSet:
                return False
            elementsSet.add(dataList[i])
            i += 1
        return True