import numpy as np
#se agarega las librerias para poder agregar la interfaz grafica
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#pip install numpy
#pip install matplotlib
    
# Nombres de archivos para guardar las tareas
ventana = tk.Tk()
root=tk.Tk()
ventana.title("Proyecto")
ventana.geometry('300x350')
ventana25 = tk.Tk()
ventana25.title("Menu")
ventana25.config(bg="limegreen")
ventana25.geometry('320x250')
ventana.config(bg="navy")
Entrada_txt25=Entry(ventana25,width=3)
matrizinversa=tk.Tk()
rangomatrices=tk.Tk()
valores=tk.Tk()
valores.geometry("300x300")
valores.config(bg="limegreen")
Entrada_txt=Entry(ventana,width=3)
filasr=Entry(rangomatrices,width=3)
columnasr=Entry(rangomatrices,width=3)
filasr2=0
columnasr2=0
opcion=""
opcion2=""
p=0
m=0
ventana_multiplicar = tk.Tk()
ventana_multiplicar.title("Multiplicación de Matrices")
ventana_multiplicar.geometry('600x400')
#----GAUSS JORDAN---
metodogaussjordan=tk.Tk()
definirvaloresmatriz=tk.Tk()
valores1=tk.Tk()
valores1.config(bg="limegreen")
incognitas=Entry(metodogaussjordan,width=3)
valores2=Entry(valores1,width=3)
l=Label(valores1,bg="limegreen", text="")
ventana2 = tk.Tk()
entry_b1 = Entry(ventana2)
entry_c1 = Entry(ventana2)
entry_a1 = Entry(ventana2)
ventana2.title("Graficas de Ecuacuaciones")
entry_a2 = Entry(ventana2)
entry_b2 = Entry(ventana2)
entry_c2 = Entry(ventana2)

def operacion(a, n):
    i = 0
    j = 0
    k = 0
    c = 0
    flag = 0
    m = 0
    pro = 0
 
    for i in range(n):
        if (a[i][i] == 0):
 
            c = 1
            while ((i + c) < n and a[i + c][i] == 0):
                c += 1
            if ((i + c) == n):
 
                flag = 1
                break
 
            j = i
            for k in range(1 + n):
 
                temp = a[j][k]
                a[j][k] = a[j+c][k]
                a[j+c][k] = temp
 
        for j in range(n):
 
            # Excluding all i == j
            if (i != j):
                p = a[j][i] / a[i][i]
 
                k = 0
                for k in range(n + 1):
                    a[j][k] = a[j][k] - (a[i][k]) * p
 
    return flag

def Chequearconsistencia(a, n, flag):
 
    # flag == 2 for infinite solution
    # flag == 3 for No solution
    flag = 3
    for i in range(n):
        sum = 0
        for j in range(n):
            sum = sum + a[i][j]
        if (sum == a[i][j]):
            flag = 2
 
    return flag



