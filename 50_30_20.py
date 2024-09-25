import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def calculate_503020():
    salary = int(salary_entry.get())
    month = int(month_entry.get())
    needs = (salary * 50 / 100)*month
    save = (needs * 30 / 100)*month
    dreams = (needs * 20 / 100)*month
    needs_lbl.configure(text=f"needs :{needs} $")
    save_lbl.configure(text=f"save :{save} $")
    dreams_lbl.configure(text=f"dream :{dreams} $")

# ------ create app
app = ttk.Window("test ttk boostrap" ,"litera")
app.geometry("400x400")
salary_lbl = ttk.Label(app ,text="Please enter your salary and month")
salary_lbl.pack()

# configure the grid
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)
#-----------
salary_lbl_1 = ttk.Label(app ,text="salary:")
salary_lbl_1.grid(column=0, row=0,pady=0)
salary_lbl.pack()
salary_entry = ttk.Entry(app,bootstyle="success" )
salary_entry.grid(column=1, row=0,pady=0)
salary_entry.pack()
#-----------
month_lbl = ttk.Label(app ,text="month:")
month_lbl.grid(column=0, row=1,pady=0)
month_lbl.pack()
month_entry = ttk.Entry(app, bootstyle="success")
month_entry.grid(column=1, row=1,pady=0)
month_entry.pack()

#-----------
#-----------
needs_lbl = ttk.Label(app , text="needs:")
needs_lbl.pack()
#----------
#-----------
save_lbl = ttk.Label(app , text="save:")
save_lbl.pack()
#----------
#-----------
dreams_lbl = ttk.Label(app, text="dreams:")
dreams_lbl.pack()
#----------

submit_btn = ttk.Button(app, bootstyle="danger" , text="apply", command = calculate_503020)
submit_btn.pack()



    


app.mainloop()