import tkinter as tk

#font settings
my_font = "Consolas"
my_font_size = 25

#window start
root = tk.Tk()

#calculating
eq = tk.StringVar(value="")
next = tk.BooleanVar(value=False)

def typenum(text):
    ops = ["+","-","/","*"]
    if next.get() == True:
        if text not in ops:    
            eq.set("")
            next.set(False)
        else:
            next.set(False)
    try:
        if text != "=":
            eq.set(eq.get() + str(text))
        else:
            ans = eval(eq.get(), {"__builtins__": None}, {})
            eq.set(ans)
            next.set(True)
    except SyntaxError:
        eq.set("Syntax Error")
        next.set(True)
    except ZeroDivisionError:
        eq.set("Math Error")
        next.set(True)




#display equation

eq = tk.StringVar(value="")

display_frame = tk.Frame(root, bg="black", height=100)
display_frame.pack(fill="both",expand=True,padx=10,pady=10)

display = tk.Label(
    display_frame,
    textvariable=eq,
    font=(my_font, 24),
    fg="white",
    bg="black",
    anchor="e",
    padx=10
)
display.pack(fill="both", expand=True)

#window config

root.geometry("500x500")
root.configure(bg="black")
root.title("Calculator")

grid = tk.Frame(root)
grid.pack(fill="both", expand=True, padx=10, pady=10)

# Configure 4 columns and 3 rows to expand
for i in range(4):  
    grid.columnconfigure(i, weight=1)
for j in range(3): 
    grid.rowconfigure(j, weight=1)



#buttons
counter = 1

operations = {0:"/",1:"*",2:"+",3:"-"}
opsymbols = {0:"÷",1:"×",2:"+",3:"-"}


for j in range(3):      
    for i in range(3):  
        tk.Button(
            grid,
            text=counter,
            font=(my_font, my_font_size),
            bg="orange",
            fg="white",
            command=lambda c=counter: typenum(c) ).grid(row=2-j, column=i, sticky="nsew")
        counter += 1

tk.Button(grid,text="0",font=(my_font,my_font_size),bg="orange",fg="white",command=lambda c="0":typenum(c)).grid(row=3,column=0,sticky="nsew")
tk.Button(grid,text="•",font=(my_font,my_font_size),bg="orange",fg="white",command=lambda c=".":typenum(c)).grid(row=3,column=1,sticky="nsew")
tk.Button(grid,text="=",font=(my_font,my_font_size),bg="orange",fg="white",command=lambda c="=":typenum(c)).grid(row=3,column=2,sticky="nsew")




for x in range(4):
    tk.Button(
        grid,
        text=opsymbols[x],
        font=(my_font,my_font_size),
        bg="orange",
        fg="white",
        command= lambda c=operations[x] : typenum(c)
    ).grid(row =x,column=3,sticky="nsew")

root.mainloop()