def rangomatriz():
    global opcion
    opcion=Entrada_txt.get()
    if(opcion=="1"):
        ventana.withdraw()
        rangomatrices.deiconify()
        rangomatrices.title("Rango de raices")
        l=Label(rangomatrices,bg="deepskyblue", text="Ingrese rango de raices",font=("Arial", 18,"bold"))
        l.grid(row=0, column=0, columnspan=3)
        q=Label(rangomatrices,bg="deepskyblue", text="Ingrese Filas",font=("Arial", 12,"bold"))
        q.grid(row=1, column=0)
        q.config(fg="black")
        filasr.grid(row=2,column=0)
        z=Label(rangomatrices,bg="deepskyblue", text="Ingrese Columnas",font=("Arial", 12,"bold"))
        z.grid(row=1, column=2)
        z.config(fg="black")
        columnasr.grid(row=2,column=2)
        nn=Label(rangomatrices,text="",bg="deepskyblue",font=("Arial", 9,"bold"))
        nn.grid(row=2, column=1)
        w=Label(rangomatrices,text="",bg="deepskyblue",font=("Arial", 9,"bold"))
        w.grid(row=3, column=0, columnspan=3)
        b1 = Button(rangomatrices, text="Confirmar",bg="red",fg="black",command=valoresmatrices)
        b1.grid(row=4, column=0, columnspan=3)
        v=Label(rangomatrices,text="",bg="deepskyblue",font=("Arial", 9,"bold"))
        v.grid(row=5, column=0, columnspan=3)
        rangomatrices.geometry("300x200")
        rangomatrices.config(bg="deepskyblue")
        rangomatrices.mainloop()

    if(opcion=="3"):
        matrizinversa.withdraw()
        rangomatrices.withdraw()
        ventana25.deiconify()
        metodogaussjordan.withdraw()
        definirvaloresmatriz.withdraw()
        valores1.withdraw()
        valores.withdraw()
        ventana.withdraw()
        Menu = Label(ventana25,text="Menu:", bg="limegreen", font=("Arial", 15,"bold"))
        agregar=Label(ventana25,text="1. Metodo Gauss-Jordan",bg="limegreen",font=("Arial", 15),anchor="e").place(x = 5, y = 30)
        pendientes=Label(ventana25,text="2. Regla de Cramer",bg="limegreen",font=("Arial", 15)).place(x = 5, y = 60)
        Entrada_txt25.place(x=150,y=180)
        b1 = Button(ventana25, text="Confirmar",command=menusecundario)
        b1.place(x=125,y=210)
        Menu.pack()

        
def menusecundario():
    opcion2=Entrada_txt25.get()
    if(opcion2=="1"):
        ventana.withdraw()#oculta la ventana principal
        metodogaussjordan.deiconify()#pantalla de rango matriz
        definirvaloresmatriz.withdraw()
        valores1.withdraw()
        ventana25.withdraw()
        metodogaussjordan.title("Incognitas")
        l=Label(metodogaussjordan,bg="limegreen",text="Ingrese cuantas incognitas tendra su ecuacion",font=("Arial", 18,"bold"))
        l.grid(row=0, column=0, columnspan=3)
        incognitas.grid(row=2,column=1)
        w=Label(metodogaussjordan,bg="limegreen", text="",font=("Arial", 12,"bold"))
        w.grid(row=2, column=3)
        b1 = Button(metodogaussjordan, text="Confirmar",command=valores3)
        b1.grid(row=4, column=0, columnspan=3)
        v=Label(metodogaussjordan,bg="limegreen",text="",font=("Arial", 12,"bold"))
        v.grid(row=5, column=0, columnspan=3)
        metodogaussjordan.geometry("600x100")
        metodogaussjordan.config(bg="limegreen")
        metodogaussjordan.mainloop()

    if(opcion2=="2"):
        ventana.withdraw()#oculta la ventana principal
        metodogaussjordan.deiconify()#pantalla de rango matriz
        definirvaloresmatriz.withdraw()
        valores1.withdraw()
        ventana25.withdraw()
        metodogaussjordan.title("Incognitas")
        l=Label(metodogaussjordan,text="Ingrese cuantas incognitas tendra su ecuacion", bg="limegreen",font=("Arial", 18,"bold"))
        l.grid(row=0, column=0, columnspan=3)
        incognitas.grid(row=2,column=1)
        w=Label(metodogaussjordan,text="",bg="limegreen", font=("Arial", 8,"bold"))
        w.grid(row=2, column=3)
        b1 = Button(metodogaussjordan, bg="green",text="Confirmar",command=valores4)
        b1.grid(row=4, column=0, columnspan=3)
        v=Label(metodogaussjordan, bg="limegreen", text="",font=("Arial", 8,"bold"))
        v.grid(row=5, column=0, columnspan=3)
        metodogaussjordan.geometry("400x300")
        metodogaussjordan.config(bg="limegreen")
        metodogaussjordan.mainloop()


