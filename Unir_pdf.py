<<<<<<< HEAD
import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
import threading

def hide_console():
    import ctypes
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd != 0:
        ctypes.windll.user32.ShowWindow(hwnd, 0)  # Ocultar la consola

def abrir_directorio(archivo):
    directorio = os.path.dirname(archivo)
    if os.path.exists(directorio):
        os.startfile(directorio)
    else:
        messagebox.showerror("Error", "No se pudo abrir el directorio.")

def merge_pdfs(input_pdfs, output_pdf, progress_window):
    merger = PyPDF2.PdfMerger()
    try:
        for pdf in input_pdfs:
            merger.append(pdf)
        
        with open(output_pdf, 'wb') as merged_pdf:
            merger.write(merged_pdf)
        
        messagebox.showinfo("Listo", f'PDFs unidos. Fueron guardados en: {output_pdf}')
    
    except Exception as e:
        messagebox.showerror("Error", f'Al unir PDFs: {e}')
    finally:
        progress_window.destroy()  # Cerrar la ventana de progreso

def merge_selected_pdfs():
    input_pdfs = text_area.get(1.0, tk.END).strip().split("\n")
    input_pdfs = [pdf for pdf in input_pdfs if pdf]  
    if input_pdfs:
        # Ask the user for the output file path
        output_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", 
                                                    filetypes=[("PDF Files", "*.pdf")],
                                                    title="Guardar PDF unidos")
        if output_pdf:  # Check if the user didn't cancel the dialog
            # Crear una ventana de progreso
            progress_window = tk.Toplevel(root)
            progress_window.title("Fusión en curso")
            progress_window.geometry("300x100")
            progress_label = tk.Label(progress_window, text="Fusionando PDFs, por favor espere...", font=("Arial", 12))
            progress_label.pack(pady=20)

            # Ejecutar la fusión en un hilo separado
            threading.Thread(target=merge_pdfs, args=(input_pdfs, output_pdf, progress_window)).start()
            abrir_directorio(output_pdf)
    else:
        messagebox.showwarning("Cuidado", "PDF no seleccionado.")
def select_files():
    # Open a dialog to select PDF files
    files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    if files:
        # Clear the text area and add the selected files
        current_files = set(text_area.get(1.0, tk.END).strip().split("\n"))  # Get current files in the text area
        for file in files:
            file_name = os.path.basename(file)
            if file not in current_files:  
                text_area.insert(tk.END, file + "\n")  
                text_area_vista.insert(tk.END, file_name + "\n")  
                current_files.add(file) 
                
            else:
                messagebox.showinfo("Archivo ya ingresado", f"El archivo '{file_name}' ya está en la lista.")
                
def clear_files():
    # Clear the text areas
    text_area.delete(1.0, tk.END)
    text_area_vista.delete(1.0, tk.END)
    messagebox.showinfo("Aviso", "Lista limpia")

# Create the main window
hide_console()
root = tk.Tk()
root.title("UNIR PDFS")
root.geometry("500x470")
root.configure(bg="#054B84")  # Custom background color

# Title
title_label = tk.Label(root, text="Lista de Archivos a unir", font=("Arial", 16), bg="#054B84", fg="white")
title_label.pack(pady=10)

# Text area to display selected files
text_area = scrolledtext.ScrolledText(root, width=45, height=15, bg="#FFFFFF", fg="#000000", font=("Arial", 12))
text_area.pack()
text_area.place(x=40, y=120)

text_area_vista = scrolledtext.ScrolledText(root, width=45, height=15, bg="#FFFFFF", fg="#000000", font=("Arial", 12))
text_area_vista.pack()
text_area_vista.place(x=40, y=120)

# Button to select files
select_button = tk.Button(root, text="SELECCIONAR", command=select_files, bg="#B10F43", fg="white", font=("Arial", 12), activebackground="#8A0C34")
select_button.pack(pady=10)

# Button to merge files
merge_button = tk.Button(root, text="    UNIR    ", command=merge_selected_pdfs, bg="#B10F43", fg="white", font=("Arial", 12), activebackground="#8A0C34")
merge_button.pack()
merge_button.place(x=140, y=410)

# Button to clear files
clear_button = tk.Button(root, text="  LIMPIAR  ", command=clear_files, bg="#B10F43", fg="white", font=("Arial", 12), activebackground="#8A0C34")
clear_button.pack()
clear_button.place(x=260, y=410)

# Run the application

=======
import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
import threading

