class palistr:
    def __init__(self):
        self.ispali=False

    def chkpali(self,mystr):
        print("parent")
        if mystr==mystr[::-1]:
            self.ispali=True
        else:
            self.ispali=False
        return self.ispali
class paliint:
    def __init__(self):
        self.ispali=False

    def chkpali(self,val):
        print("child")

        temp=val
        rev=0
        while temp!=0:
            rem=temp%10
            rev=(rev*10)+rem
            temp=temp//10
        if rev==val:
            self.ispali=True
        else:

            self.ispali=False

        return self.ispali

mystr=input("enter string")
stobj=palistr()
if stobj.chkpali(mystr):

    print("pis plai")
else:

    print("not plai")
val=int(input("enter val"))
intval=paliint()
if intval.chkpali(val):
    print("is pali")
else:
    print("not pali")
