class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        _count = defaultdict(int)
        _max = -float('inf')
        l = 0
        for r in range(len(answerKey)):
            _count[answerKey[r]] += 1
            while _count['T'] > k and  _count['F'] > k:
                 _count[answerKey[l]] -= 1
                 l += 1
            _max = max(_max, r-l+1)
        return _max         
            
