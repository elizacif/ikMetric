import tkinter as tk
from tkinter import font
import random

#----- jautajumi, atbildes teksts
jautajumi = [
    "How many milliliters are in a tablespoon (US)?", 
    "How many grams are in a cup of all-purpose flour?", 
    "How many milliliters are in a teaspoon (UK)?", 
    "How many grams are in a cup of sugar?", 
    "How many grams are in a pound?", 
    "How many milliliters are in a cup (US)?", 
    "How many ounces are in 1 liter?", 
    "How many teaspoons are in 1 tablespoon?", 
    "How many grams are in a cup of butter?", 
    "How many milliliters are in a quart (US)?", 
    "How many cups are in a liter?", 
    "How many grams are in a cup of rice?", 
    "How many milliliters are in a pint (UK)?", 
    "How many tablespoons are in 1/4 cup?", 
    "How many grams are in a cup of milk?", 
    "How many milliliters are in 1 ounce?", 
    "How many grams are in 1 tablespoon of butter?", 
    "How many teaspoons are in 1/4 teaspoon?", 
    "How many milliliters are in a gallon (US)?", 
    "How many ounces are in 100 grams?", 
    "How many cups are in 500 milliliters?", 
    "How many grams are in a cup of chopped vegetables?", 
    "How many milliliters are in a deciliter?", 
    "How many tablespoons are in 1/2 cup?", 
    "How many grams are in a medium-sized egg?", 
    "How many milliliters are in a shot (US)?", 
    "How many teaspoons are in 1/4 cup?", 
    "How many grams are in 1 cup of cooked pasta?", 
    "How many milliliters are in a tablespoon (UK)?", 
    "How many grams are in 1 cup of cooked chicken?"
]
atbildes = [
    "15 ml", "10 ml", "14.79 ml", 
    "100 grams", "150 grams", "120 grams",  
    "5 ml", "4.93 ml", "3 ml",  
    "250 grams", "200 grams", "180 grams",  
    "400 grams", "453.59 grams", "500 grams", 
    "250 ml", "236.59 ml", "240 ml",  
    "40 oz", "33.81 oz", "30 oz",  
    "3 teaspoons", "5 teaspoons", "2 teaspoons",  
    "227 grams", "200 grams", "250 grams",  
    "1,000 ml", "946.35 ml", "800 ml",  
    "5 cups", "4 cups", "4.23 cups",  
    "150 grams", "185 grams", "200 grams",  
    "600 ml", "568 ml", "500 ml",  
    "3 tablespoons", "4 tablespoons", "5 tablespoons",  
    "200 grams", "240 grams", "250 grams",  
    "29.57 ml", "25 ml", "30 ml",  
    "14 grams", "12 grams", "20 grams",  
    "1 teaspoon", "0.5 teaspoons", "0.25 teaspoons",  
    "3,000 ml", "4,000 ml", "3,785.41 ml",  
    "3.53 oz", "4 oz", "2.5 oz",  
    "2 cups", "1.5 cups", "2.11 cups",  
    "200 grams", "150 grams", "120 grams",  
    "50 ml", "200 ml", "100 ml",  
    "8 tablespoons", "10 tablespoons", "6 tablespoons",
    "60 grams", "50 grams", "40 grams", 
    "50 ml", "44.36 ml", "40 ml",  
    "12 teaspoons", "8 teaspoons", "10 teaspoons",
    "120 grams", "140 grams", "160 grams",  
    "15 ml", "12 ml", "10 ml",  
    "120 grams", "140 grams", "160 grams"
]
pareizas_atbildes = [
    "14.79 ml", "120 grams", "4.93 ml", "200 grams", "453.59 grams", "236.59 ml", "33.81 oz", "3 teaspoons", "227 grams", "946.35 ml", 
    "4.23 cups", "185 grams", "568 ml", "4 tablespoons", "240 grams", "29.57 ml", "14 grams", "0.25 teaspoons", "3,785 ml", "3.53 oz", 
    "2.11 cups", "150 grams", "100 ml", "8 tablespoons", "50 grams", "44.36 ml", "12 teaspoons", "140 grams", "15 ml", "140 grams"
]

seciba = list(range(len(jautajumi)))
random.shuffle(seciba)
points = 0
jaut_num = 1

#----- funkcijas
def skata_maina(oldskats, newskats):
    newskats.pack(fill='both', expand=True)
    oldskats.pack_forget()

    for i in oldskats.grid_slaves():
        i.grid_forget()
def restart():
    global points, jaut_num
    points = 0
    jaut_num = 1
    random.shuffle(seciba)

