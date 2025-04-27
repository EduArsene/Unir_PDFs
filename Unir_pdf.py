
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

hide_console()
root = tk.Tk()
root.title("UNIR PDFS")
root.geometry("500x470")
root.configure(bg="black") 

title_label = tk.Label(root, text="Lista de Archivos a unir", font=("Arial", 16), bg="black", 
                       fg="white",highlightbackground="#00EFEF", highlightthickness=2)
title_label.pack(pady=10)

text_area = scrolledtext.ScrolledText(root, width=45, height=15, bg="#FFFFFF", fg="#000000", font=("Arial", 12))
text_area.pack()
text_area.place(x=40, y=120)

text_area_vista = scrolledtext.ScrolledText(root, width=45, height=15, bg="#FFFFFF", fg="#000000", font=("Arial", 12)
                                            )
text_area_vista.pack()
text_area_vista.place(x=40, y=120)

select_button = tk.Button(root, text="SELECCIONAR", command=select_files, bg="black", fg="white", font=("Arial", 12,"bold"), activeforeground="white",activebackground="#00EFEF"
                          ,highlightbackground="red", highlightthickness=2)
select_button.pack(pady=10)

merge_button = tk.Button(root, text="    UNIR    ", command=merge_selected_pdfs, bg="black", fg="white", font=("Arial", 12,"bold"),activeforeground="white", activebackground="#00EFEF"
                         ,highlightbackground="red", highlightthickness=2)
merge_button.pack()
merge_button.place(x=140, y=410)

clear_button = tk.Button(root, text="  LIMPIAR  ", command=clear_files, bg="black", fg="white", font=("Arial", 12,"bold"),activeforeground="white", activebackground="#00EFEF" 
                         ,highlightbackground="skyblue", highlightthickness=2)
clear_button.pack()

clear_button.place(x=260, y=410)
root.mainloop()
root.mainloop()