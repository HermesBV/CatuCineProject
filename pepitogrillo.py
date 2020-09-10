import cv2
import numpy as np
import os, random

def correr_video1():
    nombr = random.choice(os.listdir(r"C:\\Users\\JLHI6\\Desktop\\CODE\\Catu\\videitos\\bebe"))
    videa = r"C:\\Users\\JLHI6\\Desktop\\CODE\\Catu\\videitos\\bebe\\" + nombr
    vid = cv2.VideoCapture(videa)    
    if (vid.isOpened()== False):
        print("El archivo de mierda no se pudo abrir")

    while (vid.isOpened()):
        ret, frame = vid.read()
        if ret == True:
            cv2.imshow("Frame", frame)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                break

        else:
            break

    vid.release()
    cv2.destroyAllWindows()

def correr_video2():
    nombr = random.choice(os.listdir(r"C:\\Users\\JLHI6\\Desktop\\CODE\\Catu\\videitos\\domestico"))
    videa = r"C:\\Users\\JLHI6\\Desktop\\CODE\\Catu\\videitos\\domestico\\" + nombr
    vid = cv2.VideoCapture(videa)    
    if (vid.isOpened()== False):
        print("El archivo de mierda no se pudo abrir")

    while (vid.isOpened()):
        ret, frame = vid.read()
        if ret == True:
            cv2.imshow("Frame", frame)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                break

        else:
            break

    vid.release()
    cv2.destroyAllWindows()

def correr_video3():
    nombr = random.choice(os.listdir(r"C:\\Users\\JLHI6\\Desktop\\CODE\\Catu\\videitos\\eventos"))
    videa = r"C:\\Users\\JLHI6\\Desktop\\CODE\\Catu\\videitos\\eventos\\" + nombr
    vid = cv2.VideoCapture(videa)    
    if (vid.isOpened()== False):
        print("El archivo de mierda no se pudo abrir")

    while (vid.isOpened()):
        ret, frame = vid.read()
        if ret == True:
            cv2.imshow("Frame", frame)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                break

        else:
            break

    vid.release()
    cv2.destroyAllWindows()

def correr_video4():
    nombr = random.choice(os.listdir(r"C:\\Users\\JLHI6\\Desktop\\CODE\\Catu\\videitos\\exterior"))
    videa = r"C:\\Users\\JLHI6\\Desktop\\CODE\\Catu\\videitos\\exterior\\" + nombr
    vid = cv2.VideoCapture(videa)    
    if (vid.isOpened()== False):
        print("El archivo de mierda no se pudo abrir")

    while (vid.isOpened()):
        ret, frame = vid.read()
        if ret == True:
            cv2.imshow("Frame", frame)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                break

        else:
            break

    vid.release()
    cv2.destroyAllWindows()

def correr_video5():
    nombr = random.choice(os.listdir(r"C:\\Users\\JLHI6\\Desktop\\CODE\\Catu\\videitos\\juego"))
    videa = r"C:\\Users\\JLHI6\\Desktop\\CODE\\Catu\\videitos\\juego\\" + nombr
    vid = cv2.VideoCapture(videa)    
    if (vid.isOpened()== False):
        print("El archivo de mierda no se pudo abrir")

    while (vid.isOpened()):
        ret, frame = vid.read()
        if ret == True:
            cv2.imshow("Frame", frame)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                break

        else:
            break

    vid.release()
    cv2.destroyAllWindows()

def correr_video6():
    nombr = random.choice(os.listdir(r"C:\\Users\\JLHI6\\Desktop\\CODE\\Catu\\videitos\\mama"))
    videa = r"C:\\Users\\JLHI6\\Desktop\\CODE\\Catu\\videitos\\mama\\" + nombr
    vid = cv2.VideoCapture(videa)    
    if (vid.isOpened()== False):
        print("El archivo de mierda no se pudo abrir")

    while (vid.isOpened()):
        ret, frame = vid.read()
        if ret == True:
            cv2.imshow("Frame", frame)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                break

        else:
            break

    vid.release()
    cv2.destroyAllWindows()

def correr_video7():
    nombr = random.choice(os.listdir(r"C:\\Users\\JLHI6\\Desktop\\CODE\\Catu\\videitos\\movimiento"))
    videa = r"C:\\Users\\JLHI6\\Desktop\\CODE\\Catu\\videitos\\movimiento\\" + nombr
    vid = cv2.VideoCapture(videa)    
    if (vid.isOpened()== False):
        print("El archivo de mierda no se pudo abrir")

    while (vid.isOpened()):
        ret, frame = vid.read()
        if ret == True:
            cv2.imshow("Frame", frame)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                break

        else:
            break

    vid.release()
    cv2.destroyAllWindows()

