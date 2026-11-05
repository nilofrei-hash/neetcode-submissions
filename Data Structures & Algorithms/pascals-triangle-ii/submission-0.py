class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 1:
            return [1, 1]
        elif rowIndex == 0:
            return [1]
        Liste = [1, 1]
        for i in range(rowIndex - 1):
          Result = [1]
          
          for m in range(len(Liste) - 1):
            Result.append(Liste[m] + Liste[m + 1])
          Result.append(1)
          Liste = Result 
        return Liste 

        