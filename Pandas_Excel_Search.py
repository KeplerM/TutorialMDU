import pandas as pd
from tkinter import ttk
df=pd.read_excel("C:\\Users\\ASUS\\Desktop\\Tutorial\\student.xlsx")

import tkinter as tk 

my_w=tk.Tk()
my_w.geometry("500x350")
my_w.title("Exercise")

l1=tk.Label(my_w, text="Search", width=5, font=18)
l1.grid(row=1, column=1, padx=3, pady=10)
e1=tk.Entry(my_w, width=10, bg='yellow', font=18)
e1.grid(row=1, column=2, padx=1)
e2=tk.Entry(my_w, width=10, bg='yellow', font=18)
e2.grid(row=1, column=3, padx=1)
b1=tk.Button(my_w, text="Search", width=7, font=18, command=lambda:my_search())
b1.grid(row=1, column=4, padx=2)

def my_search():
    l1=list(df) # List of column names
    query=e1.get().strip()
    query2=e2.get().strip()
    #str1=df['id']==int(query)
    #str1=df.gender.str.contains(query)
    #str1=df[(df.gender.str.contains(query)) & (df['id']==int(query2))] #sirve
    str1=df[(df['gender']==str(query)) & (df['id']==int(query2))]
    '''
    if query.isdigit():
        str1=df['id']==int(query)
    else:
        str1=df.name.str.contains(query,case=False)
    '''
    #str2=df['id']==int(query2)
    #df2=df[(str1)]
    #df3=df[(str2)]
    print(str1)
    #print(df3)
    str1_Label=tk.Label(my_w, text=str1, width=5, font=18)
    str1_Label.grid(row=2, column=1)
    '''
    #r_set=df2.to_numpy().tolist() #create list of listusing rows
    r_set=str1.to_numpy().tolist() #create list of listusing rows
    trv=ttk.Treeview(my_w,selectmode='browse')
    trv.grid(row=2, column=1, columnspan=3,padx=10, pady=20)
    trv['height']=10
    trv['show']='headings'
    trv['columns']=l1
    for i in l1:
        trv.column(i, width=90,anchor='c')
        trv.heading(i, text=i)
    '''
'''
    for dt in r_set:
        v=[r for r in dt]
        trv.insert("",'end', iid=v[0],values=v)
'''
my_w.mainloop()

