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
# def message(): 
#     app_1 = ttk.Window("50 30 20 " ,"litera", resizable=(False, False))
# ------ create app
app = ttk.Window("50 30 20 " ,"litera", resizable=(False, False))
#-----------salary_text
salary_lbl = ttk.Label(app ,text="Please enter your salary and month")
salary_lbl.grid(columnspan=2, row=0, sticky=ttk.N, padx=20, pady=5)
#------------salary
salary_lbl_1 = ttk.Label(app ,text="salary:")
salary_lbl_1.grid(column=0, row=1, sticky=ttk.W, padx=10, pady=5)
salary_entry = ttk.Entry(app,bootstyle="success" )
salary_entry.grid(column=1, row=1, sticky=ttk.W, padx=10, pady=5)
#-----------month
month_lbl = ttk.Label(app ,text="month:")
month_lbl.grid(column=0, row=2, sticky=ttk.W, padx=10, pady=5)
month_entry = ttk.Entry(app, bootstyle="success")
month_entry.grid(column=1, row=2, sticky=ttk.W, padx=10, pady=5)
#-----------
needs_lbl = ttk.Label(app , text="needs:")
needs_lbl.grid(column=0, row=4, sticky=ttk.W, padx=10, pady=5)
#-----------
save_lbl = ttk.Label(app , text="save:")
save_lbl.grid(column=0,row=5, sticky=ttk.W, padx=10, pady=5)
#-----------
dreams_lbl = ttk.Label(app, text="dreams:")
dreams_lbl.grid(column=0, row=6, sticky=ttk.W, padx=10, pady=5)
#----------
submit_btn = ttk.Button(app, bootstyle="danger" , text="apply", command = calculate_503020)
submit_btn.grid(columnspan=2, row=3, sticky=ttk.EW, padx=10, pady=5)

# message_btm = ttk.Button(app ,text="click",command=message )
# message_btm.grid(column=0 , row= 4)
app.mainloop()