def metodoinvertir():
    entrada1=filasr.get()
    entrada2=columnasr.get()
    xy=np.asarray(B, dtype=float)
    mi=np.linalg.inv(xy)
    for g in range(int(entrada1)):
        for c in range(int(entrada2)):
            cell = Entry(matrizinversa,width=5)
            cell.grid(row=p+g, column=m+c, padx=2, pady=2)
            cell.insert(0, '{}'.format(str(round(mi[g][c], 2))))
            cell.config(state= "disabled")
    matrizinversa.geometry("200x200")
    matrizinversa.config(bg="deepskyblue")
    matrizinversa.update()
    matrizinversa.update_idletasks()

e0=0
z0=0
e1=""
e2=""
B=[]


cell1= Entry(valores,width=5)

def valoresmatrices():
    global opcion
    global e1
    e1=filasr.get()
    global e2
    e2=columnasr.get()
    opcion=Entrada_txt.get()
    if(opcion=="1"):
        rangomatrices.withdraw()
        valores.deiconify()
        valores.title("Valores Matrices")
        for g in range(int(e1)):
            B.append([0]*int(e2))
        l=Label(valores,text="Ingrese valores de matriz de",font=("Arial", 10,"bold"))
        l.grid(row=0, column=0, columnspan=3)
        cell1.grid(row=1, column=1)
        b1 = Button(valores, text="Confirmar",command=llenardatos)
        b1.grid(row=4, column=0, columnspan=3)
    

def llenardatos():
    global e0
    global z0
    global e1
    global e2
    if( e0<int(e1)):
        if(z0<int(e2)):
            B[e0][z0]=cell1.get()
            cell1.delete(0, END)
            z0+=1
            print("ingresado")
        if(z0==int(e2)):
            e0+=1
            z0=0
        if(e0==int(e1)):
            MenuInvertir()

def MenuInvertir():    
    entrada1=filasr.get()
    entrada2=columnasr.get()
    global p
    global m
    if(entrada1=="") or (entrada2==""):
        messagebox.showinfo(message="LLENAR FILAS Y COLUMNAS", title="VACIO")
    else:
        valores.withdraw()
        matrizinversa.deiconify()
        matrizinversa.title("INVERSA DE UNA MATRIZ")
        l=Label(matrizinversa,text="INGRESE LOS DATOS DE LA MATRIZ",bg="deepskyblue",font=("Arial", 7,"bold"))
        l.grid(row=0, column=0, columnspan=int(entrada2)+1)
        fila=1
        columna=0
        f=0
        t=0
        for g in range(int(entrada1)):
            for c in range(int(entrada2)):
                cell = Entry(matrizinversa,width=5)
                cell.grid(row=fila+g, column=columna+c, padx=2, pady=2)
                cell.insert(0, '{}'.format(B[g][c]))
                cell.config(state= "disabled")
                t=columna+c
        f=fila+g
        b1 = Button(matrizinversa, text="Invertir",bg="red",fg="black", command=metodoinvertir)
        b1.grid(row=int((f/2)+1), column=t+1)
        o=Label(matrizinversa,text="Matriz Invertida",bg="navy",font=("Arial", 10,"bold"))
        o.grid(row=0, column=t+2, columnspan=int(entrada2)*2)
        fila=1
        columna=t+2
        p=fila
        m=columna
        for g in range(int(entrada1)):
            for c in range(int(entrada2)):
                cell = Entry(matrizinversa,width=5)
                cell.grid(row=fila+g, column=columna+c, padx=2, pady=2)
                cell.config(state= "disabled")
                t=columna+c
            f=fila+g
        matrizinversa.geometry("300x200")
        matrizinversa.config(bg="deepskyblue")
        matrizinversa.mainloop()


