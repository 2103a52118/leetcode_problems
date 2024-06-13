class Solution:
    def leftRightDifference(self, n: List[int]) -> List[int]:
        a = []
        b=[]
        c=[]
        a.append(0)
        b.append(0)

        for i in range(len(n) - 1):
            a.append(n[i] + a[i])

        x=n[::-1]
        for i in range(len(n) - 1):
            b.append(x[i] + b[i])
        b=b[::-1]
        for i in range(len(n)):
            c.append(abs(a[i]-b[i]))
        return c

        