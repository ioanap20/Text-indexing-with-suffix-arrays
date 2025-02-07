# -*- coding: utf-8 -*-

def str_compare(a, b):
    N = min(len(a),len(b))
    for i in range(N):
        if a[i] < b[i]:
            return -1
        elif a[i] > b[i]:
            return 1

    return len(a)-len(b)

def str_compare_m(a,b, m):
    if len(a) >= m and len(b) >= m:
        # len(a) >= m and len(b) >= m
        return str_compare(a[:m], b[:m])
    else:
        # len(a) < m or len(b) > m
        return str_compare(a,b)

def longest_common_prefix(a, b):
    N = min(len(a),len(b))
    for i in range(N):
        if a[i] != b[i]:
            return i
    return N


class suffix_array:

    # Question 1
    def __init__(self, t):
        self.T = t
        self.N = len(t)
        self.suffixId = sorted(range(self.N), key=lambda i: self.T[i:])

    # Question 2
    def suffix(self, i):
        return self.T[self.suffixId[i]:]

    # Question 3
    def findL(self, S):
        m = len(S)
        l = -1
        r = self.N
        
        while r != l + 1:
            k = l + (r-l)//2
            if str_compare_m(S, self.suffix(k), m) <= 0:
                r = k
            else:
                l = k

        return l + 1
        

    def findR(self,S):
        m = len(S)
        l = -1
        r = self.N
        
        while r != l + 1:
            k = l + (r-l)//2
            if str_compare_m(S, self.suffix(k), m)  >= 0:
                l = k
            else:
                r = k
        
        return r
    
    
    # Question 4
    def findLR(self,S):
        return (self.findL(S),self.findR(S))

# Question 5
def KWIC(sa, S, c = 15):
    res = []
    l,r = sa.findLR(S)
    for i in range(l,r):
        res.append(sa.T[max(sa.suffixId[i]-c,0):min(sa.suffixId[i]+len(S)+c,sa.N)])
    return res

# Question 6
def longest_repeated_substring(sa):
    lcp = [0] * sa.N
    index = 0
    for i in range(sa.N - 1):
        lcp[i] = longest_common_prefix(sa.suffix(i), sa.suffix(i + 1))
        if lcp[i] > lcp[index]:
            index = i
    return sa.suffix(index)[:lcp[index]]