def Menu():
    matrizinversa.withdraw()
    ventana2.withdraw()
    rangomatrices.withdraw()
    ventana_multiplicar.withdraw()
    root.withdraw()
    metodogaussjordan.withdraw()
    definirvaloresmatriz.withdraw()
    valores1.withdraw()
    valores.withdraw()
    ventana25.withdraw()
    ventana.deiconify()
    Menu = Label(ventana,text="Menu:",bg="deepskyblue", font=("Kaufmann BT", 20,"bold"))
    agregar=Label(ventana,text="1. Inversa de una Matriz",bg="deepskyblue",font=("Kaufmann BT", 15, "bold"),anchor="e").place(x = 5, y = 30)
    multiplicacion=Label(ventana,text="2. Multiplicacion",bg="deepskyblue",font=("Kaufmann BT", 15, "bold"),anchor="e").place(x = 5, y = 60)
    multiplicacion_button = Button(ventana, text="Multiplicación de Matrices", bg="blue", fg="white", font=("Arila", 10, "bold"), command=ventana_multiplicacion)
    multiplicacion_button.place(x=5, y=90)
    completada=Label(ventana,text="3. Ecuaciones Lineales", bg="deepskyblue",font=("Kaufmann BT", 15, "bold")).place(x = 5, y = 120)
    valor=Label(ventana,text="Seleccione una Opción:",bg="deepskyblue", font=("Kaufmann BT", 14, "bold")).place(x=60,y=150)
    Entrada_txt.place(x=150,y=190)
    b1 = Button(ventana, text="Confirmar",bg="blue", fg="white", font=("Arila", 10, "bold"),command=rangomatriz)
    b1.place(x=125,y=220)
    boton_grafica = Button(ventana, text="GRAFICAS", bg="blue", fg="white", font=("Arila", 10, "bold"),command=ventana_grafica)
    boton_grafica.place(x=125, y=255)
    Menu.pack()
    ventana.config(bg="deepskyblue")
    ventana.mainloop()

h=0
r=0
valor=[]

def valores3():
    incognita=incognitas.get()
    global h
    global valor
    global r
    if(incognita==""):
        messagebox.showinfo(message="Ingresar valor", title="VACIO")
    else:
        if(incognita.isnumeric()):
                abecedario=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                metodogaussjordan.withdraw()#oculta la ventana de coleccion de datos
                definirvaloresmatriz.withdraw()
                valores1.deiconify()
                #ventana.withdraw()#oculta la ventana principal
                valores1.title("VALORES")
                if not (valores2.get()==""):
                    if(h==0 and r==0):
                        for g in range(int(incognita)):
                            valor.append([0]*(int(incognita)+1))
                    if not (h==int(incognita)+1):
                        valor[r][h]=valores2.get()
                        valores2.delete(0, END)
                        h+=1
                
                if(h<int(incognita)):
                    l=Label(valores1,text="")
                    l=Label(valores1,text="Ingrese valor para la incognita "+abecedario[h]+" en la ecuacion #"+str(r+1),font=("Arial", 10,"bold"))
                    l.grid(row=0, column=0, columnspan=3)
                    valores2.grid(row=2,column=1)
                    b1 = Button(valores1, text="Confirmar",command=valores3)
                    b1.grid(row=4, column=0, columnspan=3)
        
    
                if(h==int(incognita)):
                    l=Label(valores1,text="")
                    l=Label(valores1,text="Ingrese  el  Valor  del  resultado de la ecuacion # "+str(r+1),font=("Arial", 10,"bold"))
                    l.grid(row=0, column=0, columnspan=3)
                    valores2.delete(0, END)
                    b1 = Button(valores1, text="Confirmar",command=valores3)
                    b1.grid(row=4, column=0, columnspan=3)

                if(h==int(incognita)+1 and r<int(incognita)-1):
                    h=0
                    r+=1
                    l=Label(valores1,text="")
                    l=Label(valores1,text="Ingrese valor para la incognita "+abecedario[h]+" en la ecuacion #"+str(r+1),font=("Arial", 10,"bold"))
                    l.grid(row=0, column=0, columnspan=3)
                    valores2.grid(row=2,column=1)
                    b1 = Button(valores1, text="Confirmar",command=valores3)
                    b1.grid(row=4, column=0, columnspan=3)
                    valores2.delete(0, END)
                if(h==int(incognita)+1 and r==int(incognita)-1):
                    h=0
                    r+=1

                if(r==int(incognita)):
                    messagebox.showinfo(message="Valores Completados", title="LLENO")
                    metodogaussjordan.withdraw()#oculta la ventana de coleccion de datos
                    definirvaloresmatriz.deiconify()
                    definirvalores()
                    valores1.withdraw()
    
                v=Label(valores1,text="",font=("Arial", 7,"bold"))
                v.grid(row=5, column=0, columnspan=3)
                valores1.mainloop()
        else:
            messagebox.showinfo(message="Ingresar valor valido", title="ERROR")

