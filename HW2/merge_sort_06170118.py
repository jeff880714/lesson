class Solution():
    def mergeList(leftList, rightList):
         if len(leftList) == 0:#如果list只有一個值，直接回傳 
             return rightList 
         elif len(rightList) == 0: 
             return leftList 
         elif leftList[0] < rightList[0]:#左右兩個list的第一個值比大小，若右邊大，就將左邊的放入，其餘的值繼續排序
             return [leftList[0]] + mergeList(leftList[1:], rightList)
         else: #與上一段相反
             return [rightList[0]] + mergeList(leftList, rightList[1:])

    def merge_sort(self,nums):
         if 1 >= len(nums):#如果list只有一個值，直接回傳 
             return nums
         centerKey = int(round(len(nums)/2))#找出中間位置
         leftList = nums[0:centerKey]
         rightList = nums[centerKey:]#將list分成左右
            
         leftData = self.merge_sort(leftList)
         rightData = self.merge_sort(rightList)# 不斷分割，直到List內剩下一個值
            
         return mergeList(leftData, rightData)#當所有list都剩一個數字，開始合併

output=Solution().merge_sort([-2,61,85,-55,94,46,69,83,75])
output

#參考資料
#https://newaurora.pixnet.net/blog/post/224658923-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95---%E4%BD%BF%E7%94%A8python
