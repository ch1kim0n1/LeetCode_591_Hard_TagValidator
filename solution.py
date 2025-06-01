class Solution(object):
    def isValid(self, code):
        s = code
        n = len(s)
        if n < 7 or s[0] != '<':
            return False
        stk = []
        i = 0
        fnd = s.find
        starts = s.startswith
        while i < n:
            if starts("<![CDATA[", i):
                if not stk:
                    return False
                j = fnd("]]>", i + 9)
                if j < 0:
                    return False
                i = j + 3
            elif starts("</", i):
                j = fnd(">", i + 2)
                if j < 0:
                    return False
                t = s[i+2:j]
                if not (1 <= len(t) <= 9 and t.isalpha() and t.isupper()):
                    return False
                if not stk or stk[-1] != t:
                    return False
                stk.pop()
                i = j + 1
                if not stk and i < n:
                    return False
            elif s[i] == '<':
                j = fnd(">", i + 1)
                if j < 0:
                    return False
                t = s[i+1:j]
                if not (1 <= len(t) <= 9 and t.isalpha() and t.isupper()):
                    return False
                stk.append(t)
                i = j + 1
            else:
                if not stk:
                    return False
                i += 1
        return not stk