def valores4():
    incognita=incognitas.get()
    global h
    global valor
    global r
    
    if(incognita==""):
        messagebox.showinfo(message="Ingresar valor", title="VACIO")
    else:
        if(incognita.isnumeric()):
            if int(incognita) < 2 or int(incognita) > 4:
                messagebox.showinfo(message="Número de ecuaciones no válido.", title="ERROR")
            else:
                abecedario=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                metodogaussjordan.withdraw()#oculta la ventana de coleccion de datos
                definirvaloresmatriz.withdraw()
                valores1.deiconify()
                ventana25.withdraw()
                #ventana.withdraw()#oculta la ventana principal
                valores1.title("VALORES")
                if not (valores2.get()==""):
                    if(h==0 and r==0):
                        for g in range(int(incognita)):
                            valor.append([0]*(int(incognita)+1))
                    if not (h==int(incognita)+1):
                        valor[r][h]=valores2.get()
                        valores2.delete(0, END)
                        h+=1
                
                if(h<int(incognita)):
                    l=Label(valores1,text="")
                    l=Label(valores1,text="Ingrese valor para la incognita "+abecedario[h]+" en la ecuacion #"+str(r+1),font=("Arial", 10,"bold"))
                    l.grid(row=0, column=0, columnspan=3)
                    valores2.grid(row=2,column=1)
                    b1 = Button(valores1, text="Confirmar",command=valores3)
                    b1.grid(row=4, column=0, columnspan=3)
        
    
                if(h==int(incognita)):
                    l=Label(valores1,text="")
                    l=Label(valores1,text="Ingrese  el  Valor  del  resultado de la ecuacion # "+str(r+1),font=("Arial", 10,"bold"))
                    l.grid(row=0, column=0, columnspan=3)
                    valores2.delete(0, END)
                    b1 = Button(valores1, text="Confirmar",command=valores3)
                    b1.grid(row=4, column=0, columnspan=3)

                if(h==int(incognita)+1 and r<int(incognita)-1):
                    h=0
                    r+=1
                    l=Label(valores1,text="")
                    l=Label(valores1,text="Ingrese valor para la incognita "+abecedario[h]+" en la ecuacion #"+str(r+1),font=("Arial", 10,"bold"))
                    l.grid(row=0, column=0, columnspan=3)
                    valores2.grid(row=2,column=1)
                    b1 = Button(valores1, text="Confirmar",command=valores3)
                    b1.grid(row=4, column=0, columnspan=3)
                    valores2.delete(0, END)
                if(h==int(incognita)+1 and r==int(incognita)-1):
                    h=0
                    r+=1

                if(r==int(incognita)):
                    messagebox.showinfo(message="Valores Completados", title="LLENO")
                    metodogaussjordan.withdraw()#oculta la ventana de coleccion de datos
                    metodogaussjordan.withdraw()#oculta la ventana de coleccion de datos
                    definirvaloresmatriz.deiconify()
                    definirvalores()
                    valores1.withdraw()
    
                v=Label(valores1,text="",font=("Arial", 7,"bold"))
                v.grid(row=5, column=0, columnspan=3)
                valores1.mainloop()
        else:
            messagebox.showinfo(message="Ingresar valor valido", title="ERROR")

