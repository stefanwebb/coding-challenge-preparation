class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        
        idx = len(a) - 1
        jdx = len(b) - 1
        carry = 0
        while jdx >= 0 or idx >= 0:
            digits = 0
            if idx >= 0:
                digits += 1 if a[idx] == '1' else 0
                idx -= 1
            
            if jdx >= 0:
                digits += 1 if b[jdx] == '1' else 0
                jdx -= 1
                
            digits += carry
            
            if digits == 0:
                ans.append('0')
                carry = 0
            elif digits == 1:
                ans.append('1')
                carry = 0
            elif digits == 2:
                ans.append('0')
                carry = 1
            else:
                ans.append('1')
                carry = 1
                
        if carry == 1:
            ans.append('1')
                
        return ''.join(reversed(ans))