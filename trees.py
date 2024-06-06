class tree:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    
def printpreorder(root):
    if root == None:
        return
    
    print(root.data,end=",")
    printpreorder(root.left)
    printpreorder(root.right)
             

obj1=tree(-15)
obj2=tree(10)
obj3=tree(7)
obj4=tree(115)
obj5=tree(102)
obj6=tree(15)
obj7=tree(18)
obj8=tree(3)
obj9=tree(71)
obj10=tree(80)

# obj1.data=obj1
obj1.left=obj2
obj1.right=obj3
obj2.right=obj5
obj2.left=obj4
obj3.right=obj7
obj3.left=obj6
obj5.left=obj8
obj7.left=obj9
obj7.right=obj10
printpreorder(obj1)