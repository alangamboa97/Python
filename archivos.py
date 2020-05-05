import turtle

def main():
    filename = input("Ingresa el nombre del archivo")

    t = turtle.Turtle()

    screen = t.getscreen()

    archivo = open(filename, "r")

    for linea in archivo:

        text = linea.strip() #une todos las lineas

        comandos = text.split(",") #lee las instrucciones separadas por un ,



        comando = comandos[0]