from cgitb import text
import tkinter as tk
import tempfile
import time
import math 
from tkinter.filedialog import askopenfile
from turtle import color


tmp = tempfile.NamedTemporaryFile()



tkk = tk.Tk()
outval = "check"
root_number = 1

tree_arr=[]
a = []
nnode = 0

canvas = tk.Canvas(tkk, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

result_text = tk.StringVar()
result_text.set("")

ext_time = tk.StringVar()
ext_time.set("")

input_text = tk.StringVar()
input_text.set("")



#################################################################################


def open_file():  

    input_text.set("")  
    result_text.set("") 
   
    file = askopenfile(mode ='r', filetypes =[('Text Files', '*.txt')])
    if file is not None:

       

        with open(file.name) as f:
            # print(f)
            for line in f:
                print(line)
                a.append([int(v) for v in line.split()])

        # print(a)      
                  

        data= file.read()
        outval="check2"  
        input_text.set('File : '+file.name)
        startTime = time.time()
        tree_creation(startTime)
   
    file.seek(0)   
    
    file.close() 



def calculate_btn(): 
    
    input_text.set("")  
    result_text.set("") 

    lines = user_input_text.get(1.0, "end-1c")
        
    with open(tmp.name, 'w') as f:
        f.write(lines)
    
    with open(tmp.name) as f:
        for line in f:
            a.append([int(v) for v in line.split()])
        
       
    print(a)      
                  
    user_input_text.delete(1.0, "end-1c")
    startTime = time.time()
    tree_creation(startTime)

    
def f(n,b):
    nnode = a[0][0]
    vv = 1    
    if len(b) == 1:
        return ( 1 )
    else:

        for i in range(1,len(b)):          
            for j in range(1,nnode+1):
                if b[i] == a[j][0]:
                    # print(b[i],' - ',j)
                    vv = vv * g(n,a[j])
        return ( vv)  
            
def g(n,b):
    nnode = a[0][0]
    vv = 1    
    # print(b)
    if len(b) == 1:
        return ( 1 )
    else:

        for i in range(1,len(b)):  
            for j in range(1,nnode+1):
                if b[i] == a[j][0]:
                    # print(b[i],' - ',j)
                    vv = vv * (f(n,a[j]) + g(n,a[j]) )
        return (vv )  





def tree_creation(startTime): 
    
    result_text.set("Calculating Result ....") 
    ext_time.set("") 
    
    n=1
    output = f(n,a[n])+g(n,a[n])
    print('output ',output) 
    result_text.set('TOTAL COUNT = '+str(output))
    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ', round(executionTime,2),' ',time.time(),' ',startTime)
    ext_time.set('Execution time in seconds: ' + str(round(executionTime,2)))
    a.clear()

  
    

#######################################################################






#instructions
instructions = tk.Label(tkk, text="NUMBER OF INDEPENDENT SETS IN A TREE", font="Helvetica 18 bold" )
instructions.grid(columnspan=3, column=0, row=1)

instructions = tk.Label(tkk, text="Enter Input node values. \n(First row -  number of nodes.\nThen each node with child node values in each row. \nNames of vertices must be 1,...,n)")
instructions.grid(columnspan=3, column=0, row=2)

#user input
user_input_text = tk.Text(tkk, height = 5, width = 52)
user_input_text.grid(columnspan=3, column=0, row=3)


#calculate button
Check_btn = tk.Button(tkk, text = "Calculate", command=lambda:calculate_btn(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
Check_btn.grid(columnspan=3, column=0, row=4)



output_label = tk.Label(tkk, text="OR", font="Helvetica 18 bold" ,background='gray')
output_label.grid(columnspan=3, column=0, row=5, padx=5, pady=5)



output_label = tk.Label(tkk, text="Select a tree input text file from your computer", font="Helvetica 14 bold")
output_label.grid(columnspan=3, column=0, row=6)



#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(tkk, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(columnspan=3, column=0, row=7)

#file name
output_label = tk.Label(tkk, textvariable=input_text, font="Raleway")
output_label.grid(columnspan=3, column=0, row=8)



output_label = tk.Label(tkk, textvariable=result_text , font="Helvetica 10 bold")
output_label.grid(columnspan=3, column=0, row=9)


output_exe = tk.Label(tkk, textvariable=ext_time, font="Raleway")
output_exe.grid(columnspan=3, column=0, row=10)


tkk.mainloop()
