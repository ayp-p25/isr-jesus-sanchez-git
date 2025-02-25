A = float(input("Ingrese su sueldo : \n"))
if 0.01 <= A <=3644.94 :
    LI = 0.01
    Cf = 12.88
    P = 0.10
elif 3644.95 <= A <= 7446.19 :
    LI = 3644.95
    Cf = 303.76
    P = 0.20
elif 7446.20 <= A <= 10298.35 :
    LI = 7446.20
    Cf = 10298.92 
    P = 0.30
else :
    LI = 10298.36
    Cf = 1063.92
    P = 0.35
T = ((A-LI)*P)+Cf
print("ISR : ", T)