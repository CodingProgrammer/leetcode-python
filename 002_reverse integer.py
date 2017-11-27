class Solution(object):
    def reverse(self, x):
        if (x < 0):
            flag = 1
            x = -x
        else:
            flag = 0
        if (x > 2**31):
            return 0
        else:
            tem ='%d' %x
            tem = tem[::-1]
            tem = re.sub("\D", "", tem)
            a = string.atoi(tem)
            if (a > 2**31):
                return 0
            if (1 == flag):
                return -a
            else:
                return a
