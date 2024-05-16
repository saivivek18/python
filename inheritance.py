'''class Bird():
    def Fly(self):
        print("almost all birds")
class parrot(Bird):
    def colour(self):
        print("green")
p1.parrot()
p1.Fly
b1.=Bird()
b1.colour()'''
'''class actor():
    def acting(self):
        print("movie,series,drama")
class singer():
    def singing(self):
        print("playback,albums,concert")
class dhanush(actor,singer):
    def perfomance(self):
        print("excellent")
obj=dhanush()
obj.perfomance()
obj.acting()
obj.singing()


class animal():
    def types(self):
        print("herbivorres and carnivores")
class elephant(animal):
    def size(self):
        print("biggest land animal")
class cheetah(animal):
    def speed(self):
        print("fastest land animal")
e1=elephant()
c1=cheetah()
e1.types()
c1.types()'''


st=[]
while True:
    print("Enter 0 - Exit")
    print("Enter 1 - top")
    print("Enter 2 - push")
    print("Enter 3 - pop")
    n=int(input())
    if n==0:
        break
    elif n==1:
        if len(st)==0:
            print("stack is empty")
        else:
            print(st[-1])
    elif n==2:
        a=int(input())
        st.append(a)
    elif n==3:
        if len(st)>0:
            st.pop()
        else:
            print("stack is empty")























