class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = -1, len(letters)-1
        while l+1 < r:
            mid = (l+r)//2
            if ord(letters[mid]) > ord(target):
                r = mid
            else:
                l = mid
               
        return letters[r] if ord(letters[r]) > ord(target) else letters[0]            
