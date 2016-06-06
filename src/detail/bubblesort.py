#-*-coding:utf-8 -*-
'''
Created on 2016��5��31��

@author: Administrator
'''
def bubbleSort(nums):
    for j in xrange(len(nums)-1,-1,-1):  # 4,3,2,1,0
        for i in xrange(j):
            if nums[i]>nums[i+1]:
                nums[i] , nums[i+1] = nums[i+1],nums[i]
            print nums

def main():
    nums = [23,12,9,15,6]
    bubbleSort(nums)

if __name__ == "__main__":
    main()
        