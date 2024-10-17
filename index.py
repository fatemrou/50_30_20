import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def input_data () :
    # create empty dictioanry(dic)
    data = {}
    # add entry data into the dic
    data['capital'] = int(salary_entry.get())
    data['number_months'] = int(month_entry.get())
    # add default data into the dic:
    data['capital_growth_percentage']= 10
    data['need_percentage']= 50
    data['dream_percentage']= 30
    data['save_percentage']= 20
    # return dic as raw data
    return data
def caculate_data(raw_data):
    # ------calculate result of each month and insert into a nested dic
    calculated_info = {}
    row = 1
    for month in range(1, raw_data['number_months'] + 1):
        result = {}
        needs = (raw_data['capital'] * raw_data['need_percentage'] / 100)
        dreams = (raw_data['capital'] * raw_data['dream_percentage'] / 100)
        saves = (raw_data['capital'] * raw_data['save_percentage'] / 100)
        result['month'] = round(month , 2)
        result['capital'] = round(raw_data['capital'] , 2)
        result['needs'] = round(needs , 2)
        result['dreams'] = round(dreams , 2)
        result['saves'] = round(saves , 2)
        raw_data['capital'] += raw_data['capital'] * raw_data['capital_growth_percentage'] / 100
        calculated_info[row] = result
        row += 1
    return calculated_info
def create_tv_in_new_window(height):
    # ------ create result_window
    result_window = ttk.Window("50 30 20 " ,"litera", resizable= (False, False))
    # we need to define a global variable for tree view, because we will use it in other functions too
    global tv
    # ------ create Treeview (notice: we get number_months as height)
    tv = ttk.Treeview(result_window, show='headings' , height= height)
    # config columns for tv(tree view)
    tv.configure(columns= (
        'month', 'capital', 'need', 
        'dream', 'save'
    ))
    # introduce columns as heading
    for col in tv['columns']:
        tv.heading(col, text= col.title(), anchor= W)
    # ------ determine month column width(you can determine the width for other columns too)
    tv.column('month', width= 60, stretch= True)
    tv.grid()
def insert_data_tree_view(calculated_info):
    # ------calculate result of each month and insert into the treeview
    for key , value in calculated_info.items():
        tv.insert(
                '',
                'end',
                key, 
                values=(
                    value['month'],
                    value['capital'],
                    value['needs'],
                    value['dreams'],
                    value['saves']
                )            
        )
def do_proccess():
    raw_data = input_data()
    caculated_info = caculate_data(raw_data)
    create_tv_in_new_window(raw_data['number_months'])
    insert_data_tree_view(caculated_info)

# ------ create app
app = ttk.Window("50 30 20 " ,"litera", resizable= (False, False))
#-----------salary_text
salary_lbl = ttk.Label(app ,text="Please enter your salary and month")
salary_lbl.grid(columnspan= 2, row= 0, sticky= ttk.N, padx= 20, pady= 5)
#------------salary
salary_lbl_1 = ttk.Label(app ,text="salary:")
salary_lbl_1.grid(column= 0, row= 1, sticky= ttk.W, padx= 10, pady= 5)
salary_entry = ttk.Entry(app,bootstyle="success" )
salary_entry.grid(column= 1, row= 1, sticky= ttk.W, padx= 10, pady= 5)
#-----------month
month_lbl = ttk.Label(app ,text="month:")
month_lbl.grid(column= 0, row= 2, sticky= ttk.W, padx= 10, pady= 5)
month_entry = ttk.Entry(app, bootstyle="success")
month_entry.grid(column= 1, row= 2, sticky= ttk.W, padx= 10, pady= 5)

#-----------btn submit
submit_btn = ttk.Button(app, bootstyle= "danger" , text= "submit", command = do_proccess)
submit_btn.grid(columnspan= 2, row= 3, sticky= ttk.EW, padx= 10, pady= 5)
#-------
app.mainloop()