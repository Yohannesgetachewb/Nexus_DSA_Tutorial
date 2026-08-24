class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        if p_len > s_len:
            return []

        s_count = [0] * 26
        p_count = [0] * 26

        a_ord = ord('a')

        for i in range(p_len):
            p_count[ord(p[i]) - a_ord] += 1
            s_count[ord(s[i]) - a_ord] += 1

        matches = 0
        for i in range(26):
            if p_count[i] == s_count[i]:
                matches += 1

        result = []

        for i in range(s_len - p_len):
            if matches == 26:
                result.append(i)

            left_idx = ord(s[i]) - a_ord
            s_count[left_idx] -= 1
            if s_count[left_idx] == p_count[left_idx]:
                matches += 1
            elif s_count[left_idx] == p_count[left_idx] - 1:
                matches -= 1

            right_idx = ord(s[i + p_len]) - a_ord
            s_count[right_idx] += 1
            if s_count[right_idx] == p_count[right_idx]:
                matches += 1
            elif s_count[right_idx] == p_count[right_idx] + 1:
                matches -= 1

        if matches == 26:
            result.append(s_len - p_len)

        return result
        
