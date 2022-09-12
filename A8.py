class ClassA:
    def method1(self):
         print("This is a base class ")
class ClassB(Class A):
    def method2(self):
        print("This is derived class-1")
class ClassC(ClassA):
    def method3(self):
        print("This is a derived class-2")
ob1=ClassC()
ob1.method1()
ob1.method3()
ob2=ClassB()
ob2.method2()
ob2.method1()
