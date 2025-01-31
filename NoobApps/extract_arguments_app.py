import os
from tkinter import Tk, filedialog, Text, Button, Scrollbar, END, Entry
from xml.etree import ElementTree as ET

# Function to extract namespaces dynamically
def get_namespaces(file_path):
    try:
        events = ET.iterparse(file_path, events=("start-ns",))
        namespaces = {prefix: uri for event, (prefix, uri) in events}
    except ET.ParseError as e:
        print(f"Error parsing namespaces in file {file_path}: {e}")
        namespaces = {}
    return namespaces

# Function to process a single XAML file and extract arguments
def extract_arguments_from_xaml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except (FileNotFoundError, ET.ParseError) as e:
        return None, None

    # Extract namespaces dynamically from the file
    namespaces = get_namespaces(file_path)

    # Find all <x:Property> elements dynamically using namespaces
    arguments = root.findall('.//x:Property', namespaces)

    in_arguments = []
    out_arguments = []

    # Process each argument
    for argument in arguments:
        direction = argument.attrib.get('Direction', 'In')  # Default to 'In' if no Direction is specified
        name = argument.attrib.get('Name', 'UnknownName')
        if direction.lower() == 'in':
            in_arguments.append(name)
        elif direction.lower() == 'out':
            out_arguments.append(name)

    # Move arguments starting with 'out_' from in_arguments to out_arguments
    remaining_in_arguments = []
    for arg in in_arguments:
        if arg.startswith('out_'):
            out_arguments.append(arg)
        else:
            remaining_in_arguments.append(arg)

    # Replace the original in_arguments list with the filtered one
    in_arguments = remaining_in_arguments

    return in_arguments, out_arguments

# Function to process a directory of XAML files recursively
def process_directory(directory):
    results = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.xaml'):
                file_path = os.path.join(root, file)
                in_args, out_args = extract_arguments_from_xaml(file_path)
                if in_args is not None and out_args is not None:
                    results.append((file, in_args, out_args))
    return results

# GUI Application
def create_app():
    def select_folder():
        folder = filedialog.askdirectory()
        folder_entry.delete(0, END)
        folder_entry.insert(0, folder)

    def run_extraction():
        folder = folder_entry.get()
        if not os.path.isdir(folder):
            output_text.insert(END, "Invalid directory! Please select a valid folder.\n")
            return
        
        output_text.delete(1.0, END)  # Clear previous output
        results = process_directory(folder)
        
        if not results:
            output_text.insert(END, "No XAML files found in the selected folder.\n")
        else:
            for file_name, in_args, out_args in results:
                output_text.insert(END, f"{file_name}\n")
                output_text.insert(END, f"In Arguments: {in_args}\n")
                output_text.insert(END, f"Out Arguments: {out_args}\n\n")

    # Create main window
    root = Tk()
    root.title("XAML Argument Extractor")
    root.geometry("800x600")

    # Folder Selection
    folder_label = Text(root, height=1, width=20)
    folder_label.insert(END, "Select Folder:")
    folder_label.configure(state="disabled")
    folder_label.pack()

    folder_entry = Entry(root, width=80)
    folder_entry.pack(pady=5)

    browse_button = Button(root, text="Browse", command=select_folder)
    browse_button.pack(pady=5)

    # Run Button
    run_button = Button(root, text="Run Extraction", command=run_extraction)
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