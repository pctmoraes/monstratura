from tkinter import *
from tkinter import font as tkFont
import time
import sys


# MONTANDO A GUI
def GUI():
    
    janela = Tk() # instância de uma janela
    janela.title('M O N S T R A T U R A')
    #janela.resizable(False, False)
    # calculando a posição
    w = 350 
    h = 450 
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y)) # setando a posição no meio
    janela.configure(bg="white")
    
    # Fonte
    smallFonts16 = tkFont.Font(family='Small Fonts', size=16)
    fixedSys18 = tkFont.Font(family='Fixedsys', size=18)
    
    # Função Iniciar: oculta os widgets da tela e inicia o jogo
    def Iniciar(x,y,z,b,jan):
        x.pack_forget()
        y.pack_forget()
        z.pack_forget()
        b.pack_forget()
        prologo(jan)

    def prologo(jan):
        baner = Label(jan, text='\nOlá', bg="white", fg="black", font=fixedSys18)
        baner.pack(padx=1, pady=60)

        ir = Button(jan, text=" ! ", 
                                fg="black", 
                                bg="#FCFBD7", 
                                height=1, 
                                width=2,
                                font=fixedSys18)
        ir.pack(padx=1, pady=1)
        cont = 0
        def skip(cont, ir, ban):
            cont += 1
            if cont == 1:
                msg = "\nVocê está prestes\n a iniciar em uma \nnova aventura!"
                ban.configure(text=msg)
            elif cont == 2:
                msg = "\nMas antes \nvejamos alguns \ncomandos básicos."
                ban.configure(text=msg)
            elif cont == 3:
                ban.configure(text=" ")
                ban.pack(padx=1, pady=1)
                jogar = Button(janela, text="j",
                                        fg="black",
                                        bg="#FCFBD7",
                                        font=fixedSys18)
                jogar.pack(padx=1, pady=10)
                # jogar.grid(row=1, column=1)
                
                mochila = Button(janela, text="m",
                                        fg="black",
                                        bg="#FCFBD7",
                                        font=fixedSys18)
                mochila.pack(padx=1, pady=10)

                opcoes = Button(janela, text="o",
                                        fg="black",
                                        bg="#FCFBD7",
                                        font=fixedSys18)
                opcoes.pack(padx=1, pady=10)

                atributos = Button(janela, text="a",
                        fg="black",
                        bg="#FCFBD7",
                        font=fixedSys18)
                atributos.pack(padx=1, pady=10)
                
                salvar = Button(janela, text="s",
                                        fg="black",
                                        bg="#FCFBD7",
                                        font=fixedSys18)
                salvar.pack(padx=1, pady=10)

                sair = Button(janela, text="e",
                                        fg="black",
                                        bg="#FCFBD7",
                                        font=fixedSys18)
                sair.pack(padx=1, pady=10)

                ir.pack(side=BOTTOM)
            ir.configure(command=lambda:skip(cont, ir,baner))
        ir.configure(command=lambda:skip(cont, ir,baner))      


    def botoes():
        baner = Label(janela, text=" ",bg="white")
        baner.pack(padx=1,pady=20)

        # Botões
        iniciar = Button(janela, text="I n i c i a r", 
                                fg="black", 
                                bg="#FCFBD7", 
                                height=2, 
                                width=12,
                                font=smallFonts16)
        
        iniciar.pack(padx=1, pady=20)
        iniciar.configure(command=lambda:Iniciar(iniciar, continuar, opcoes, baner, janela))

        continuar = Button(janela, text="C o n t i n u a r", 
                            fg="black", 
                            bg="#FCFBD7", 
                            height=2, 
                            width=12,
                            font=smallFonts16)
        
        continuar.pack(padx=1, pady=20)

        opcoes = Button(janela, text="O p ç õ e s", 
                        fg="black", 
                        bg="#FCFBD7", 
                        height=2, 
                        width=12,
                        font=smallFonts16)
        
        opcoes.pack(padx=1, pady=20)
    
    botoes()
    janela.mainloop()

GUI()
