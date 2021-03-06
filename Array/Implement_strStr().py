Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Update (2014-11-02):
The signature of the function had been updated to return the index instead of the pointer. 
If you still see your function signature returns a char * or String, please click the reload button  
to reset your code definition.

Reference:http://yucoding.blogspot.com/2013/01/leetcode-question-34-implement-strstr.html

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        if len(haystack) < len(needle): return -1
        if not haystack or not needle or len(needle) == 0: return 0
        m = len(haystack)
        n = len(needle)
        
        for i in range(m-n+1):
            j = 0
            while j < n:
                if haystack[i+j] != needle[j]:
                    break
                j += 1
            if j == n:
                return i
        return -1  
    
    
    def strStr_1(self, haystack, needle):
        if len(haystack) < len(needle): return -1
        if haystack == None or needle == None or len(needle) == 0: return 0
        m = len(haystack)
        n = len(needle)
        
        for i in range(m-n+1):
            flag = True
            for j in range(n): # 这里如果用range的话，j所取的最后一个数为n-1, 所以不能用上面的方法判断！
                if haystack[i+j] != needle[j]:
                    flag = False
                    break
            if flag:
                return i
        
        return -1  
        


# Use the [KMP algorithm]
# https://github.com/UmassJin/Leetcode/blob/master/Algorithm/KMP_algorithm.md
    def strStr(self, haystack, needle):
        if len(haystack) < len(needle): return -1
        if not haystack or not needle or len(needle) == 0: return 0
        m = len(haystack); n = len(needle)
        
        next_arr = [-1 for i in xrange(n+1)]   
        for i in xrange(1, n+1):
            pos = next_arr[i-1]
            while pos != -1 and needle[pos] != needle[i-1]:
                    pos = next_arr[pos]
            next_arr[i] = pos + 1
        
        i = 0; j = 0
        while i < m and j < n:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next_arr[j]
        if j == n:        
            return i - j
        else:
            return -1


    def nextfuc(self,p):
        length = len(p)
        nextarr = [0] * length
        nextarr[0] = -1
        k = -1
        j = 0
        while j < length - 1:
            if k == -1 or p[k] == p[j]:
                k += 1
                j += 1
                nextarr[j] = k
            else:
                k = nextarr[k]
        return nextarr
    
    def strStr(self, haystack, needle):
        if needle == "": return 0
        nextarr = self.nextfuc(needle)
        i = 0; j = 0
        lengthh = len(haystack)
        lengthn = len(needle)
        
        while i < lengthh and j < lengthn:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = nextarr[j]
        if j == lengthn:        
            return i - j
        else:
            return -1
            
