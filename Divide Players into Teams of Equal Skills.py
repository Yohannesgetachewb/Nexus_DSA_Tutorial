class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        
        left, right = 0, len(skill) - 1
        target_sum = skill[left] + skill[right]
        total_chemistry = 0
        
        while left < right:
            if skill[left] + skill[right] != target_sum:
                return -1
            
            total_chemistry += skill[left] * skill[right]
            left += 1
            right -= 1
            
        return total_chemistry