def definirvalores():
    opcion2=Entrada_txt25.get()
    global valor
    abecedario=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    incognita=incognitas.get()
    hh=0
    tt=0
    for g in range(int(incognita)+1):
        for c in range(int(incognita)+3):
            if(c==0):
                cell = Entry(definirvaloresmatriz,width=5)
                cell.grid(row=g, column=c, padx=2, pady=2)
                cell.insert(0, str(g))
                cell.config(state= "disabled")
                tt=1
            else:
                if(g==0 and c<=int(incognita) and c>0):
                    cell = Entry(definirvaloresmatriz,width=5)
                    cell.grid(row=g, column=c, padx=2, pady=2)
                    cell.insert(0, abecedario[c-1])
                    cell.config(state= "disabled")
                else:
                    if(c==int(incognita)+1):
                        cell = Entry(definirvaloresmatriz,width=5)
                        cell.grid(row=g, column=c, padx=2, pady=2)
                        cell.insert(0, "=")
                        cell.config(state= "disabled")
                        tt=2
                    else:
                        if(g==0 and c==int(incognita)+2):
                            cell = Entry(definirvaloresmatriz,width=5)
                            cell.grid(row=g, column=c, padx=2, pady=2)
                            cell.insert(0, "RESP.")
                            cell.config(state= "disabled")
                        else:
                            cell1=Entry(definirvaloresmatriz,width=5)
                            cell1.grid(row=g, column=c, padx=2, pady=2)
                            cell1.insert(0, '{}'.format(valor[g-1][c-tt]))
    if(opcion2=="2"):                            
        b1 = Button(definirvaloresmatriz, text="Obtener Respuestas",command=respuesta2)
        b1.grid(row=int(incognita)+2, column=1, columnspan=3)
    else:
        b1 = Button(definirvaloresmatriz, text="Obtener Respuestas",command=respuesta)
        b1.grid(row=int(incognita)+2, column=1, columnspan=3)

def respuesta2():
    incognita=int(incognitas.get())
    global valor
    A=[]
    B=[]
    resp=""
    for g in range(incognita):
        A.append([0]*(incognita))
    for i in range(incognita):
        for a in range(incognita+1):
            if(a<incognita):
                A[i][a]=valor[i][a]
            else:
                B.append(valor[i][a])
    AA = np.asarray(A, dtype=float)
    BB=np.asarray(B, dtype=float)
    resultado = regla_cramer(AA, BB)
    if isinstance(resultado, str):
        messagebox.showinfo(message=resultado, title="Resultado")
    else:
        for i, sol in enumerate(resultado):
            resp+=f'x{i + 1} = {sol}'+"  "
    messagebox.showinfo(message=resp, title="Solución del sistema de ecuaciones:")

def regla_cramer(A, B):
    n = A.shape[0]
    det_A = np.linalg.det(A)
    if det_A == 0:
        return "Este sistema no tiene solucion."
    solucion = []
    for i in range(n):
        Ai = A.copy()
        Ai[:, i] = B
        det_Ai = np.linalg.det(Ai)
        xi = det_Ai / det_A
        solucion.append(xi)
    return solucion
        
def imprimirmatriz(a, n):
    for i in range(n):
        print(*a[i])

def imprimirresultados(a, n, flag):
    Resp=""
    abecedario=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if (flag == 2):
        messagebox.showinfo(message="LAS O LA SOLUCION ES INFINITA", title="RESPUESTA")
    elif (flag == 3):
        messagebox.showinfo(message="NO EXISTE SOLUCIÓN", title="RESPUESTA")

    else:
        for i in range(n):
            p=str(a[i][n] / a[i][i])
            Resp+=abecedario[i]+"="+p+", "
    messagebox.showinfo(message=Resp, title="RESPUESTA")
    

