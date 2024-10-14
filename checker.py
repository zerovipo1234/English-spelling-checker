import tkinter as tk
from spellchecker import SpellChecker

# Function to check spelling
def check_spelling():
    # Get the input text
    input_text = text_input.get("1.0", tk.END)
    words = input_text.split()

    # Initialize spell checker
    spell = SpellChecker()

    # Find misspelled words
    misspelled = spell.unknown(words)

    # Clear the output box
    output_box.config(state=tk.NORMAL)
    output_box.delete("1.0", tk.END)

    if misspelled:
        result_text = "Misspelled words and their suggestions:\n"
        for word in misspelled:
            correction = spell.correction(word)
            suggestions = ', '.join(spell.candidates(word))
            result_text += f"{word} -> {correction} (Suggestions: {suggestions})\n"
    else:
        result_text = "No spelling mistakes found!"

    # Display the result
    output_box.insert(tk.END, result_text)
    output_box.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("English Spelling Checker")
root.geometry("500x400")

# Create a text input box
text_label = tk.Label(root, text="Enter text to check:", font=("Arial", 12))
text_label.pack(pady=10)

text_input = tk.Text(root, height=6, width=50, font=("Arial", 12))
text_input.pack()

# Create a button to check spelling
check_button = tk.Button(root, text="Check Spelling", command=check_spelling, font=("Arial", 12))
check_button.pack(pady=10)

# Create an output box to show results
output_label = tk.Label(root, text="Results:", font=("Arial", 12))
output_label.pack(pady=10)

output_box = tk.Text(root, height=8, width=50, font=("Arial", 12), state=tk.DISABLED)
output_box.pack()

# Run the application
root.mainloop()