def correr_video8():
    nombr = random.choice(os.listdir(r"C:\\Users\\JLHI6\\Desktop\\CODE\\Catu\\videitos\\nieve"))
    videa = r"C:\\Users\\JLHI6\\Desktop\\CODE\\Catu\\videitos\\nieve\\" + nombr
    vid = cv2.VideoCapture(videa)    
    if (vid.isOpened()== False):
        print("El archivo de mierda no se pudo abrir")

    while (vid.isOpened()):
        ret, frame = vid.read()
        if ret == True:
            cv2.imshow("Frame", frame)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                break

        else:
            break

    vid.release()
    cv2.destroyAllWindows()

def correr_video9():
    nombr = random.choice(os.listdir(r"C:\\Users\\JLHI6\\Desktop\\CODE\\Catu\\videitos\\risas"))
    videa = r"C:\\Users\\JLHI6\\Desktop\\CODE\\Catu\\videitos\\risas\\" + nombr
    vid = cv2.VideoCapture(videa)    
    if (vid.isOpened()== False):
        print("El archivo de mierda no se pudo abrir")

    while (vid.isOpened()):
        ret, frame = vid.read()
        if ret == True:
            cv2.imshow("Frame", frame)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                break

        else:
            break

    vid.release()
    cv2.destroyAllWindows()

def correr_video10():
    nombr = random.choice(os.listdir(r"C:\\Users\\JLHI6\\Desktop\\CODE\\Catu\\videitos\\zoom"))
    videa = r"C:\\Users\\JLHI6\\Desktop\\CODE\\Catu\\videitos\\zoom\\" + nombr
    vid = cv2.VideoCapture(videa)    
    if (vid.isOpened()== False):
        print("El archivo de mierda no se pudo abrir")

    while (vid.isOpened()):
        ret, frame = vid.read()
        if ret == True:
            cv2.imshow("Frame", frame)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                break

        else:
            break

    vid.release()
    cv2.destroyAllWindows()

