class parentClass:
    def parent_method(self):
        print("This is parent")
        
        
class childClass (parentClass):
    def child_method(self):
        print("This is child class ")
        super().parent_method()
        
child_object=childClass()
child_object.parent_method()