def minjump(nums):
        jumps=0
        current_jump_end=0
        far=0
        for i in range(len(nums)-1):
            far=max(far,i+nums[i])
            if i==current_jump_end:
                jumps+=1
                current_jump_end=far
        return jumps

nums1=[2,3,1,1,4]
print(minjump(nums1))
