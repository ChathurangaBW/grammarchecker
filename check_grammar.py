import tkinter as tk
from language_check import LanguageTool

def check_grammar():
    text = text_input.get("1.0", "end-1c")  # Get the input text from the Text widget
    tool = LanguageTool('en-US')  # Initialize the language tool for English
    matches = tool.check(text)  # Check the grammar of the provided text
    display_errors(matches)

def display_errors(matches):
    errors_text.delete("1.0", "end")  # Clear any previous error messages
    if matches:
        for match in matches:
            error_message = f"Error at position {match.offset}: {match.msg}\n"
            errors_text.insert("end", error_message)
    else:
        errors_text.insert("end", "No grammar errors found.")

def rewrite_text():
    text = text_input.get("1.0", "end-1c")  # Get the input text from the Text widget
    tool = LanguageTool('en-US')  # Initialize the language tool for English
    matches = tool.check(text)  # Check the grammar of the provided text
    corrected_text = LanguageTool.correct(text, matches)  # Apply suggested corrections
    text_input.delete("1.0", "end")  # Clear the input text
    text_input.insert("end", corrected_text)  # Insert the corrected text in the Text widget

# Create the main window
window = tk.Tk()
window.title("Grammar Checking Application")

# Create the Text widget for input text
text_input = tk.Text(window, height=10, width=50)
text_input.pack()

# Create the "Check Grammar" button
check_button = tk.Button(window, text="Check Grammar", command=check_grammar)
check_button.pack()

# Create the Text widget for error messages
errors_text = tk.Text(window, height=5, width=50)
errors_text.pack()

# Create the "Rewrite Text" button
rewrite_button = tk.Button(window, text="Rewrite Text", command=rewrite_text)
rewrite_button.pack()

# Run the main event loop
window.mainloop()
