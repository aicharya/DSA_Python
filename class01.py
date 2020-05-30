class ClassName():
    test = "Hello!"
    
    def test_function(self):
        print("This is a message inside the class")
 
 
    def addNum(self, x, y):
        return x + y       


#test_object = ClassName()
#print(test_object.test)
#test_object.test_function()
myObj = ClassName()
print( myObj.addNum(10,20) )

