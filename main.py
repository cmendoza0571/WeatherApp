from tkinter import *
import weatherbackend


def weatherRetrieve():
    tfield.delete("1.0", END)
    tfield.insert(INSERT, weatherbackend.showWeather(city_value))


root = Tk()
root.geometry("1200x700")
root.title("Weather App")

Instructions = Label(root, text="Enter City:")

city_value = StringVar()
tfield = Text(root, width=46, height=10)
ExitButton = Button(root, text="Exit", bg="red", padx=25, pady=10, command=root.destroy)
LocationEntry = Entry(root, textvariable=city_value, width=40)
SearchButton = Button(root, text="Search", bg="light green", padx=25, pady=10, command=lambda: weatherRetrieve())


Instructions.place(x=475, y=200)
ExitButton.place(x=600, y=650)
SearchButton.place(x=600, y=250)
LocationEntry.place(x=550, y=200)
tfield.place(x=450, y=350)


root.mainloop()


