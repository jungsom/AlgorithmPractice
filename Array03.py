class Solution: 
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums) # k가 배열의 길이보다 클 경우를 대비
        
        rotated = nums[-k:] # k단계 회전된 배열
        remained = nums[:-k] # 나머지 배열
        
        nums[:] = rotated + remained
        