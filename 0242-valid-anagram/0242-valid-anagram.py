class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashmap = {}

        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1

        for c in t:

            if c not in hashmap:
                return False
            else:
                hashmap[c] -= 1

                if hashmap[c] < 0:
                    return False

        
        return True if max(hashmap.values()) == 0 else False