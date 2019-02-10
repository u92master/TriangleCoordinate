import math
import turtle
print("Distance Formula by Griffin Cox")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Welcome to Triangles")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
i=1
while i >0:
    xc1=float(input("Enter X of Coordinate 1___"))
    yc1=float(input("Enter Y of Coordinate 1___"))
    xc2=float(input("Enter X of Coordinate 2___"))
    yc2=float(input("Enter Y of Coordinate 2___"))
    xc3=float(input("Enter X of Coordinate 3___"))
    yc3=float(input("Enter Y of Coordinate 3___"))
    u=str(input("Enter Unit Now___"))
    #Distance1 Arguments
    Dis1Arg1=((xc2-xc1)**2)
    Dis1Arg2=((yc2-yc1)**2)
    #Distance2 Arguments
    Dis2Arg1=((xc3-xc2)**2)
    Dis2Arg2=((yc3-yc2)**2)
    #Distance3 Arguments
    Dis3Arg1=((xc1-xc3)**2)
    Dis3Arg2=((yc1-yc3)**2)
    #Define final distances
    Dis1=(math.sqrt(Dis1Arg1+Dis1Arg2))
    Dis2=(math.sqrt(Dis2Arg1+Dis2Arg2))
    Dis3=(math.sqrt(Dis3Arg1+Dis3Arg2))
    print("Line 1 (a)=", Dis1, "(",u,")")
    print("Line 2 (b)=", Dis2, "(",u,")")
    print("Line 3 (c)=", Dis3, "(",u,")")
    #Sets Arguments for Angles A and B
    Ang1Arg1=(Dis3**2+Dis2**2-Dis1**2)
    Ang1Arg2=(2*Dis3*Dis2)
    Ang2Arg1=(Dis2**2+Dis1**2-Dis3**2)
    Ang2Arg2=(2*Dis2*Dis1)
    #Defines final Angles
    Ang1=(math.acos(Ang1Arg1/Ang1Arg2))
    Ang2=(math.acos(Ang2Arg1/Ang2Arg2))
    Ang3=(3.14159265-(Ang1+Ang2))
    print("Angle 1 (A)=", (math.degrees(Ang1)),"°, (", Ang1, "radians)")
    print("Angle 2 (B)=", (math.degrees(Ang2)),"°, (", Ang2, "radians)")
    print("Angle 3 (C)=", (math.degrees(Ang3)),"°, (", Ang3, "radians)")
    print("~~~~~~~~~~~~~~~~~~~~~~~~RESTART~~~~~~~~~~~~~~~~~~~~~~~~")
    
    
    


