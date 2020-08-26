
import math

from tkinter import *

form = Tk()
form.title("Tension Fabric Structure")
txta = StringVar()
txtb = StringVar()
txtc = StringVar()
txtd = StringVar()
txte = StringVar()
txtp = StringVar()
txtv = StringVar()

def Analysis():
    H = E1.get()
    h = E2.get()
    L = E3.get()
    PTFE = E4.get()
    D = E5.get()
    R = E6.get()
    M = E7.get()
    b1 = E8.get()
    b2 = E9.get()
    s1 = E10.get()
    s2 = E11.get()
    s3 = E12.get()
    f1 = E13.get()
    f2 = E14.get()
    n  = E15.get()

    
    


    TensionInFabric = round(float(PTFE)*float(R),1)

    StrutCompressionForce= round(2*float(TensionInFabric)*math.cos(math.radians(float(s1))),2)

    TieDownAnchorForce = round(float(TensionInFabric)*math.sin(math.radians(float(s2)))/math.cos(math.radians(float(s3))),2)

    UpLiftForce = round(float(TieDownAnchorForce)*math.cos(math.radians(float(s3))),2)

    ConcreteBlockDepth = round((float(f1)+1)*float(UpLiftForce)/(float(M)*float(b1)*float(b2)),2)

    TotalTiedownForce = round(float(n)*float(UpLiftForce),2)

    UnfactoredMastLoad = round(float(TotalTiedownForce)/float(f2),2)
    

    txta.set(TensionInFabric)
    txtb.set(StrutCompressionForce)
    txtc.set(TieDownAnchorForce )
    txtd.set(UpLiftForce)
    txte.set(ConcreteBlockDepth)
    txtp.set(TotalTiedownForce)
    txtv.set(UnfactoredMastLoad)
    

L1 = Label(form, text = " Total Height of Structure (H) in [m]")
L1.place(x=10,y=10)

E1= Entry(form, bd=5)
E1.place(x=270,y=10)


L2 = Label(form, text = " Height to Horizonal Booms (h)in [kN] ")
L2.place(x=10,y=50)

E2= Entry(form, bd=5)
E2.place(x=270,y=50)


L3 = Label(form, text = "Length of Booms/Horizontal Struts(L)  [m]")
L3.place(x=10,y=90)

E3= Entry(form, bd=5)
E3.place(x=270,y=90)


L4 = Label(form, text = " Fabric PVC Tension (PTFE) [kN/m]")
L4.place(x=10,y=130)

E4= Entry(form, bd=5)
E4.place(x=270,y=130)


L5 = Label(form, text = "Diameter of Upper Ring Beam (D) [m]")
L5.place(x=10,y=170)

E5= Entry(form, bd=5)
E5.place(x=270,y=170)


L6 = Label(form, text = "Radius Measured in plane,Edge Cables (R) [m]")
L6.place(x=10,y=210)

E6= Entry(form, bd=5)
E6.place(x=270,y=210)




L7 = Label(form, text = "Density of Concrete (M) [kN/m^3]")
L7.place(x=10,y=240)

E7= Entry(form, bd=5)
E7.place(x=270,y=240)



L8 = Label(form, text = " Concrete Base Width (b1) in [m]")
L8.place(x=10,y=280)

E8= Entry(form, bd=5)
E8.place(x=270,y=280)


L9 = Label(form, text = " Concrete Base Length(b2)in [m] ")
L9.place(x=10,y=320)

E9= Entry(form, bd=5)
E9.place(x=270,y=320)


L10 = Label(form, text = "Boom End Horizontal Forces Angle(s1)  [Degrees]")
L10.place(x=10,y=360)

E10= Entry(form, bd=5)
E10.place(x=270,y=360)


L11 = Label(form, text = " Boom End Angle Anchor Top (s2) [Degrees]")
L11.place(x=10,y=400)

E11= Entry(form, bd=5)
E11.place(x=270,y=400)


L12 = Label(form, text = "Boom End Angle Anchor Bottom (s3) [Degrees]")
L12.place(x=10,y=440)

E12= Entry(form, bd=5)
E12.place(x=270,y=440)


L13 = Label(form, text = "Material Safety Factor (f1) ")
L13.place(x=10,y=480)

E13= Entry(form, bd=5)
E13.place(x=270,y=480)




L14 = Label(form, text = "Load Factor (f2) ")
L14.place(x=10,y=520)

E14= Entry(form, bd=5)
E14.place(x=270,y=520)

L15 = Label(form, text = "Number of Anchor Points (n) ")
L15.place(x=10,y=560)

E15= Entry(form, bd=5)
E15.place(x=270,y=560)












L16 =Label(form, text= "Edge Cable Tension (Tc) is [kN]:")
L16.place(x=10, y=660)

E16= Entry(form, bd=5, textvariable=txta)
E16.place(x=270,y=660)

L17 =Label(form, text= " Boom Compression Force (Cb) is [kN]:")
L17.place(x=10, y=710)

E17= Entry(form, bd=5, textvariable=txtb)
E17.place(x=270,y=710)

L18 =Label(form, text= "Tie Down Forces (Ta) is [kN]:")
L18.place(x=10, y=740)

E18= Entry(form, bd=5, textvariable=txtc)
E18.place(x=270,y=740)


L19 =Label(form, text= " Uplift on Tie Down Blocks (Uv) is [kN]:")
L19.place(x=10, y=780)

E19= Entry(form, bd=5, textvariable=txtd)
E19.place(x=270,y=780)

L20 =Label(form, text= "Depth of Concrete Block (d) is [m]:")
L20.place(x=10, y=820)

E20= Entry(form, bd=5, textvariable=txte)
E20.place(x=270,y=820)


L21 =Label(form, text= "Compression in Post/Mast [kN]:")
L21.place(x=10, y=860)

E21= Entry(form, bd=5, textvariable=txtp)
E21.place(x=270,y=860)


L22 =Label(form, text= "Unfactored Mast Load [kN]:")
L22.place(x=10, y=900)

E22= Entry(form, bd=5, textvariable=txtv)
E22.place(x=270,y=900)






B = Button(form, text ="Calculate", command=lambda:Analysis())
B.place(x=210, y=610)

form.geometry("600x980+10+10")

form.mainloop()
