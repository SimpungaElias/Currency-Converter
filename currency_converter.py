
import tkinter as tk 
from tkinter import *
import tkinter.messagebox 

root = tk.Tk()

root.title("Currency converter:SIEL")

Tops = Frame(root, bg = '#800080', pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=0)

headlabel = tk.Label(Tops, font=('lato green', 19, 'bold'), text='Currency converter :SIEL ',
					bg='#800080', fg='black')
headlabel.grid(row=1, column=0, sticky=W)

variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)

variable1.set("currency")
variable2.set("currency")


def RealTimeCurrencyConversion():
	from forex_python.converter import CurrencyRates
	c = CurrencyRates()

	from_currency = variable1.get()
	to_currency = variable2.get()

	if (Amount1_field.get() == ""):
		tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please enter valid amount.")

	elif (from_currency == "currency" or to_currency == "currency"):
		tkinter.messagebox.showinfo("Error !!",
									"Currency Not Selected.\n Please select FROM and TO Currency form menu.")

	else:
		new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
		new_amount = float("{:.4f}".format(new_amt))
		Amount2_field.insert(0, str(new_amount))

#Clearing all the data entered by the user
def clear_all():
	Amount1_field.delete(0, tk.END)
	Amount2_field.delete(0, tk.END)


CurrenyCode_list = ["RWF", "USD", "CAD", "GBP", "RUB", "EUR"]

root.configure(background='#800080')
root.geometry("400x400")

Label_1 = Label(root, font=('lato red', 27, 'bold'), text="", padx=2, pady=2, bg="#800080", fg="red")
Label_1.grid(row=1, column=0, sticky=W)

label1 = tk.Label(root, font=('lato red', 15, 'bold'), text="\t Amount : ", bg="#800080", fg="red")
label1.grid(row=2, column=0, sticky=W)

label1 = tk.Label(root, font=('lato red', 15, 'bold'), text="\t From Currency : ", bg="#800080", fg="red")
label1.grid(row=3, column=0, sticky=W)

label1 = tk.Label(root, font=('lato red', 15, 'bold'), text="\t To Currency : ", bg="#800080", fg="red")
label1.grid(row=4, column=0, sticky=W)

label1 = tk.Label(root, font=('lato red', 15, 'bold'), text="\t Converted Amount : ", bg="#800080", fg="red")
label1.grid(row=8, column=0, sticky=W)

Label_1 = Label(root, font=('lato red', 7, 'bold'), text="", padx=2, pady=2, bg="#800080", fg="red")
Label_1.grid(row=5, column=0, sticky=W)

Label_1 = Label(root, font=('lato red', 7, 'bold'), text="", padx=2, pady=2, bg="#800080", fg="red")
Label_1.grid(row=7, column=0, sticky=W)

FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list)
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list)

FromCurrency_option.grid(row=3, column=0, ipadx=45, sticky=E)
ToCurrency_option.grid(row=4, column=0, ipadx=45, sticky=E)

Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=0, ipadx=28, sticky=E)

Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=0, ipadx=31, sticky=E)

Label_9 = Button(root, font=('green', 15, 'bold'), text=" Convert ", padx=2, pady=2, bg="lightblue", fg="green",
				command=RealTimeCurrencyConversion)
Label_9.grid(row=6, column=0)

Label_1 = Label(root, font=('lato red', 7, 'bold'), text="", padx=2, pady=2, bg="#800080", fg="red")
Label_1.grid(row=9, column=0, sticky=W)

Label_9 = Button(root, font=('green', 15, 'bold'), text=" Clear All ", padx=2, pady=2, bg="lightblue", fg="green",
				command=clear_all)
Label_9.grid(row=10, column=0)


root.mainloop()




