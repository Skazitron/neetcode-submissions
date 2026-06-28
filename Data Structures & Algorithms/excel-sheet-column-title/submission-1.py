class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ret = []

        while (columnNumber > 0):
            columnNumber -= 1
            rem = columnNumber % 26
            columnNumber //=26
            ret.append(chr(ord('A') + rem))
            

        ret.reverse()

        return "".join(ret)
        