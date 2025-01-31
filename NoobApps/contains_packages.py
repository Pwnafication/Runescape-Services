import os
import json
import pandas as pd
import openpyxl
import warnings
import threading
from tkinter import Tk, filedialog, Text, Button, Scrollbar, END, Entry, Label, Checkbutton, BooleanVar
from concurrent.futures import ThreadPoolExecutor

# Suppress warnings from openpyxlpi
warnings.simplefilter("ignore")

# Function to search for a term within JSON, XAML, and Excel files
def search_for_term(folder, search_term, search_xaml, search_excel):
    project_results = set()  # Store unique project names
    file_paths = []  # Collect relevant files for processing

    for root, _, files in os.walk(folder):
        project_name = None
        project_json_path = os.path.join(root, "project.json")

        # Always search project.json
        if os.path.exists(project_json_path):
            try:
                with open(project_json_path, "r", encoding="utf-8") as f:
                    project_data = json.load(f)
                    project_name = project_data.get("name", "Unknown Project")
            except (json.JSONDecodeError, FileNotFoundError) as e:
                print(f"Error processing {project_json_path}: {e}")

        # Collect XAML/Excel files only if a project name exists
        for file in files:
            file_path = os.path.join(root, file)

            if project_name and (
                (search_xaml and file.endswith(".xaml")) or
                (search_excel and file.endswith((".xls", ".xlsx")))
            ):
                file_paths.append((file_path, project_name))

    def process_file(file_path, project_name):
        try:
            # Search in XAML files
            if search_xaml and file_path.endswith(".xaml"):
                with open(file_path, "r", encoding="utf-8") as f:
                    if search_term in f.read():
                        project_results.add(project_name)
                        return

            # Search in Excel files (.xls, .xlsx)
            if search_excel and file_path.endswith((".xls", ".xlsx")):
                engine = "openpyxl" if file_path.endswith(".xlsx") else "xlrd"
                try:
                    df = pd.read_excel(file_path, engine=engine, dtype=str)
                    if df.applymap(lambda x: search_term in str(x) if pd.notna(x) else False).any().any():
                        project_results.add(project_name)
                        return
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

        except (json.JSONDecodeError, FileNotFoundError, pd.errors.ParserError) as e:
            print(f"Error processing {file_path}: {e}")

    # Use ThreadPoolExecutor for parallel execution
    with ThreadPoolExecutor() as executor:
        executor.map(lambda fp: process_file(*fp), file_paths)

    return sorted(project_results)  # Return sorted unique project names

# GUI Application
def create_app():
    def select_folder():
        folder = filedialog.askdirectory()
        folder_entry.delete(0, END)
        folder_entry.insert(0, folder)

    def run_search():
        folder = folder_entry.get()
        search_term = search_term_entry.get()
        search_xaml = xaml_var.get()
        search_excel = excel_var.get()

        if not os.path.isdir(folder):
            output_text.insert(END, "Invalid directory! Please select a valid folder.\n")
            return
        if not search_term:
            output_text.insert(END, "Please enter a search term.\n")
            return
        if not (search_xaml or search_excel):  # JSON is always checked
            output_text.insert(END, "Please select at least one file type (XAML or Excel).\n")
            return

        output_text.delete(1.0, END)  # Clear previous output
        output_text.insert(END, "Searching... Please wait.\n")

        def background_search():
            results = search_for_term(folder, search_term, search_xaml, search_excel)

            output_text.delete(1.0, END)  # Clear again to update results
            if not results:
                output_text.insert(END, f"No projects found containing '{search_term}'.\n")
            else:
                output_text.insert(END, f"Projects containing '{search_term}':\n")
                for project_name in results:
                    output_text.insert(END, f"- {project_name}\n")

        # Run search in a separate thread to prevent UI freezing
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

    # File Type Selection (Checkbuttons for XAML & Excel only)
    Label(root, text="Select File Types to Search (JSON is always included):").pack()
    xaml_var = BooleanVar(value=True)
    excel_var = BooleanVar(value=True)

    xaml_check = Checkbutton(root, text="Search XAML (.xaml)", variable=xaml_var)
    xaml_check.pack()
    excel_check = Checkbutton(root, text="Search Excel (.xls, .xlsx)", variable=excel_var)
    excel_check.pack()

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