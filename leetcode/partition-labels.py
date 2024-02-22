class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        #declering l, r for storing left and right part oof the partition
        l, r = 0, 0
        #getting last occurance of every character 
        last_occurance = {s[i]:i for i in range(len(s))}

        for i in range(len(s)):
            #updating right side of the partition based the occurance current letter
            r = max(r, last_occurance[s[i]])
            if r == i:
                ans.append(r-l+1)
                l = i+1

        return ans            