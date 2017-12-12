class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la = len(a)
        lb = len(b)
        if la < lb:
            a,b = b,a
        b = b.zfill(max(la,lb))
        a = list(a)
        b = list(b)
        la = len(a)
        lb = len(b)
        for i in range(la):
            a[i] = int(a[i])
        for i in range(lb):
            b[i] = int(b[i])    
        if la < lb:
            a,b = b,a


        for i in range(len(b) - 1, -1, -1):
            a[i] = (int(a[i]) + int(b[i]))
        for i in range(len(a) - 1, -1, -1):
            benwei = a[i] % 2
            jinwei = a[i] / 2
            a[i] = benwei
            if i > 0:
                a[i - 1] += jinwei
        if 0 == i and 1 == jinwei:
            a.insert(0,1)
        for i in range(len(a)):
            a[i] = str(a[i])
        #print a
        a = "".join(a)
        return a
