
import tkinter as tknew
from turtle import color
import random
import os



tkk = tknew.Tk()
outval = "check"
root_number = 1

tree_arr=[]
a = []
nnode = 0

canvas = tknew.Canvas(tkk, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

result_text = tknew.StringVar()
result_text.set("")

ext_time = tknew.StringVar()
ext_time.set("")

input_text = tknew.StringVar()
input_text.set("")

##############################################################################################################################3


def calculate_btn(): 

    file = open("inputfile.txt", "a")
    if file is not None:
        os.remove("inputfile.txt")

    input_text.set("")  
    result_text.set("") 

    numnode = user_input_text.get(1.0, "end-1c")
    print(numnode)  
    n = int(numnode)
    
    x = random.randint(1,n)
    print(x) 

    if x+1 <= n:
        y = random.randint(x+1,n)
        print(y) 
    else:
        y = 0
   
    file = open("inputfile.txt", "a")
    if file is not None:
        file.truncate(0)
        file.close()

    f = open("inputfile.txt", "a")
    f.write(str(n)+'\n')

    for i in range(1,n+1):
            if i != x and i+1 !=n+1:
                k = str(i)+' '+str(i+1)+'\n'
                f.write(k)
            else:
                break
    for i in range(x,n+1):            
            if i == x:
                k = str(i)+' ' 
                f.write(k)                       
            elif i == x+1:

                for j in range(x+1,y+1):  
                    print(j)
                    k = str(j)+' '
                    f.write(k) 
                k = '\n' 
                f.write(k) 
            
            # elif i == x+2:    
            #     k = str(i)+'\n' 
            #     f.write(k) 
            #     k = str(i)+'\n'
            #     f.write(k)               
            # else:
            #     if i+1 <= n:
            #         k = str(i)+' '+str(i+1)+'\n' 
            #     else:
            #         k = str(i)+'\n' 
            #     f.write(k)                
            
    for i in range(x+1,n+1):
            if i < y:
                k = str(i)+'\n'
                f.write(k)
            else:
                if i+1 <= n:
                    k = str(i)+' '+str(i+1)+'\n'
                    f.write(k)
                else: 
                    k = str(i)
                    f.write(k)

    f.close()

    result_text.set("File created with "+str(n)+" node values tree")               
    user_input_text.delete(1.0, "end-1c")


#################################################################################


#instructions
instructions = tknew.Label(tkk, text="GENERATE RANDOM TREE", font="Helvetica 18 bold" )
instructions.grid(columnspan=3, column=0, row=1)

instructions = tknew.Label(tkk, text="Enter node value to generate random Tree in file")
instructions.grid(columnspan=3, column=0, row=2)

#user input
user_input_text = tknew.Text(tkk, height = 2, width = 20)
user_input_text.grid(columnspan=3, column=0, row=4)


instructions = tknew.Label(tkk, text="")
instructions.grid(columnspan=3, column=0, row=6)

#calculate button
Check_btn = tknew.Button(tkk, text = "Generate", command=lambda:calculate_btn(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
Check_btn.grid(columnspan=3, column=0, row=8)


output_label = tknew.Label(tkk, textvariable=result_text , font="Helvetica 10 bold")
output_label.grid(columnspan=3, column=0, row=12)


instructions = tknew.Label(tkk, text="")
instructions.grid(columnspan=3, column=0, row=16)


tkk.mainloop()
