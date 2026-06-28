class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        l,r,t,b = 0, n-1, 0, n-1
        while (t < b):
            for i in range(b-t):
                carry = matrix[t][l+i]
                matrix[t][l+i] = matrix[b-i][l]
                matrix[b-i][l] = matrix[b][r-i]
                matrix[b][r-i] = matrix[t+i][r]
                matrix[t+i][r] = carry
            l+=1
            r-=1
            t += 1
            b -= 1




