import tkinter as tk

finestra = tk.Tk()

finestra.title("Formulari")
finestra.configure(bg="#add4fd")

acceptat = tk.BooleanVar(value=False)

def Submit():
    if not acceptat.get():
        requerit.grid()
        requerit.configure(text="*Has d'acceptar termes i condicions")
    if acceptat.get():
        requerit.grid_remove()
        missatgePantalla.set(f"Benvingut, {nom.get()} {cognom.get()}")

marcPantalla = tk.Frame(finestra, bd=2, relief="solid",bg="#7dbbfc")
marcPantalla.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
missatgePantalla = tk.StringVar()
info = tk.Label(marcPantalla, text="Informació:", bg="#7dbbfc")
info.grid(row=0, column=0, columnspan=2, sticky="nsew")
pantalla = tk.Entry(marcPantalla, textvariable=missatgePantalla, state="readonly")
pantalla.grid(row=1, column=0, columnspan=2, sticky="nsew")

marcInfoPersonal = tk.Frame(finestra, bd=2, relief="solid",bg="#7dbbfc")
marcInfoPersonal.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
etiquetaNom = tk.Label(marcInfoPersonal, text="Nom: ", bg="#7dbbfc")
etiquetaNom.grid(row=0, column=0)
nom = tk.Entry(marcInfoPersonal)
nom.grid(row=0, column=1, sticky="nsew")

etiquetaCognom = tk.Label(marcInfoPersonal, text="Cognom: ", bg="#7dbbfc")
etiquetaCognom.grid(row=1, column=0)
cognom = tk.Entry(marcInfoPersonal)
cognom.grid(row=1, column=1, sticky="nsew")

marcOpcions = tk.Frame(finestra, bd=2, relief="solid")
marcOpcions.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
requerit = tk.Label(marcOpcions, text="", fg="red", bg="#7dbbfc")
requerit.grid(row=0, column=0,columnspan=2, sticky="nsew")
requerit.grid_remove()
termesICondicions = tk.Checkbutton(marcOpcions, text="Accepte els termes i condicions", variable=acceptat, bg="#7dbbfc")
termesICondicions.grid(row=1, column=0,columnspan=2, sticky="nsew")

marcBotons = tk.Frame(finestra, bd=2, relief="solid",bg="#7dbbfc")
marcBotons.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
boto = tk.Button(marcBotons, text="Enviar", bg="#0b7ef7", command=Submit)
boto.grid(row=0, column=0, sticky="nsew")
finestra.mainloop()