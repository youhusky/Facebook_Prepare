class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        begin, last = 0, len(s) - 1
        # 
        while begin <= last and s[begin] == ' ':
            begin += 1
        while begin <= last and s[last] == ' ':
            last -= 1

        # 
        if begin < last and (s[begin] == '+' or s[begin] == '-'):
            begin += 1
        num, dot, exp = False, False, False

        while begin <= last:
            # 
            if s[begin] >= '0' and s[begin] <= '9':
                num = True
            # 
            elif s[begin] == '.':
                if dot or exp:
                    return False
                dot = True
            # 
            elif s[begin] == 'e' or s[begin] == 'E':
                if exp or not num:
                    return False
                exp, num = True, False
            # 
            elif s[begin] == '+' or s[begin] == '-':
                if s[begin - 1] != 'e':
                    return False
            else:
                return False
            begin += 1
        return num