import tkinter as tk

def on_click(button_value):
    current_text = entry.get()
    
    if button_value == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_value == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_value)

# Erstelle das Hauptfenster
root = tk.Tk()
root.title("VSCode-Rechner")
root.geometry("400x600")  # Ändere die Größe des Fensters

# Eingabefeld
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=5, insertwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

# Schaltflächen
buttons = [
    ('7', '#333333'), ('8', '#333333'), ('9', '#333333'), ('/', '#555555'),
    ('4', '#333333'), ('5', '#333333'), ('6', '#333333'), ('*', '#555555'),
    ('1', '#333333'), ('2', '#333333'), ('3', '#333333'), ('-', '#555555'),
    ('0', '#333333'), ('.', '#333333'), ('=', '#FFA500'), ('+', '#555555'),
    ('C', '#888888')
]

row_val = 1
col_val = 0

for button, color in buttons:
    tk.Button(root, text=button, width=8, height=4, font=('Arial', 14),
              command=lambda button=button: on_click(button), bd=0, bg=color, fg='#FFFFFF').grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Stilanpassungen für ein professionelles Aussehen
root.configure(bg='#1E1E1E')  # Hintergrundfarbe
entry.configure(bg='#333333', fg='#FFFFFF', relief=tk.FLAT)  # Eingabefeldfarbe, Textfarbe und Randstil
for button in root.winfo_children():
    if isinstance(button, tk.Button):
        button.configure(relief=tk.FLAT)  # Randstil für Schaltflächen

# Starte die Tkinter-Schleife
root.mainloop()
