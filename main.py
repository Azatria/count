import customtkinter
root = customtkinter.CTk()
root.configure(fg_color='black')
root.geometry("300x300")
root.title("Let's count !")

customtkinter.set_appearance_mode("dark")
NumBer = 0
plus = 1
def reset():
    global NumBer 
    global plus
    NumBer = 0
    plus = 1
    print('reset !')
    Num_label.configure(text=NumBer)
    checkbox_1.deselect()
    


def button_press():
    global NumBer
    NumBer += plus
    print(NumBer)
    # global NumBer
    NUM = NumBer
    Num_label.configure(text=NUM)
    


press = customtkinter.CTkButton(root, text='count', command=button_press)
press.pack(padx=10, pady=10)
# press.grid_columnconfigure(1, weight=1).pack()

Reset = customtkinter.CTkButton(root,text='reset', command=reset)
Reset.pack(padx = 10, pady = 10)
# Reset.grid_columnconfigure(1, weight=1).pack()




check_var = customtkinter.StringVar()
def check1_on ():
    global plus
    plus = 5
    print(checkbox_1.get())
    
    if checkbox_1.get() == "off" :
        plus = 1
        
    
    
checkbox_1 = customtkinter.CTkCheckBox(master=root, text="เพิ่มที่ละ 5", fg_color='white', command = check1_on,
                                       variable= check_var, onvalue="on", offvalue="off")
checkbox_1.pack_configure(padx=20, pady=(0, 20))



entry = customtkinter.CTkEntry(root, placeholder_text=('plus'))
entry.pack()



def Entry():
    global plus
    user_input = int(entry.get())
    plus = user_input
    checkbox_1.deselect()

entry_butt = customtkinter.CTkButton(root, text='plus', command=Entry)
entry_butt.pack(pady = (20,0))

Num_label = customtkinter.CTkLabel(root,
                                   font = ("ds-digital",100, 'bold'),
                                   text_color= "green",
                                    text = "0"
                                    )
    
    


Num_label.pack(padx=10, pady=10)

root.mainloop()

