import customtkinter as ct

def initial(root):
    l1 = ct.CTkLabel(root, text="Waifu2z - Image Quality Improver")
    l1.pack(pady=20)

def main():
    root = ct.CTk()
    root.geometry("650x400")
    root.title("Waifu2z - Image Quality Improver")
    root.after(1, lambda :root.iconbitmap(''))

    initial(root)
    
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

main()