def show_question():
    global points, jaut_num
    for i in range(3):
        jaut_skats.columnconfigure(i, weight=2)
    for i in range(8):
        jaut_skats.rowconfigure(i, weight=1)
    jaut_bg = tk.Label(jaut_skats, image=bgimage)
    jaut_bg.grid(row=0, rowspan=8, column=0, columnspan=3)


    jaut_skaits = tk.Label(jaut_skats, text=f'{jaut_num}/10', bg='#f0d3c1')
    jaut_skaits.grid(row=5, column=0, sticky='swe', padx=40)

    gained_points = tk.Label(jaut_skats, text=f'{points}.pts', bg='#f0d3c1')
    gained_points.grid(row=5, column=2, sticky='swe', padx=40)
    
    jaut = jautajumi[seciba[jaut_num-1]]
    jaut_label = tk.Label(jaut_skats, text=f'{jaut_num}. {jaut}', bg='#f0d3c1')
    jaut_label.grid(row=6, column=0, columnspan=3, sticky='swe', padx=30)

    ans_range = atbildes[seciba[jaut_num-1] * 3: seciba[jaut_num-1] * 3 + 3]
    random.shuffle(ans_range)
    for i in range(3):
        ans = ans_range[i]
        ans_button = tk.Button(jaut_skats, text=ans, height=1, width=20,  command=lambda ans=ans: check_answer(ans), bg='#f6c8b9', bd=0, activebackground='#f5a7a5')
        ans_button.grid(row=7, column=i, sticky='nwe', padx=10, pady=10)
        hover_change(ans_button, '#f4b79f', '#f6c8b9')
def check_answer(answer):
    global points, jaut_num
    for i in jaut_skats.grid_slaves():
        i.grid_forget()

    correct_answer = pareizas_atbildes[seciba[jaut_num-1]]
    if answer == correct_answer:
        points += 1
    
    if jaut_num < 10:
        jaut_num += 1
        show_question()
    else:
        skata_maina(jaut_skats, rez_skats)
        show_results()

def show_results():
    for i in range(8):
        rez_skats.rowconfigure(i, weight=1)
    for i in range(2):
        rez_skats.columnconfigure(i, weight=1)

    rez_bg = tk.Label(rez_skats, image=bgimage)
    rez_bg.grid(row=0, rowspan=8, column=0, columnspan=2)

    if points < 5:
        rez_label = tk.Label(rez_skats, text=f"""Oof... you've earned a total of {points} points - {points*10}% Correct :°/""", bg='#f0d3c1')
        try_again = tk.Label(rez_skats, text='Want to try again?', bg='#f0d3c1', width=18)

    elif points > 9:
        rez_label = tk.Label(rez_skats, text=f"""Congrats! You're a real pro B°) 
You earned a total of {points} points - {points*10}% Correct!!""", bg='#f0d3c1')
        try_again = tk.Label(rez_skats, text='Restart quiz?', bg='#f0d3c1', width=18)
    else:
        rez_label = tk.Label(rez_skats, text=f"""All done! 
You've earned a total of {points} points - {points*10}% Correct :°)""", bg='#f0d3c1')
        try_again = tk.Label(rez_skats, text='Restart quiz?', bg='#f0d3c1', width=18)
        
    rez_label.grid(row=5, column=0, columnspan=2)
    try_again.grid(row=6, column=0, columnspan=2, sticky='s')
    yes = tk.Button(rez_skats, text='Yes, please', command= lambda: [restart(), skata_maina(rez_skats, jaut_skats), show_question()], width=11, bg='#f6c8b9', bd=0, activebackground='#f5a7a5')
    yes.grid(row=7, column=0, sticky='ne', padx=10, pady=10)
    hover_change(yes, '#f4b79f', '#f6c8b9')
    no = tk.Button(rez_skats, text='No, thanks', command= lambda: window.destroy(), width=11, bg='#f6c8b9', bd=0, activebackground='#f5a7a5')
    no.grid(row=7, column=1, sticky='nw', padx=10, pady=10)
    hover_change(no, '#f4b79f', '#f6c8b9')

def hover_change(btn, hovercolor, leavecolor):
    btn.bind('<Enter>', func=lambda e: btn.config(bg= hovercolor))

    btn.bind('<Leave>', func=lambda e: btn.config(bg= leavecolor))

window = tk.Tk()
window.geometry('740x400')
window.resizable(False, False)
window.title('ikMetric')

bgimage = tk.PhotoImage(file=r'C:\Users\Eliza\Documents\11kl\Python\ikMetricX\bg.png')
window.iconbitmap(default='icon.ico')

default_font = font.nametofont('TkDefaultFont')
default_font.config(family='Segoe Script', size=12)
window.option_add('*Font', default_font)
window.option_add('*Foreground', '#351b28')
window.option_add('*activeForeground', '#860043')

#----- sākuma skats
sak_skats = tk.Frame(window)
sak_skats.pack(fill='both', expand=True)
sak_skats.columnconfigure(0, weight=1)
for i in range(6):
    sak_skats.rowconfigure(i, weight=1)

bg_label = tk.Label(sak_skats, image=bgimage)
bg_label.grid(row=0, rowspan=6)

title = tk.Label(sak_skats, text="Let's test your unit conversion knowledge!", bg='#f0d3c1')
title.grid(row=4, pady=10, sticky='s')
start = tk.Button(sak_skats, text='Start!', command=lambda: [skata_maina(sak_skats, jaut_skats), show_question()], bg='#f6c8b9', bd=0, activebackground='#eeb2ad')
start.grid(row=5, sticky='nwe', padx=300)
hover_change(start, '#f4b79f', '#f6c8b9')
#----- citi skati
jaut_skats = tk.Frame(window)
rez_skats = tk.Frame(window)

tk.mainloop()
