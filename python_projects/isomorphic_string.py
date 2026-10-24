class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_st = {}
        map_ts = {}
        
        for a, b in zip(s, t):
            if a in map_st and map_st[a] != b:
                return False
            
            if b in map_ts and map_ts[b] != a:
                return False
            
            map_st[a] = b
            map_ts[b] = a
            
        return True
    
s = Solution()
print(s.isIsomorphic("egg", "add"))
print(s.isIsomorphic("foo", "bar"))
print(s.isIsomorphic("paper", "title"))
