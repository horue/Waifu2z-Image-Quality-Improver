import customtkinter as ct
from improver import upscaling
from customtkinter import filedialog   


def select(l2):
    global path
    path = filedialog.askopenfile().name
    l2.configure(text=f'Selected file: {path}')


def initial(root):
    l1 = ct.CTkLabel(root, text="Waifu2z - Image Quality Improver")
    l1.pack(pady=20)

    check_var = ct.StringVar(value='off')
    c1 = ct.CTkCheckBox(root, text='Color improvement', checkbox_width=15, checkbox_height=15, corner_radius=0, border_width=2, variable=check_var, onvalue='on', offvalue='off')
    c1.pack(pady=10)

    check_var2 = ct.StringVar(value=False)
    c2 = ct.CTkCheckBox(root, text='Quadrant Upscaling', checkbox_width=15, checkbox_height=15, corner_radius=0, border_width=2, variable=check_var2, onvalue=True, offvalue=False)
    c2.pack()

    l2 = ct.CTkLabel(root, text='Upscaling factor: ')
    l2.pack()

    e1 = ct.CTkEntry(root, width=30)
    e1.pack(pady=10)

    l2 = ct.CTkLabel(root, text='Selected Image: None')
    l2.pack()

    b1 = ct.CTkButton(root, text='Select image', command=lambda:select(l2))
    b1.pack(pady=10)

    b2 = ct.CTkButton(root, text='Upscale', command=lambda:upscaling(imagePath=path, upscale=float(e1.get()), q=check_var2.get()))
    b2.pack()

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