def correr_videos(conteo):
    if conteo == 1:
        correr_video1()
    elif conteo == 2:
        correr_video2()
        correr_video3()
    elif conteo == 3:
        correr_video4()
        correr_video5()
        correr_video6()
    elif conteo == 4:
        correr_video7()
        correr_video8()
        correr_video9()
        correr_video10()
    elif conteo == 5:
        correr_video3()
        correr_video1()
        correr_video8()
        correr_video4()
        correr_video10()
    elif conteo == 6:
        correr_video2()
        correr_video7()
        correr_video5()
        correr_video8()
        correr_video4()
        correr_video6()
    elif conteo == 7:
        correr_video7()
        correr_video10()
        correr_video4()
        correr_video2()
        correr_video1()
        correr_video3()
        correr_video8()
    elif conteo == 8:
        correr_video8()
        correr_video10()
        correr_video1()
        correr_video3()
        correr_video2()
        correr_video9()
        correr_video4()
        correr_video5()
    elif conteo == 9:
        correr_video7()
        correr_video1()
        correr_video2()
        correr_video4()
        correr_video5()
        correr_video8()
        correr_video10()
        correr_video3()
        correr_video6()
    elif conteo == 10:
        correr_video5()
        correr_video6()
        correr_video10()
        correr_video3()
        correr_video7()
        correr_video4()
        correr_video9()
        correr_video2()
        correr_video8()
        correr_video1()
    elif conteo == 11:
        correr_video4()
        correr_video5()
        correr_video1()
        correr_video3()
        correr_video9()
        correr_video2()
        correr_video6()
        correr_video7()
        correr_video8()
        correr_video10()
        correr_video5()
    elif conteo == 12:
        correr_video5()
        correr_video6()
        correr_video1()
        correr_video7()
        correr_video9()
        correr_video2()
        correr_video3()
        correr_video4()
        correr_video8()
        correr_video10()
        correr_video5()
        correr_video1()
    elif conteo == 13:
        correr_video3()
        correr_video5()
        correr_video6()
        correr_video9()
        correr_video10()
        correr_video2()
        correr_video1()
        correr_video4()
        correr_video7()
        correr_video10()
        correr_video4()
        correr_video3()
        correr_video5()
    elif conteo == 14:
        correr_video10()
        correr_video3()
        correr_video4()
        correr_video7()
        correr_video3()
        correr_video1()
        correr_video6()
        correr_video4()
        correr_video9()
        correr_video10()
        correr_video2()
        correr_video5()
        correr_video8()
    elif conteo == 15:
        correr_video1()
        correr_video8()
        correr_video2()
        correr_video8()
        correr_video3()
        correr_video10()
        correr_video6()
        correr_video4()
        correr_video5()
        correr_video9()
        correr_video4()
        correr_video2()
        correr_video7()
        correr_video10()
        correr_video3()
    elif conteo == 16:
        correr_video1()
        correr_video9()
        correr_video1()
        correr_video5()
        correr_video2()
        correr_video10()
        correr_video3()
        correr_video8()
        correr_video4()
        correr_video7()
        correr_video5()
        correr_video10()
        correr_video6()
        correr_video3()
        correr_video7()
        correr_video2()
    elif conteo == 17:
        correr_video1()
        correr_video9()
        correr_video1()
        correr_video5()
        correr_video2()
        correr_video10()
        correr_video3()
        correr_video8()
        correr_video4()
        correr_video7()
        correr_video5()
        correr_video10()
        correr_video4()
        correr_video3()
        correr_video7()
        correr_video2()
        correr_video6()
    elif conteo == 18:
        correr_video10()
        correr_video6()
        correr_video4()
        correr_video2()
        correr_video1()
        correr_video3()
        correr_video5()
        correr_video8()
        correr_video7()
        correr_video10()
        correr_video2()
        correr_video4()
        correr_video3()
        correr_video5()
        correr_video8()
        correr_video7()
        correr_video9()
        correr_video1()
    elif conteo == 19:
        correr_video10()
        correr_video6()
        correr_video4()
        correr_video2()
        correr_video1()
        correr_video3()
        correr_video5()
        correr_video8()
        correr_video7()
        correr_video10()
        correr_video2()
        correr_video4()
        correr_video3()
        correr_video5()
        correr_video8()
        correr_video7()
        correr_video9()
        correr_video1()
        correr_video4()
    elif conteo == 20:
        correr_video4()
        correr_video3()
        correr_video2()
        correr_video5()
        correr_video7()
        correr_video9()
        correr_video8()
        correr_video6()
        correr_video1()
        correr_video2()
        correr_video8()
        correr_video3()
        correr_video4()
        correr_video10()
        correr_video2()
        correr_video8()
        correr_video5()
        correr_video4()
        correr_video10()
        correr_video1()
    elif conteo == 21:
        correr_video2()
        correr_video3()
        correr_video6()
        correr_video1()
        correr_video8()
        correr_video7()
        correr_video4()
        correr_video3()
        correr_video2()
        correr_video8()
        correr_video7()
        correr_video1()
        correr_video9()
        correr_video10()
        correr_video5()
        correr_video5()
        correr_video10()
        correr_video3()
        correr_video4()
        correr_video6()
        correr_video1()
    elif conteo == 22:
        correr_video10()
        correr_video6()
        correr_video4()
        correr_video2()
        correr_video1()
        correr_video3()
        correr_video5()
        correr_video8()
        correr_video7()
        correr_video10()
        correr_video2()
        correr_video4()
        correr_video3()
        correr_video5()
        correr_video8()
        correr_video7()
        correr_video9()
        correr_video1()
        correr_video2()
        correr_video4()
        correr_video6()
        correr_video1()
    elif conteo == 23:
        correr_video2()
        correr_video3()
        correr_video6()
        correr_video1()
        correr_video8()
        correr_video7()
        correr_video4()
        correr_video3()
        correr_video2()
        correr_video8()
        correr_video7()
        correr_video1()
        correr_video9()
        correr_video10()
        correr_video5()
        correr_video4()
        correr_video3()
        correr_video10()
        correr_video6()
        correr_video1()
        correr_video8()
        correr_video7()
        correr_video4()
    elif conteo == 24:
        correr_video1()
        correr_video9()
        correr_video1()
        correr_video5()
        correr_video2()
        correr_video10()
        correr_video3()
        correr_video8()
        correr_video4()
        correr_video7()
        correr_video5()
        correr_video10()
        correr_video4()
        correr_video3()
        correr_video7()
        correr_video2()
        correr_video6()
        correr_video4()
        correr_video3()
        correr_video2()
        correr_video8()
        correr_video7()
        correr_video1()
        correr_video9()
    elif conteo == 25:
        correr_video1()
        correr_video9()
        correr_video1()
        correr_video5()
        correr_video2()
        correr_video10()
        correr_video3()
        correr_video8()
        correr_video4()
        correr_video7()
        correr_video5()
        correr_video10()
        correr_video4()
        correr_video3()
        correr_video7()
        correr_video2()
        correr_video6()
        correr_video4()
        correr_video3()
        correr_video2()
        correr_video8()
        correr_video7()
        correr_video1()
        correr_video9()
        correr_video6()

import tkinter as tk

def texto_ingresado():
    frase = campo_de_texto.get()
    archivo.write(frase+"\n")
    campo_de_texto.delete(0, tk.END)
    lista_frase = frase.split()
    conteo = 0
    for element in lista_frase:
        if len(element) > 3:
            conteo = conteo + 1
        else:
            conteo = conteo
    correr_videos(conteo)

archivo = open('data.txt', 'a')
archivo.write("Iniciando:\n")
master = tk.Tk()
tk.Label(master, text="Introduzca una frase por favor").grid(row=0)
campo_de_texto = tk.Entry(master)
campo_de_texto.grid(row=1)
tk.Button(master, text="Ingresar", command=texto_ingresado).grid(row=2)
master.mainloop()