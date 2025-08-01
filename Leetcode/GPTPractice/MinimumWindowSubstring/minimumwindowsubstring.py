class Solution(object):
    def minWindow(self, s, t):
        if len(t) > len(s): return ""
        sMap, tMap = {},{}
        counter = 0
        lindex = 0
        result = [-1,-1]
        resLength = float('infinity')
        for index,char in enumerate(t):
            tMap[char] = 1 + tMap.get(char,0)
        need = len(tMap)
        for rindex,char in enumerate(s):
            sMap[char] = 1 + sMap.get(char,0)
            
            if (char in tMap and sMap[char] == tMap[char]):
                counter +=1 

            while counter == need:
                if (rindex - lindex + 1) < resLength:
                    result = [lindex,rindex+1]
                    resLength = rindex - lindex + 1
                sMap[s[lindex]] -= 1 
                if s[lindex] in tMap and sMap[s[lindex]] < tMap[s[lindex]]:
                    counter -= 1
                lindex +=1
        lindex,rindex = result
        return s[lindex:rindex]
    
s = "ADOBECODEBANC"
t = "ABC"

theSolution = Solution()
print(theSolution.minWindow(s,t))