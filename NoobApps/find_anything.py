import os
import json
import pandas as pd
import openpyxl
import warnings
import threading
from tkinter import Tk, filedialog, Text, Button, Scrollbar, END, Entry, Label
from concurrent.futures import ThreadPoolExecutor

# Suppress openpyxl warnings
warnings.simplefilter("ignore")

# Function to search for the user-defined term in JSON, XAML, and Excel files
def search_for_term(folder, search_term):
    results = []
    file_paths = []

    # Collect all files first for parallel processing
    for root, _, files in os.walk(folder):
        for file in files:
            file_paths.append(os.path.join(root, file))

    def process_file(file_path):
        print(f"Searching in: {file_path}")  # Logging files being searched
        try:
            # Check project.json
            if file_path.endswith("project.json"):
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if search_term in json.dumps(data):
                        return file_path

            # Check XAML files
            elif file_path.endswith(".xaml"):
                with open(file_path, "r", encoding="utf-8") as f:
                    if search_term in f.read():
                        return file_path

            # Check Excel files (.xls, .xlsx)
            elif file_path.endswith((".xls", ".xlsx")):
                engine = "openpyxl" if file_path.endswith(".xlsx") else "xlrd"
                try:
                    df = pd.read_excel(file_path, engine=engine, dtype=str)
                    if df.applymap(lambda x: search_term in str(x) if pd.notna(x) else False).any().any():
                        return file_path
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

        except (json.JSONDecodeError, FileNotFoundError, pd.errors.ParserError) as e:
            print(f"Error processing {file_path}: {e}")

        return None

    # Use ThreadPoolExecutor for parallel processing
    with ThreadPoolExecutor() as executor:
        results = list(filter(None, executor.map(process_file, file_paths)))

    return results

# GUI Application
def create_app():
    def select_folder():
        folder = filedialog.askdirectory()
        folder_entry.delete(0, END)
        folder_entry.insert(0, folder)

    def run_search():
        folder = folder_entry.get()
        search_term = search_term_entry.get()

        if not os.path.isdir(folder):
            output_text.insert(END, "Invalid directory! Please select a valid folder.\n")
            return
        if not search_term:
            output_text.insert(END, "Please enter a search term.\n")
            return

        output_text.delete(1.0, END)  # Clear previous output
        output_text.insert(END, "Searching... Please wait.\n")

        def background_search():
            results = search_for_term(folder, search_term)

            output_text.delete(1.0, END)  # Clear again to update results
            if not results:
                output_text.insert(END, f"No occurrences of '{search_term}' found.\n")
            else:
                output_text.insert(END, f"Files containing '{search_term}':\n")
                for file_path in results:
                    output_text.insert(END, f"- {file_path}\n")

        # Run in a separate thread to prevent UI freezing
        threading.Thread(target=background_search, daemon=True).start()

    # Create main window
    root = Tk()
    root.title("Search for a Term in JSON, XAML, and Excel")
    root.geometry("800x600")

    # Folder Selection
    Label(root, text="Select Folder:").pack()
    folder_entry = Entry(root, width=80)
    folder_entry.pack(pady=5)
    browse_button = Button(root, text="Browse", command=select_folder)
    browse_button.pack(pady=5)

    # Search Term Input
    Label(root, text="Enter Search Term:").pack()
    search_term_entry = Entry(root, width=80)
    search_term_entry.pack(pady=5)

    # Run Button
    run_button = Button(root, text="Search", command=run_search)
    run_button.pack(pady=10)

    # Output Text Box with Scrollbar
    scrollbar = Scrollbar(root)
    scrollbar.pack(side="right", fill="y")

    output_text = Text(root, wrap="word", yscrollcommand=scrollbar.set, height=30)
    output_text.pack(pady=10, padx=10, fill="both", expand=True)
    scrollbar.config(command=output_text.yview)

    root.mainloop()

if __name__ == "__main__":
    create_app()