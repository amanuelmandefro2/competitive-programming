class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        blocks_count = {}
        blocks_count['B'] = 0
        blocks_count['W'] = 0
        min_op = float('inf')

        for i in range(k):
            blocks_count[blocks[i]] += 1
        min_op = blocks_count['W']

        for i in range(k, len(blocks)):
            blocks_count[blocks[i-k]] -= 1
            blocks_count[blocks[i]] += 1
            min_op = min(min_op, blocks_count['W'])  


        return min_op     
        