import customtkinter as ct

def initial(root):
    print('')

def main():
    root = ct.CTk()
    root.geometry("650x700")
    root.title("Waifu2z - Image Quality Improver")
    root.after(1, lambda :root.iconbitmap(''))

    initial(root)
    
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

main()