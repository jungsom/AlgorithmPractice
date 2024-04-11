class Solution:
    def removeDuplicates(self, nums):
        result = []        # 빈 배열 생성
 
        for num in nums:   # for문 사용
            if num not in result:
                result.append(num)
        nums[:] = result   # 출력할 배열로 업데이트

        return len(result) # 배열의 수 반환