def respuesta():
    global valor
    a = np.asarray(valor, dtype=float)
    n = int(incognitas.get())
    flag = 0
    flag = operacion(a, n)
    if (flag == 1):
        flag = Chequearconsistencia(a, n, flag)



matriz1_entries = []
matriz2_entries = []
matrices_creadas = False  

def multiplicar_matrices(matriz1, matriz2):
    result = [[0 for _ in range(len(matriz2[0]))] for _ in range(len(matriz1))]
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                result[i][j] += matriz1[i][k] * matriz2[k][j]
    return result

#---MULTIPLICACION DE MATRICES---
def ventana_multiplicacion():
    ventana.withdraw()
    ventana_multiplicar.deiconify()
    ventana_multiplicar.config(bg="navy")
    def crear_matrices():
        global matrices_creadas
        if matrices_creadas:
            return  

        filas_matriz1 = int(entry_filas_matriz1.get())
        columnas_matriz1 = int(entry_columnas_matriz1.get())
        filas_matriz2 = int(entry_filas_matriz2.get())
        columnas_matriz2 = int(entry_columnas_matriz2.get())

      
        matrices_creadas = False

        
        for row in matriz1_entries:
            for entry in row:
                entry.destroy()
        for row in matriz2_entries:
            for entry in row:
                entry.destroy()

    
        label_matriz1 = Label(ventana_multiplicar, text="MATRIZ A:", bg="navy", fg="white", font=("Arila", 10, "bold"))
        label_matriz1.pack()
        matriz1_entries.extend(crear_entradas_matriz(filas_matriz1, columnas_matriz1, frame1, "Matriz A"))

        label_matriz2 = Label(ventana_multiplicar, text="Matriz B:", bg="navy", fg="white", font=("Arila", 10, "bold"))
        label_matriz2.pack()
        matriz2_entries.extend(crear_entradas_matriz(filas_matriz2, columnas_matriz2, frame2, "Matriz B"))

      
        button_multiplicar = Button(ventana_multiplicar, text="Multiplicar", bg="white", fg="black", font=("Arila", 10, "bold"),command=multiplicar)
        button_multiplicar.pack()

        button_crear_matrices.config(state="disabled")  

    def crear_entradas_matriz(filas, columnas, parent_frame, nombre_matriz):
        matriz_frame = Frame(parent_frame)
        matriz_frame.pack()

        entries = []

        if nombre_matriz:
            # Crear etiqueta con el nombre de la matriz
            label_nombre_matriz = Label(matriz_frame, text=nombre_matriz)
            label_nombre_matriz.grid(row=0, columnspan=columnas, pady=5)

        for i in range(filas):
            row_entries = []
            for j in range(columnas):
                entry = Entry(matriz_frame, width=10)
                entry.grid(row=i + 1, column=j, padx=5, pady=5)
                row_entries.append(entry)
            entries.append(row_entries)
        return entries

    def multiplicar():
        
        matriz1 = obtener_valores(matriz1_entries)
        matriz2 = obtener_valores(matriz2_entries)

        try:
            resultado = multiplicar_matrices(matriz1, matriz2)

            resultado_frame = Frame(ventana_multiplicar, bg="navy")
            resultado_frame.pack()

            resultado_label = Label(resultado_frame, text="Resultado:", bg="navy")
            resultado_label.pack()

            for i, row in enumerate(resultado):
                row_label = Label(resultado_frame, text=str(row))
                row_label.pack()

        except Exception as e:
            messagebox.showerror("Error", "Ha ocurrido un error al multiplicar las matrices.")

    def obtener_valores(entries):
        return [[float(entry.get()) for entry in row] for row in entries]

    label_filas_matriz1 = Label(ventana_multiplicar, text="Filas de Matriz A:", bg="navy", fg="white", font=("Arila", 15, "bold"))
    label_filas_matriz1.pack()
    entry_filas_matriz1 = Entry(ventana_multiplicar, width=10)
    entry_filas_matriz1.pack()

    label_columnas_matriz1 = Label(ventana_multiplicar, text="Columnas de Matriz A:", bg="navy", fg="white", font=("Arila", 15, "bold"))
    label_columnas_matriz1.pack()
    entry_columnas_matriz1 = Entry(ventana_multiplicar, width=10)
    entry_columnas_matriz1.pack()

    label_filas_matriz2 = Label(ventana_multiplicar, text="Filas de Matriz B:", bg="navy", fg="white", font=("Arila", 15, "bold"))
    label_filas_matriz2.pack()
    entry_filas_matriz2 = Entry(ventana_multiplicar, width=10)
    entry_filas_matriz2.pack()

    label_columnas_matriz2 = Label(ventana_multiplicar, text="Columnas de Matriz B:", bg="navy", fg="white", font=("Arila", 15, "bold"))
    label_columnas_matriz2.pack()
    entry_columnas_matriz2 = Entry(ventana_multiplicar, width=10)
    entry_columnas_matriz2.pack()

    frame1 = Frame(ventana_multiplicar, bg="navy")
    frame1.pack()
    
    frame2 = Frame(ventana_multiplicar, bg="navy")
    frame2.pack()

    button_crear_matrices = Button(ventana_multiplicar, text="INGRESAR LAS MATRICES", font=("Arila", 10, "bold"), command=crear_matrices)
    button_crear_matrices.pack()

