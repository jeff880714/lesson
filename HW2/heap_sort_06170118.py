class Solution():
    def heapify(self,nums):
        n=len(nums)#n是list的長度
        for i in range(n,-1,-1):#從原本list的最後一個開始往前
            if 2*i+1<n and nums[i]<nums[2*i+1]:#若2*j+1在list是存在的就比大小
                nums[i],nums[2*i+1]=nums[2*i+1],nums[i]
            if 2*i+2<n and nums[i]<nums[2*i+2]:#若2*j+2在list是存在的就比大小
                nums[i],nums[2*i+2]=nums[2*i+2],nums[i]
            else:
                continue
    def heap_sort(self,nums):
        results=[]#取出來時 裝在這裡
        n=len(nums)#n是list的長度
        for j in range(n):#有幾個數字就取幾次
            self.heapify(nums)
            results.append(nums.pop(0))#每次取最大值出來
        results.reverse()#因為是max heap取出來的list要反轉
        return results
#參考資料:https://github.com/wellslu/DSA/blob/master/HW2/heap_sort_06170107.py
