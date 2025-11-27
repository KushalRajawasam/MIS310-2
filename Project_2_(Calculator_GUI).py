#import the required module
import tkinter as tk
from tkinter import StringVar
#Create main window
main_window = tk.Tk()
#Set size
main_window.geometry('312x324')
#Giving the name
main_window.title('My Calculator')

#Global variables
expression =  ""
input_text = StringVar()

#Create 3 functions
#Function to handle number/operation button click
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

#Clear function - clear the input fields
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

#Function to evaluate the expression
def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
    except:
        input_text.set("Error")
        expression = ""

#Creating frames to organize widgets
#Top frame
input_frame = tk.Frame(main_window, width=312, height=50, bd=0, highlightbackground= "black",
                       highlightcolor="black", highlightthickness=1)
#Pack this frame using pack()
input_frame.pack(side='top')


#Create entry widgets (input field) to be places in this frame
input_field = tk.Entry(input_frame, font=('Arial', 18, 'bold'), textvariable=input_text,
                       width=50, bg="#eee", bd=0, justify='right')
#Position thr frame into the input_frame
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)


#Buttons frame
btns_frame = tk.Frame(main_window, width=312, height=272.5, bg="grey")
btns_frame.pack()

#The next row includes 2 buttons, 'Clear(clear)' and D'Divide(/)':
#Create a button widget called  btn_clearing
btn_clearing=tk.Button(btns_frame, text="Clear", fg="black", width=32, height=3, bd=0, bg="#eee",
                       cursor="hand2", command=btn_clear)


#First row of the bottom frame
btn_clearing.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
#Create a button for the division operator called btn_div
btn_div=tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee",
                  cursor="hand2", command=lambda: btn_click("/"))
#Position the button div in the grid
btn_div.grid(row=0, column=3, padx=1, pady=1)

#Second row of the bottom frame
tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee",
          cursor="hand2", command=lambda: btn_click('*')).grid(row=1, column=3, padx=1, pady=1)


#Third row of the bottom frame
tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee",
          cursor="hand2", command=lambda: btn_click('-')).grid(row=2, column=3, padx=1, pady=1)


#Fourth row of the bottom frame
tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee",
          cursor="hand2", command=lambda: btn_click('+')).grid(row=3, column=3, padx=1, pady=1)

#Last row of bottom frame
tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee",
          cursor="hand2", command=lambda: btn_click('.')).grid(row=4, column=2, padx=1, pady=1)
tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee",
          cursor="hand2", command=btn_equal).grid(row=4, column=3, padx=1, pady=1)

main_window.mainloop()
