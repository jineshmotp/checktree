import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

##############################################################################################################################################




################################################################################################################################################

tkk = tk.Tk()
outval = "check"

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

def open_file():  

    input_text.set("")   
    file = askopenfile(mode ='r', filetypes =[('Text Files', '*.txt')])
    if file is not None: 
        print(file.name)
        file1 = open(file.name, "r")
        data= file1.read()
        outval="check2"  
        input_text.set(data)
        file1 = open(file.name, "r")
        #print(str(data))
        for line in file1:
            for character in line:
                if(character == 'r'):
                    print("root")
                else :
                    print(character)
        


    # readlines function 
    #print("5.Output of Readlines function is ")
    #print(file1.readlines())
    #print()
    
   
    
    file1.seek(0)
    
    
    file1.close() 

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
output_label.grid(columnspan=3, column=0, row=8)

output_label = tk.Label(tkk, textvariable=result_text, font="Raleway")
output_label.grid(columnspan=3, column=0, row=7)

canvas = tk.Canvas(tkk, width=600, height=250)
canvas.grid(columnspan=3)
canvas = tk.Canvas(tkk, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)





tkk.mainloop()
