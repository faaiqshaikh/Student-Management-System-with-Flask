# Author: MohammedFaiq Shaikh
# Date: 15-04-2024
# Program Name: Temperature Converter
# Program Description: Program that converts temperature from Cesius to Fahrenheir and vice versa

import tkinter as tk # Import tkinter module


def validate_input(entry_value):
    """
    Validates the input
    """
    try:
        float(entry_value)
        return True
    except ValueError:
        return False

# Display text in the output field (read-only)
def display(text):
    outputEntry.config(state="normal")
    outputEntry.delete(0, tk.END)
    outputEntry.insert(0, text)
    outputEntry.config(state="readonly")
    
def fahrenheitToCelsius(fahrenheit):
    '''Converts Fahrenheit to Celsius'''
    fahrenheit = float(fahrenheit)
    celcius = (fahrenheit - 32) * 5 / 9
    return celcius

def celsiusToFahrenheit(celsius):
    '''Converts Celsius to Fahrenheit'''
    celsius = float(celsius)
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def convertButtonClick():
    '''
    Executed when Convert button is clicked
    - Writes an error message in case the temperature is invalid
    - If the temperature is valid, then converts it
    '''
    entry_value = inputEntry.get()
    # display error when the input field is empty
    if not entry_value:
        outputEntry.config(fg="red")
        display("Please enter a value.")
    
    # call necessary functions upon valid input    
    elif validate_input(entry_value):
        if conversionType.get() == "celsius":
            outputEntry.config(fg="black")
            celcius = fahrenheitToCelsius(entry_value)
            text = f"{celcius:.1f} °c"
            display(text)
        else:
            outputEntry.config(fg="black")
            fahrenheit = celsiusToFahrenheit(entry_value)
            text = f"{fahrenheit:.1f} °f"
            display(text)
    # non-numeric input will show this error    
    else:
        outputEntry.config(fg="red")
        display("invalid input!")

def clearButtonClick():
    """
    Executed when the [clear] button is clicked
    - Clears the input and output text
    - Reset the radiobutton to celsius
    """
    #clear input field
    inputEntry.delete(0, tk.END)
    #clear output field
    outputEntry.config(state="normal")
    outputEntry.delete(0, tk.END)
    outputEntry.config(state="readonly")
    # Reset the Radio button to celsius
    conversionType.set("celsius")
    

# Setup window properties
window = tk.Tk()                                         # Create a window
window.title("Temperature Converter - MohammedFaiq Shaikh") # Change the title
window.resizable(width=False, height=False)           # Window is not resizable
window.geometry("500x250")
window.iconbitmap("thermometer.ico")                        # Set the icon


# Frames
leftFrame = tk.Frame(window, bg="lightblue")
rightFrame = tk.Frame(window, bg="lightgreen")

# Labels
inputLabel = tk.Label(leftFrame, text="Input Temperature", bg="lightblue")
outputLabel = tk.Label(rightFrame, text="Output Temperature", bg="lightgreen")

# Input Entry
inputText = tk.StringVar()
inputText.set("32")
inputEntry = tk.Entry(leftFrame, width=30, textvar=inputText)

# Output Entry
outputText = tk.StringVar()
outputText.set("0.0 °C")
outputEntry = tk.Entry(rightFrame, width=30, state="readonly", textvar=outputText, cursor="no")

# Radio buttons
conversionType = tk.StringVar()
conversionType.set("celsius")
celsiusRadioButton = tk.Radiobutton(leftFrame, text="Convert to Celsius", variable=conversionType, value="celsius", bg="lightblue")
fahrenheitRadioButton = tk.Radiobutton(rightFrame, text="Convert to Fahrenheit", variable=conversionType, value="fahrenheit", bg="lightgreen")

# Buttons
clearButton = tk.Button(leftFrame, text="Clear", width=20, command=clearButtonClick)
convertButton = tk.Button(rightFrame, text="Convert", width=20, command=convertButtonClick)

# Pack widgets on the screen
leftFrame.pack(side=tk.LEFT, padx=10, pady=10)
rightFrame.pack(side=tk.RIGHT, padx=10, pady=10)

inputLabel.pack()
inputEntry.pack(ipadx=20, pady=5)
celsiusRadioButton.pack()
clearButton.pack(pady=5)

outputLabel.pack()
outputEntry.pack(ipadx=20, pady=5)
fahrenheitRadioButton.pack()
convertButton.pack(pady=5)

# Start app
window.mainloop()