
#calculation based on arithmetic

class Arithmetic:
    def add(self):
        a=10
        b=20
        print(a+b)

    def sub(self):
        a=10
        b=20
        print(a-b)

    def mul(self):
        a=10
        b=20
        print(a*b)

    def div(self):
        a=10
        b=20
        print(a/b)

obj=Arithmetic()
obj.add()
obj.sub()
obj.mul()
obj.div()

#calculation based on area formulas
class area:
    def area_of_rectangle(self):
        l=10
        b=8
        print(l*b)

    def area_of_triangle(self):
        h=10
        b=8
        print(0.5*h*b)

    def area_of_square(self):
        s=10
        print(s*s)

    def area_of_circle(self):
        r=8
        print(3.14*r*r)

obj1=area()
obj1.area_of_rectangle()
obj1.area_of_triangle()
obj1.area_of_square()
obj1.area_of_circle()

#calculation based on volume formulas
class volume:
    def volume_of_cuboid(self):
        l=10
        b=8
        h=5
        print(l*b*h)

    def volume_of_cube(self):
        a=10
        print(a*a*a)

    def volume_of_cone(self):
        h=20
        r=10
        print(1/h*h*3.14*r*r)

    def volume_of_cylinder(self):
        r=8
        h=20
        print(3.14*r*r*h)

obj2=volume()
obj2.volume_of_cuboid()
obj2.volume_of_cube()
obj2.volume_of_cone()
obj2.volume_of_cylinder()

# swap of two variable
class swap:
    def swap(self):
        a=5
        b=6
        a,b=b,a
        print(a,b)
obj3=swap()
obj3.swap()

#reverse of three digits
class reverse:
    def reverse(self):
        a=123
        print(str(a)[::-1])
obj4=reverse()
obj4.reverse()

#program to calculate (a+b)^2 and (a-b)^2
class formula:
    def f1(self):
        a=6
        b=4
        print(a*a+2*a*b+b*b)
    def f2(self):
        a=6
        b=4
        print(a*a+2*a*b-b*b)
obj5=formula()
obj5.f1()
obj5.f2()

#program to convert km to meter
class km_meter:
    def km_meter(self):
        km=1
        print("meter:",km*1000)
obj6=km_meter()
obj6.km_meter()

#program to convert celsius to fahrenheit
class temprature:
    def cel_fah(self):
        cel=50
        fah=(cel*1.8)+32
        print(fah)
obj7=temprature()
obj7.cel_fah()