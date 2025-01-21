import tkinter as tk

def value_check(input):
    if input.isdigit() or input == "":
        return True
    return False

def get_data():
    try:
        value_weight = float(entry_weight.get())
        value_height = float(entry_height.get())

        if value_height > 3:
            value_height /= 100

        bmi_calculator = value_weight / (value_height ** 2)
        if bmi_calculator < 18.4:
            label_output.config(text=f"BMI Value: {bmi_calculator:.2f} -- Under weight ",fg='red')
        elif bmi_calculator >= 18.5 and bmi_calculator < 25:
            label_output.config(text=f"BMI Value: {bmi_calculator:.2f} -- Normal ",fg='green')
        elif bmi_calculator >= 25 and bmi_calculator < 39.9:
            label_output.config(text=f"BMI Value: {bmi_calculator:.2f} -- Over weight ",fg='green')
        else:
            label_output.config(text=f"BMI Value: {bmi_calculator:.2f} -- Obese ",fg='red')

    except ValueError:
        label_output.config(text="Please enter a valid number!")
    except ZeroDivisionError:
        label_output.config(text="Size cannot be zero or an invalid value!")

screen = tk.Tk()
screen.geometry("300x250")
label_weight = tk.Label(screen, text='Enter Your Weight (kg) ', font=('Arial', 12, 'bold'))
label_weight.pack(padx=10, pady=7)

entry_weight = tk.Entry(screen, validate="key", font=('Arial', 12, 'bold', 'bold'), width=15)
entry_weight['validatecommand'] = (screen.register(value_check), '%P')
entry_weight.pack(padx=10, pady=7)

label_height = tk.Label(screen, text='Enter Your Height (kg) ', font=('Arial', 12, 'bold'))
label_height.pack(padx=10, pady=7)

entry_height = tk.Entry(screen, validate="key", font=('Arial', 12, 'bold'), width=15)
entry_height['validatecommand'] = (screen.register(value_check), '%P')
entry_height.pack(padx=10, pady=7)

cal_button = tk.Button(screen,text="Calculate", command=get_data)
cal_button.pack(padx=10, pady=7)

label_output = tk.Label(screen, text="", font=('Arial', 12, 'bold' ))
label_output.pack(padx=10, pady=7)


screen.mainloop()
