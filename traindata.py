from random import randint
from subprocess import call
import random
n = 100000
a=[]
b=[]
for row in range(n):
        lp1=str(randint(22,50))
        wp1=str(randint(90,1000))
        lp2=str(randint(22,50))
        wp2=str(randint(90,1000))
        ln1=str(randint(22,50))
        wn1=str(randint(90,1000))
        ln2=str(randint(22,50))
        wn2=str(randint(90,1000))
        temp=str(randint(25,80))
        pvdd=str(random.uniform(0.95,1.05))
        fl=open('NAND2_Leakage.sp','r')
        data=fl.readlines()
        fl.close()
        data[143]=".PARAM pvdd="+pvdd+"\n"
        data[158]="Mp1  nodez   nodea   vddd!   vddd!   pmos l="+lp1+"n w="+wp1+"n \n"
        data[159]="Mp2  nodez   nodeb   vddd!   vddd!   pmos l="+lp2+"n w="+wp2+"n \n"
        data[160]="Mn1  node4   nodea   gndd!   gndd!   nmos l="+ln1+"n w="+wn1+"n \n"
        data[161]="Mn2  nodez   nodeb   node4   gndd!   nmos l="+ln2+"n w="+wn2+"n \n"
        data[162]=".temp="+temp+"\n"
        data[194]=".DC temp "+temp+" "+temp+" "+temp+" SWEEP DATA=Var_Input\n"

        fl=open('NAND2_Leakage.sp','w')
        fl.writelines(data)
        fl.close()
        call(["hspice64","NAND2_Leakage.sp"])

        fl=open('delays_nand2.sp','r')
        data=fl.readlines()
        fl.close()

        data[161]=".temp "+temp+"\n"
        data[172]="+    pvdd="+pvdd+"\n"
        data[194]="Mp1  nodez   nodea   vddd!   vddd!   pmos l="+lp1+"n w="+wp1+"n \n"
        data[195]="Mp2  nodez   nodeb   vddd!   vddd!   pmos l="+lp2+"n w="+wp2+"n \n"
        data[196]="Mn1  node4   nodea   gndd!   gndd!   nmos l="+ln1+"n w="+wn1+"n \n"
        data[197]="Mn2  nodez   nodeb   node4   gndd!   nmos l="+ln2+"n w="+wn2+"n \n"


        fl=open('delays_nand2.sp','w')
        fl.writelines(data)
        fl.close()
        call(["hspice64","delays_nand2.sp"])

        rowdata=[]
        rowdata1=[]
        rowdata.append(lp1)
        rowdata.append(wp1)
        rowdata.append(lp2)
        rowdata.append(wp2)
        rowdata.append(ln1)
        rowdata.append(wn1)
        rowdata.append(ln2)
        rowdata.append(wn2)
        rowdata.append(temp)
        rowdata.append(pvdd)

        with open('NAND2_Leakage.ms0','r') as file:
                data=file.readlines()
        list_of=list()
        list_of.extend([float(x) for x in data[11].split()])
        rowdata1.append(list_of[0])
        list_of=list()
        list_of.extend([float(x) for x in data[16].split()])
        rowdata1.append(list_of[0])
        #print(rowdata1)
        list_of=list()
        list_of.extend([float(x) for x in data[21].split()])
        rowdata1.append(list_of[0])
        list_of=list()
        list_of.extend([float(x) for x in data[26].split()])
        rowdata1.append(list_of[0])
        with open('delays_nand2.mt0','r') as file:
                data=file.readlines()
        list_of=list()
        list_of.extend([float(x) for x in data[4].split()])
        rowdata1.append(list_of[0])
        rowdata1.append(list_of[1])
        rowdata1.append(list_of[2])
        rowdata1.append(list_of[3])
        a.append(rowdata)
        b.append(rowdata1)

import csv
with open("inputs.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(a)

with open("outputs.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(b)
        