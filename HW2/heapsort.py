class Solution():
    def heapify(self,nums):
        n=len(nums)#n是list的長度
        for i in range(n,-1,-1):#從原本list的最後一個開始往前
            try:#怕index超過list，所以try
                if nums[i]<nums[2*i+1]:#開始比大小做max heap
                    nums[i],nums[2*i+1]=nums[2*i+1],nums[i]
                if nums[i]<nums[2*i+2]:
                    nums[i],nums[2*i+2]=nums[2*i+2],nums[i]
            except:
                continue
        
    def heap_sort(self,nums):
        results=[]#取出來時 裝在這裡
        n=len(nums)#n是list的長度
        for j in range(n):#有幾個數字就取幾次
            self.heapify(nums)
            results.append(nums.pop(0))#每次取最大值出來
        results.reverse()#因為是max heap取出來的list要反轉
        return results
