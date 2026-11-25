class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = []
        out = "" 
        for s in strs:
            enc.append(str(len(s)))
            enc.append('#')
            enc.append(s)
        
        out = "".join(enc)
        return out 


    def decode(self, s: str) -> List[str]:
        dec = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            dec.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        
        return dec
                
            


            
