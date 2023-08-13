
from tkinter import *

#screen settings
window = Tk()
window.title("BMI Calculator")
window.minsize(width=450,height=200)
window.config(padx=20,pady=20)
x = window.winfo_width()
y= window.winfo_height()

#weight label
weight_label = Label(text="Enter Your Weight (kg)")
weight_label.pack()

#weight entry
weight_entry = Entry(width=15)
weight_entry.pack()

#height label
height_label = Label(text="Enter Your Height (cm)")
height_label.pack()

#height entry
height_entry = Entry(width=15)
height_entry.pack()

def bmi_calculator():
    weight = (weight_entry.get())
    height = (height_entry.get())
    if weight == "" or height == "":
        result_label.config(text="Enter your weight and height")
    else:
        try:
            bmi = round(float(weight) / ((float(height) / 100) ** 2),1)
            bmi_result(bmi)
        except:
            result_label.config(text="Please enter a valid number")

#calculate button
calculate_button = Button(text="Calculate",command=bmi_calculator)
calculate_button.pack()

#result label
result_label = Label(text = " ")
result_label.pack()
def bmi_result(bmi):
    if 0 < bmi < 18.5:
        result_label.config(text=f"Your BMI is {bmi}. You are under weight.")
    elif 18.4 < bmi < 24.9:
        result_label.config(text=f"Your BMI is {bmi}. You are normal weight.")
    elif 24.8 < bmi < 30:
        result_label.config(text=f"Your BMI is {bmi}. You are overweight.")
    elif 29 < bmi < 35:
        result_label.config(text=f"Your BMI is {bmi}. You are obese.")
    else:
        result_label.config(text=f"Your BMI is {bmi}. You are extremely obese.")

window.mainloop()
