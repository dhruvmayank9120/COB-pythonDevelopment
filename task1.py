import tkinter as tk
from tkinter import filedialog
from collections import Counter

# Function to open a text file, read it, and count unique words
def count_unique_words():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not file_path:
        return

    with open(file_path, "r") as file:
        text = file.read()

    # Tokenize text into words and remove punctuation
    words = text.split()
    words = [word.strip(".,!?()[]{}\"'") for word in words]
    words = [word.lower() for word in words]  # Convert to lowercase
    word_count = Counter(words)
    unique_words = sorted(set(words))

    # Clear previous results and content
    result_text.delete(1.0, "end")
    content_text.delete(1.0, "end")

    for word in unique_words:
        count = word_count[word]
        result_text.insert("end", f"{word}: {count}\n")

    content_text.insert("1.0", text)  # Display the content of the file

# Create the main application window
app = tk.Tk()
app.title("Word Frequency Counter")
app.geometry("600x400")
app.configure(bg='lightgray')

# Create a frame for styling
frame = tk.Frame(app, bg='white', bd=5)
frame.place(relx=0.5, rely=0.2, relwidth=0.8, relheight=0.6, anchor='n')

# Create and configure a button to open the file dialog
browse_button = tk.Button(app, text="Open Text File", command=count_unique_words, font=("Helvetica", 12, "bold"), bg='blue', fg='white')
browse_button.pack(pady=20)

# Create and configure a text widget for displaying results
result_text = tk.Text(frame, wrap='word', font=("Helvetica", 12), bg='white', fg='black')
result_text.pack(side='left', fill='both', expand=True)

# Create and configure a text widget to display the content of the file
content_text = tk.Text(frame, wrap='word', font=("Helvetica", 12), bg='white', fg='black')
content_text.pack(side='right', fill='both', expand=True)

app.mainloop()
