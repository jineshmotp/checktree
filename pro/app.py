import tkinter as tk
import numpy as np
from tkinter.filedialog import askopenfile



tkk = tk.Tk()
outval = "check"
root_number = 1

tree_arr=[]
a = []
nnode = 0

canvas = tk.Canvas(tkk, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)



#instructions
instructions = tk.Label(tkk, text="NUMBER OF INDEPENDENT SETS IN A TREE", font="Helvetica 18 bold" )
instructions.grid(columnspan=3, column=0, row=1)

    


#instructions
instructions = tk.Label(tkk, text="Select a tree input text file from your computer", font="Raleway")
instructions.grid(columnspan=3, column=0, row=2)
result_text = tk.StringVar()
result_text.set("")

input_text = tk.StringVar()
input_text.set("")

#######################################################################

def f(n):
    if n == 1:
        return 1
    else:
        return (g(n-1))

def g(n):
    if n == 1:
        return 1
    else:
        return (f(n-1) + g(n-1))

def mainf(n):

    subc = 0
 
    subc = subf(n-1)
    return subc

def subf(n):

    # print('subfunstion')
    subnode = len(a[n])
    m = n + 1
    subcc = 0
    subv = 0


    
    # print('length of ',a[n],' is : ',subnode, ' n  val : ', n ,' m  val : ', m )
    
    for k in range(n,0,-1):
        print(k)
        if (a[m][0] not in a[k]):
            print('value : ',a[k][0])
            subcc = subcc + 1
        
                    
        # if (a[m][0] not in a[k]):
        #     print('value : ',a[k][0])
        #     subcc = subcc + 1
    subcc = subcc + subv
    # print('sum : ',subcc)       
    return subcc

def open_file():  

    input_text.set("")  
    result_text.set("") 

   
    file = askopenfile(mode ='r', filetypes =[('Text Files', '*.txt')])
    if file is not None: 
        print(file.name)
        file1 = open(file.name, "r")

       

        with open(file.name) as f:
            for line in f:
                a.append([int(v) for v in line.split()])

        print(a)

        
        # File_data = np.loadtxt(file.name, dtype=int)
        # print(File_data)
        
        # data= file1.read()
        # outval="check2"  
        # input_text.set(data)
        # file1 = open(file.name, "r")
        # #print(str(data))
        # for line in file1:
        #     for character in line:
        #         tree_arr.append(character)
        # print(tree_arr)                

        data= file1.read()
        outval="check2"  
        input_text.set(data)
        tree_creation()

    # readlines function 
    #print("5.Output of Readlines function is ")
    #print(file1.readlines())
    #print()
    
   
    
    file1.seek(0)
    
    
    file1.close() 

#######################################################################        

def tree_creation(): 
    nnode = a[0][0]
    result_text.set("") 
    output = 0
    leaf = 0
    flag = 0

    for i in range(nnode,0,-1):
        if(len(a[i])%2 == 0):
            flag = 1
        if(len(a[i])==1):
            leaf = leaf + 1
    print('flag value : ', flag,' ',nnode)
   
    
    

    if flag == 1:

        for i in range(nnode,0,-1):
            v = mainf(i)
            print('output of ', a[i][0],' is ',v)
            output = output + v
        
        output = nnode +1

        if(leaf > 2):
            leaf =leaf * 2
            output = output + leaf

        # v = mainf(4)
        # print('output of  is ',v)
        # output = output + (pow(2,v) - 1)
        print('Total count is ',output)

    else:
        if leaf %2 == 0 :
            output = f(nnode)+g(nnode)
        else:
            output = 1+ f(nnode)+g(nnode)
        print('binary tree Total count is ',output)




    # v = mainf(4)
    # print('output of  is ',v)
    # output = output + (pow(2,v) - 1)
    print('Total count is ',output)
    result_text.set(output)
    a.clear()




#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(tkk, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(columnspan=3, column=0, row=3)

output_label = tk.Label(tkk, text="INPUT DATA", font="Helvetica 18 bold")
output_label.grid(columnspan=3, column=0, row=5)
  
output_label = tk.Label(tkk, textvariable=input_text, font="Raleway")
output_label.grid(columnspan=3, column=0, row=7)

output_label = tk.Label(tkk, text="RESULT", font="Helvetica 18 bold")
output_label.grid(columnspan=3, column=0, row=12)

output_label = tk.Label(tkk, textvariable=result_text, font="Raleway")
output_label.grid(columnspan=3, column=0, row=15)


tkk.mainloop()
