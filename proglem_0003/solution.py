class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        known = {}
        head = answer = 0
        for i, value in enumerate(s):
            if value in known:
                p = known[value]
                if head <= p:
                    answer = max(i - head, answer)
                    head = known[value] + 1

            known[value] = i

        answer = max(len(s) - head, answer)
        return answer
