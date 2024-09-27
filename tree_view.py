import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# default data:
capital = 4000
capital_growth_percentage = 10
need_percentage = 50
dream_percentage = 30
save_percentage = 20
number_months = 12
month_number = 1
#---------------------------

# ------ create app
app = ttk.Window("50 30 20 " ,"litera", resizable=(False, False))

# ------ create frame
panel = ttk.Frame(app, padding=(2, 1))
panel.grid()

# ------ create Treeview
tv = ttk.Treeview(panel, show='headings', height= number_months)
# ------ create Treeview columns
tv.configure(columns=(
    'month', 'capital', 'need', 
    'dream', 'save'
))

for col in tv['columns']:
    tv.heading(col, text=col.title(), anchor=W)

# ------ display Treeview by grid
tv.grid()

# ------ determine month column width
tv.column('month', width=100, stretch=True)
# ------calculate result of each month and insert into the treeview
for month in range(1, number_months + 1):
    needs = (capital * need_percentage / 100)
    dreams = (capital * dream_percentage / 100)
    saves = (capital * save_percentage / 100)
    tv.insert('',
              'end',
              month, 
              values=(
                  round(month , 2),
                  round(capital, 2),
                  round(needs, 2),
                  round(dreams, 2),
                  round(saves, 2))
    )
    capital += capital * capital_growth_percentage / 100

app.mainloop()