class Ventana:
    def __init__(self,titulo,xsi1=0,ysi1=0,xid2=500,yid2=500):
        self.__titulo=titulo
        
        if xsi1 < 0:
            xsi1=0
            
        if ysi1 < 0:
            ysi1=0
            
        if xid2 > 500:
            xid2=500
            
        if yid2 > 500:
            yid2=500
            
        if xsi1 >= xid2:
            xid2=xsi1+1
            
        if ysi1 >= yid2:
            yid2=ysi1+1
            
        self.__xsi1=xsi1
        self.__ysi1=ysi1
        self.__xid2=xid2
        self.__yid2=yid2

    def mostrar(self):
        print(f"el titulo es {self.__titulo}")
        print(f"vertice superior izquierdo {self.__xsi1} {self.__ysi1} ")
        print(f"vertice inferior derecho {self.__xid2} {self.__yid2} ")

    def getTitulo(self):
        return self.__titulo
    
    def alto(self):
        return self.__yid2 - self.__ysi1
        
    def ancho(self):    
        return self.__xid2 - self.__xsi1

    def moverDerecha(self,uni=1):
        self.__xid2+=uni
        self.__xsi1+=uni
        if self.__xid2 > 500:
            self.__xid2=500
            self.__xsi1=self.__xid2 - self.ancho()
    
    
    def moverIzquierda(self,uni=1):
        self.__xid2+=uni
        self.__xsi1+=uni
        if self.__xsi1<0:
            self.__xsi1=0
            self.__xid2=self.__xsi1+self.ancho()
    
    def bajar(self,uni=1):
        self.__ysi1 += uni
        self.__yid2 += uni
        if self.__yid2 > 500:
            self.__yid2 = 500
            self.__ysi1 = self.__yid2 - self.alto()
        
    def subir(self,uni=1):
        self.__ysi1 -= uni
        self.__yid2 -= uni
        if self.__ysi1 < 0:
            self.__ysi1 = 0
            self.__yid2 = self.__ysi1 + self.alto()


if __name__=='__main__':
    print('==== Ventana Inicio ====')
    ventanaInicio= Ventana('Inicio')
    ventanaInicio.mostrar()
    print('Ventana: {} Alto: {} Ancho: {}'.format(ventanaInicio.getTitulo(),ventanaInicio.alto(),ventanaInicio.ancho()))
    print('==== Ventana Cargar ====')
    ventanaCargar= Ventana('Cargar',10,20)
    ventanaCargar.mostrar()
    print('*** Mueve a la derecha ***')
    ventanaCargar.moverDerecha(10)
    ventanaCargar.mostrar()
    print('*** Mueve a la izquierda ***')
    ventanaCargar.moverIzquierda(10)
    ventanaCargar.mostrar()
    print('*** Bajar ***')
    ventanaCargar.bajar(10)
    ventanaCargar.mostrar()
    print('==== Ventana Borrar ====')
    ventanaBorrar = Ventana('Borrar', 10,20,100,200)
    ventanaBorrar.mostrar()
    print('*** Subir ***')
    ventanaBorrar.subir(5)   
    ventanaBorrar.mostrar()
    print('*** Subir ***')
    ventanaBorrar.subir()
    ventanaBorrar.mostrar()
    print('*** Bajar ***')
    ventanaBorrar.bajar()
    ventanaBorrar.mostrar()