def hide_console():
    import ctypes
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd != 0:
        ctypes.windll.user32.ShowWindow(hwnd, 0)  # Ocultar la consola

def abrir_directorio(archivo):
    directorio = os.path.dirname(archivo)
    if os.path.exists(directorio):
        os.startfile(directorio)
    else:
        messagebox.showerror("Error", "No se pudo abrir el directorio.")

def merge_pdfs(input_pdfs, output_pdf, progress_window):
    merger = PyPDF2.PdfMerger()
    try:
        for pdf in input_pdfs:
            merger.append(pdf)
        
        with open(output_pdf, 'wb') as merged_pdf:
            merger.write(merged_pdf)
        
        messagebox.showinfo("Listo", f'PDFs unidos. Fueron guardados en: {output_pdf}')
    
    except Exception as e:
        messagebox.showerror("Error", f'Al unir PDFs: {e}')
    finally:
        progress_window.destroy()  # Cerrar la ventana de progreso

def merge_selected_pdfs():
    input_pdfs = text_area.get(1.0, tk.END).strip().split("\n")
    input_pdfs = [pdf for pdf in input_pdfs if pdf]  
    if input_pdfs:
        # Ask the user for the output file path
        output_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", 
                                                    filetypes=[("PDF Files", "*.pdf")],
                                                    title="Guardar PDF unidos")
        if output_pdf:  # Check if the user didn't cancel the dialog
            # Crear una ventana de progreso
            progress_window = tk.Toplevel(root)
            progress_window.title("Fusión en curso")
            progress_window.geometry("300x100")
            progress_label = tk.Label(progress_window, text="Fusionando PDFs, por favor espere...", font=("Arial", 12))
            progress_label.pack(pady=20)

            # Ejecutar la fusión en un hilo separado
            threading.Thread(target=merge_pdfs, args=(input_pdfs, output_pdf, progress_window)).start()
            abrir_directorio(output_pdf)
    else:
        messagebox.showwarning("Cuidado", "PDF no seleccionado.")
def select_files():
    # Open a dialog to select PDF files
    files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    if files:
        # Clear the text area and add the selected files
        current_files = set(text_area.get(1.0, tk.END).strip().split("\n"))  # Get current files in the text area
        for file in files:
            file_name = os.path.basename(file)
            if file not in current_files:  
                text_area.insert(tk.END, file + "\n")  
                text_area_vista.insert(tk.END, file_name + "\n")  
                current_files.add(file) 
                
            else:
                messagebox.showinfo("Archivo ya ingresado", f"El archivo '{file_name}' ya está en la lista.")
                
def clear_files():
    # Clear the text areas
    text_area.delete(1.0, tk.END)
    text_area_vista.delete(1.0, tk.END)
    messagebox.showinfo("Aviso", "Lista limpia")

# Create the main window
hide_console()
root = tk.Tk()
root.title("UNIR PDFS")
root.geometry("500x470")
root.configure(bg="#054B84")  # Custom background color

# Title
title_label = tk.Label(root, text="Lista de Archivos a unir", font=("Arial", 16), bg="#054B84", fg="white")
title_label.pack(pady=10)

# Text area to display selected files
text_area = scrolledtext.ScrolledText(root, width=45, height=15, bg="#FFFFFF", fg="#000000", font=("Arial", 12))
text_area.pack()
text_area.place(x=40, y=120)

text_area_vista = scrolledtext.ScrolledText(root, width=45, height=15, bg="#FFFFFF", fg="#000000", font=("Arial", 12))
text_area_vista.pack()
text_area_vista.place(x=40, y=120)

# Button to select files
select_button = tk.Button(root, text="SELECCIONAR", command=select_files, bg="#B10F43", fg="white", font=("Arial", 12), activebackground="#8A0C34")
select_button.pack(pady=10)

# Button to merge files
merge_button = tk.Button(root, text="    UNIR    ", command=merge_selected_pdfs, bg="#B10F43", fg="white", font=("Arial", 12), activebackground="#8A0C34")
merge_button.pack()
merge_button.place(x=140, y=410)

# Button to clear files
clear_button = tk.Button(root, text="  LIMPIAR  ", command=clear_files, bg="#B10F43", fg="white", font=("Arial", 12), activebackground="#8A0C34")
clear_button.pack()
clear_button.place(x=260, y=410)

# Run the application

>>>>>>> 05fc4567549b073cb3cab20982952a0b764e27bc
root.mainloop()