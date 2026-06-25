class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split(" ")
        if len(pattern)!=len(words):
            return False
        ctow={}
        wtoc={}
        for c,w in zip(pattern,words):
            if c in ctow and ctow[c]!=w:
                return False
            if w in wtoc and wtoc[w]!=c:
                return False
            ctow[c]=w
            wtoc[w]=c
        return True