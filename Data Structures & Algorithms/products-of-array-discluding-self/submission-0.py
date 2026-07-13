class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # eg. nums = [1,2,4,6], i=1 output=2*4*6
        prefix = 1
        postfix = 1
        output = [1] * len(nums)

        for i in range(len(nums)):
            #range(start, stop, step)
            output[i] = prefix
            prefix *= nums[i]

        for j in range(len(nums)-1,-1,-1):
            output[j] *= postfix
            postfix *= nums[j]
 
        return output
        # return output[i] product of all the elements of nums except nums[i].
        #return output[i]