from tkinter import *
from tkinter import font as tkFont
import time


# MONTANDO A GUI
def GUI():
    
    janela = Tk() # instância de uma janela
    janela.title('M O N S T R A T U R A')
    janela.resizable(False, False)
    # calculando a posição
    w = 350 
    h = 450 
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y)) # setando a posição no meio
    janela.configure(bg="white")
    
    
    # Função Iniciar: oculta os widgets da tela e inicia o jogo
    def Iniciar(x,y,z):
        x.pack_forget()
        y.pack_forget()
        z.pack_forget()

    
    def botoes():
        baner = Label(janela, text=' ',bg='white')
        baner.pack(padx=1,pady=20)

        # Fonte
        smallFonts16 = tkFont.Font(family='Small Fonts', size=16)
        
        # Botões
        iniciar = Button(janela, text="I n i c i a r", 
                                fg="black", 
                                bg="#FCFBD7", 
                                height=2, 
                                width=12,
                                font=smallFonts16)
        
        iniciar.pack(padx=1, pady=20)
        iniciar.configure(command=lambda:Iniciar(iniciar, continuar, opcoes))

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
