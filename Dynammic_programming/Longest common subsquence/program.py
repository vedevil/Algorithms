import numpy as np
with open('input.txt','r') as f:
    s1 = f.readline().split('\n')[0]
    s2 = f.readline().split('\n')[0]
    nums1=list(s1)
    nums2=list(s2)
    l1=len(nums1)
    l2=len(nums2)
    dp=np.zeros((l1+1,l2+1))
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i]==nums2[j]:
                dp[i+1][j+1]=1+dp[i][j]
            else:
                dp[i+1][j+1]=max(dp[i][j+1], dp[i+1][j])
print(dp)
print(int(dp[i+1][j+1]))