class PPP:
    a =10
    _b=20
    __c=30

    def __privatemethod(self):
        astr = "THis is a private method"
        return astr
    
    def _protectedmethod(self):
        str = "THis is a protected method"
        return str
    
    def publicmethod(self):
        csr = "This is a pulic method"
        return csr
        print(self.privatemethod())
        print(self.__c)

obj = PPP()
print(obj.a)
print(obj._b)
#print(obj.__c)
print(obj.publicmethod())
print(obj._protectedmethod())
#print(obj.__privatemethod())