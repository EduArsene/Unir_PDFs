import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox
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
    input_pdfs = listbox_files.get(0, tk.END)
    input_pdfs = [pdf for pdf in input_pdfs if pdf]  # Filtrar las entradas vacías
    if input_pdfs:
        output_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", 
                                                    filetypes=[("PDF Files", "*.pdf")],
                                                    title="Guardar PDF unidos")
        if output_pdf:  
            progress_window = tk.Toplevel(root)
            progress_window.title("Fusión en curso")
            progress_window.geometry("300x100")
            progress_label = tk.Label(progress_window, text="Fusionando PDFs, por favor espere...", font=("Arial", 12))
            progress_label.pack(pady=20)

            threading.Thread(target=merge_pdfs, args=(input_pdfs, output_pdf, progress_window)).start()
            abrir_directorio(output_pdf)
    else:
        messagebox.showwarning("Cuidado", "PDF no seleccionado.")

def select_files():
    files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    if files:
        current_files = set(listbox_files.get(0, tk.END))  
        for file in files:
            file_name = os.path.basename(file)
            if file not in current_files:  
                listbox_files.insert(tk.END, file)  
                current_files.add(file) 
            else:
                messagebox.showinfo("Archivo ya ingresado", f"El archivo '{file_name}' ya está en la lista.")
                
def clear_files():
    # Clear the listbox
    listbox_files.delete(0, tk.END)
    messagebox.showinfo("Aviso", "Lista limpia")

hide_console()

root = tk.Tk()
root.title("UNIR PDFS")
root.geometry("760x470")
root.configure(bg="#2C3E50") 

# Título principal
title_label = tk.Label(root, text="Lista de pdf's a unir", font=("Arial", 16), bg="#2C3E50", 
                       fg="white", highlightbackground="#00EFEF", highlightthickness=2)
title_label.pack(pady=15)

# Listbox para mostrar los archivos PDF seleccionados
listbox_files = tk.Listbox(root, width=70, height=15, bg="#34495E", fg="#ECF0F1", font=("Arial", 12), 
                           selectbackground="#1ABC9C", selectmode=tk.MULTIPLE, activestyle="none")
listbox_files.pack(pady=10)
listbox_files.place(x=40, y=120)

# Boton para seleccionar archivos
boton_seleccionar = tk.Button(root, text="SELECCIONAR", command=select_files, bg="#1ABC9C", fg="white", 
                              font=("Arial", 12, "bold"), activeforeground="white", activebackground="#00EFEF", 
                              highlightbackground="red", highlightthickness=2)
boton_seleccionar.pack(pady=10)

# Botón para unir los PDFs seleccionados
boton_unir = tk.Button(root, text="    UNIR    ", command=merge_selected_pdfs, bg="#1ABC9C", fg="white", 
                       font=("Arial", 12, "bold"), activeforeground="white", activebackground="#00EFEF", 
                       highlightbackground="red", highlightthickness=2)
boton_unir.pack()
boton_unir.place(x=220, y=410)

# Botón para limpiar la lista de archivos
boton_borrar = tk.Button(root, text="  LIMPIAR  ", command=clear_files, bg="#1ABC9C", fg="white", 
                         font=("Arial", 12, "bold"), activeforeground="white", activebackground="#00EFEF", 
                         highlightbackground="skyblue", highlightthickness=2)
boton_borrar.pack()
boton_borrar.place(x=420, y=410)

root.mainloop()
