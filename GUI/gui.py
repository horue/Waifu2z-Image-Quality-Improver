import customtkinter as ct

def initial(root):
    l1 = ct.CTkLabel(root, text="Waifu2z - Image Quality Improver")
    l1.pack(pady=20)


    check_var = ct.StringVar(value='off')
    c1 = ct.CTkCheckBox(root, text='Color improvement', checkbox_width=15, checkbox_height=15, corner_radius=0, border_width=2, variable=check_var, onvalue='on', offvalue='off')
    c1.pack(pady=10)


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