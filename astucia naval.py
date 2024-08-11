import random
#clase tablero
class Tablero:
    def __init__(self):
        self.tamaño = 10
        self.posiciones = []

    def crearTablero(self):
        for _ in range(self.tamaño):
            campos = ["?"] * self.tamaño
            self.posiciones.append(campos)

    def mostrarTablero(self):
        print("****************************")
        print("   ASTUCIA NAVAL SOLITARIO ")
        print("****************************")

        for fila in self.posiciones:
            print("  ".join(fila))
    
    def verificarTablero(self,fila,columna):
        if self.posiciones[fila-1][columna-1]=="?":
            return True
        else:
            return False

#clase disparo
class Disparo:
    def __init__(self, tableroJugador, barcos):
        self.tableroJugador = tableroJugador
        self.barcos = barcos
        self.aciertos = 0

    def disparar(self, fila, columna):
        print(f"Disparando a la posición ({fila}, {columna})")
        if self.tableroJugador.verificarTablero(fila,columna):
            if self.barcos.verificarBarco(fila, columna):
                self.tableroJugador.posiciones[fila - 1][columna - 1] = "B"
                print("¡Le diste a un barco!")
                self.aciertos = self.aciertos +1
                if self.aciertos >= 9:
                    print("GANASTE EL JUEGO")
                    return self.aciertos
            else:
                self.tableroJugador.posiciones[fila - 1][columna - 1] = "-"
                print("No le diste a ningún barco")
        else:
            print("ya disparaste a ese campo antes, dispara a un lugar diferente esta vez")

class Barcos:
    def __init__(self, tableroJugador):
        self.tableroJugador = tableroJugador
        self.barcos = []

    def crearBarco(self, fila, columna, orientacion):
        posiciones = []
        if 0 <= fila+2 < self.tableroJugador.tamaño and 0 <= columna+2 < self.tableroJugador.tamaño:
            if orientacion == "horizontal":
                if columna + 2 < self.tableroJugador.tamaño:
                    for i in range(3):
                        posiciones.append((fila, columna + i))
            elif orientacion == "vertical":
                if fila + 2 < self.tableroJugador.tamaño:
                    for i in range(3):
                        posiciones.append((fila + i, columna))
            else:
                print("Orientación equivocada")
                return

            self.barcos.append(posiciones)
            return True
        else:
            return False

    def verificarBarco(self, fila, columna):
        for posicion in self.barcos:
            if (fila, columna) in posicion:
                return True
        return False


def jugar():
    #creacion de tableros
    tableroJugador = Tablero()
    tableroJugador.crearTablero()
    #creacion de barco
    barco = Barcos(tableroJugador)
    while not barco.crearBarco(random.randint(1,10),random.randint(1,10),"horizontal"):
        pass
    while not barco.crearBarco(random.randint(1,10),random.randint(1,10),"vertical"):
        pass
    while not barco.crearBarco(random.randint(1,10),random.randint(1,10),"horizontal"):
        pass
    #creacion disparo 
    disparoJugador = Disparo(tableroJugador, barco)
    for i in barco.barcos:
        print(i)

    while disparoJugador.aciertos < 9 :
        while True:
            try:
                fila = int(input("digite la fila en la que va a disparar entre 1 y 10 --  "))
                if 0 < fila < tableroJugador.tamaño:
                    break
                else:
                    print("Error de digitación. Introduzca un número válido entre 1 y 10.")
            except ValueError:
                print("error de digitacion introduzca un numero valido")

        while True:
            try:
                columna = int(input("digite la columna en la que va a disparar entre 1 y 10 --  "))
                if 0 < columna < tableroJugador.tamaño:
                    break
                else:
                    print("Error de digitación. Introduzca un número válido entre 1 y 10.")
            except ValueError:
                print("error de digitacion introduzca un numero valido")


        disparoJugador.disparar(fila,columna)
        tableroJugador.mostrarTablero()




    
# juego

jugar()