#---GRAFICA---

def ventana_grafica():
    ventana.withdraw()
    ventana2.deiconify()
    ventana2.config(bg="red")
    ventana2.geometry("425x200")
    Label(ventana2, text="X: ", bg="red", font=("Arila", 10, "bold")).grid(row=0, column=0)
    Label(ventana2, text="Y: ", bg="red", font=("Arila", 10, "bold")).grid(row=0, column=2)
    Label(ventana2, text="TI: ", bg="red", font=("Arila", 10, "bold")).grid(row=0, column=4)

    entry_a1.grid(row=0, column=1)  

    entry_b1.grid(row=0, column=3)

    entry_c1.grid(row=0, column=5)

    Label(ventana2, text="X: ", bg="red", font=("Arila", 10, "bold")).grid(row=1, column=0)
    Label(ventana2, text="Y: ", bg="red", font=("Arila", 10, "bold")).grid(row=1, column=2)
    Label(ventana2, text="TI: ", bg="red", font=("Arila", 10, "bold")).grid(row=1, column=4)

    entry_a2.grid(row=1, column=1)

    entry_b2.grid(row=1, column=3)

    entry_c2.grid(row=1, column=5)

    Button(ventana2, text="GRAFICAR", bg="orange", fg="white", font=("Arila", 10, "bold"),command=graficar_sistema).grid(row=2, column=0, columnspan=6)

def graficar_sistema():
    a1 = float(entry_a1.get())
    b1 = float(entry_b1.get())
    c1 = float(entry_c1.get())
    a2 = float(entry_a2.get())
    b2 = float(entry_b2.get())
    c2 = float(entry_c2.get())

    def ecuacion1(x):
        return (-a1 * x + c1) / b1

    def ecuacion2(x):
        return (-a2 * x + c2) / b2

    x = np.linspace(-10, 10, 100)
    y1 = ecuacion1(x)
    y2 = ecuacion2(x)

    plt.figure(figsize=(6, 6))
    plt.plot(x, y1, label='Ecuación numero 1')
    plt.plot(x, y2, label='Ecuación numero 2')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='navy', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('SISTEMA DE ECUACIONES')
    canvas = FigureCanvasTkAgg(plt.gcf(), master=ventana2)
    canvas.draw()
    canvas.get_tk_widget().grid(row=3, column=0, columnspan=6)


def main():
    Menu()

if __name__ == "__main__":
    main()
