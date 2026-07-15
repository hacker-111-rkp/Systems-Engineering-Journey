

class NumArray(object):
    def __init__(self, nums):#__init__ never return anything 
        self.nums=nums    # nums now is stored in object    
    def sumRange(self, left, right):#---o(1)
        total=0
        for i in range(left,right+1):#o(n)
            total+=self.nums[i]
        return total
