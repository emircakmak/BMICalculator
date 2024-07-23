from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(height=200,width=400)
FONT = ('Arial', 10, 'bold')

weight_label = Label(text="Enter Your Weight (kg)", pady=5, padx=5, font=FONT)
weight_label.pack()

weight_entry = Entry()
weight_entry.focus()
weight_entry.pack()

height_label = Label(text="Enter Your Height (cm)", padx=5, pady=5, font=FONT)
height_label.pack()

height_entry = Entry()
height_entry.pack()

def calculate():
    height = height_entry.get()
    weight = weight_entry.get()

    if weight == "" or height == "":
        write_label = Label(text="Enter both weight and height !", font=FONT, fg="red")
        write_label.pack()
    else:
        try:
            bmi = float(weight) / ((float(height) / 100) ** 2)
            result = write_text(bmi)
            write_label = Label(text=result)
        except:
            write_label = Label(text="Enter a valid number !", font=FONT, fg="red")
            write_label.pack()

def write_text(bmi):
    if 0 < bmi < 18.5:
        write_label = Label(text=f"Your BMI is {round(bmi, 2)}. You are Underweight.", font=FONT)
        write_label.pack()
    elif 18.5 < bmi < 24.9:
        write_label = Label(text=f"Your BMI is {round(bmi, 2)}. You are Normal Range.", font=FONT)
        write_label.pack()
    elif 25.0 < bmi < 29.9:
        write_label = Label(text=f"Your BMI is {round(bmi, 2)}. You are Overweight.", font=FONT)
        write_label.pack()
    elif 30.0 < bmi < 34.9:
        write_label = Label(text=f"Your BMI is {round(bmi, 2)}. You are Obese Class 1.", font=FONT)
        write_label.pack()
    elif 35.0 < bmi < 39.9:
        write_label = Label(text=f"Your BMI is {round(bmi, 2)}. You are Obese Class 2.", font=FONT)
        write_label.pack()
    elif bmi >= 40:
        write_label = Label(text=f"Your BMI is {round(bmi, 2)}. You are Obese Class 3.", font=FONT)
        write_label.pack()

def exit_button():
    window.destroy()

button = Button(text="Calculate", command=calculate, font=FONT, padx=5, pady=5, relief=FLAT, width=5)
button.pack()

exit_button = Button(text="Exit", font=FONT, command=exit_button, relief=FLAT, width=5)
exit_button.pack()

window.mainloop()