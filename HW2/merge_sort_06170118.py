cclass Solution():
    def mergeList(self,left, right):
         if len(left) == 0:#如果list只有一邊有值，直接回傳 
             return right
         if len(right) == 0: 
             return left 
         if left[0] <= right[0]:#左右兩個list的第一個值比大小，若右邊大，就將左邊的放入，其餘的值繼續排序
             return [left[0]] + self.mergeList(left[1:], right)
         if left[0] >= right[0]: #與上一段相反
             return [right[0]] + self.mergeList(left, right[1:])

    def merge_sort(self,nums):
         if len(nums)<=1:#如果list只有一個值，直接回傳 
             return nums
         mid = len(nums)//2#找出中間位置
         left = nums[0:mid]
         right = nums[mid:]#將list分成左右
            
         leftData = self.merge_sort(left)
         rightData = self.merge_sort(right)# 不斷分割，直到List內剩下一個值
            
         return self.mergeList(leftData, rightData)#當所有list都剩一個數字，開始合併


#參考資料
#https://newaurora.pixnet.net/blog/post/224658923-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95---%E4%BD%BF%E7%94%A8python
