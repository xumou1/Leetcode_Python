class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        address_index = []
        for i in nums:
            if target - i not in nums:
                continue
            else:
                if i == target - i:
                    address_sameindex = [j for j in range(len(nums)) if nums[j] == i]
                    if len(address_sameindex) < 2:
                        continue
                    else: 
                        address_index = address_sameindex
                        break

                else:
                    address_index.append(nums.index(i))
                    address_index.append(nums.index(target - i))
                    break
        
        return address_index