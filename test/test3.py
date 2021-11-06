class Test(object):
    def __init__(self,x):
        self.x = x
        print(self.x)

    class xxx(object):
        def __init__(self,z):
            self.z = z
            print(self.z)
y = Test.xxx("ggg")