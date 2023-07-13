import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import PyPDF2

def search_pdf_files():
    # Get the search string and folder path
    search_string = entry.get()
    folder_path = folder_entry.get()
#hello world
    if not search_string or not folder_path:
        messagebox.showwarning("Warning", "Please enter a search string and folder path.")
        return

    if not os.path.isdir(folder_path):
        messagebox.showwarning("Warning", "Please enter a valid folder path.")
        return

    # Iterate over the PDF files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)

            # Search for the string in the PDF file
            with open(file_path, "rb") as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    if search_string.lower() in page.extract_text().lower():
                        # Add the file path to the list of results
                        result_list.insert(END, filename)
                        break

def open_file(event):
    # Get the selected file path from the list
    selected_file = result_list.get(result_list.curselection())
    
    # Open the file with the system viewer
    file_path = os.path.join(folder_entry.get(), selected_file)
    os.startfile(file_path)

# Create the main window
window = Tk()
window.title("PDF Search")
window.configure(background="grey")

# Create the search label and entry
search_label = Label(window, text="Enter search string:", bg="grey")
search_label.pack()

entry = Entry(window, bg="white")
entry.pack()

# Create the folder selection label and entry
folder_label = Label(window, text="Enter folder path:", bg="grey")
folder_label.pack()

folder_entry = Entry(window, bg="white")
folder_entry.pack()

# Create the search button
search_button = Button(window, text="Search", command=search_pdf_files)
search_button.pack()

# Create the result list
result_list = Listbox(window, width=50)
result_list.pack()

# Bind double click event to open_file function
result_list.bind("<Double-Button-1>", open_file)

# Run the main loop
window.mainloop()
