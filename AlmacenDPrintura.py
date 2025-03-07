class Pintura:
    # esta clase representa una pintura en el almacén.
    
    def __init__(self,nombre,color,cantidad,disponible=True):
        # se asignan los atributos de la pintura.
        self.nombre=nombre
        self.color=color
        self.cantidad=cantidad
        self.disponible=disponible
    
    def comprar(self,cantidad):
        # se compra pintura. si hay suficiente, se descuenta la cantidad.
        if self.disponible and self.cantidad>=cantidad:
            self.cantidad-=cantidad
            if self.cantidad==0:
                self.disponible=False  # si la cantidad llega a 0, se marca como agotado.
            return True
        return False
    
    def cambiar(self,cantidad,defecto=False):
        # se cambia pintura. si tiene defecto, se devuelve al almacén.
        if defecto:
            self.cantidad+=cantidad  # se devuelve la cantidad al almacén.
            self.disponible=True
            return True
        elif self.cantidad>=cantidad:
            self.cantidad+=cantidad  # se incrementa la cantidad sin defecto.
            return True
        return False
    
    def __str__(self):
        # se muestra la información de la pintura.
        estado="disponible" if self.disponible else "agotado"
        return self.nombre+" - color: "+self.color+" - cantidad: "+str(self.cantidad)+" - "+estado

# definición de la clase compra
class Compra:
    # esta clase representa una compra de pintura.
    
    def __init__(self,usuario,pintura,cantidad):
        # se asignan los datos de la compra.
        self.usuario=usuario
        self.pintura=pintura
        self.cantidad=cantidad
    
    def __str__(self):
        # se muestra la compra realizada.
        return "el "+self.usuario.nombre+" compró "+str(self.cantidad)+" unidades de "+self.pintura.nombre+" ("+self.pintura.color+")"

# definición de la clase usuario
class Usuario:
    # esta clase representa un usuario del almacén.
    
    def __init__(self,nombre):
        # se asigna el usuario con su nombre y listas vacías.
        self.nombre=nombre
        self.pinturas=[]  # lista de pinturas compradas.
        self.historial_compras=[]  # historial de compras realizadas.
    
    def comprar_pintura(self,pintura,cantidad):
        # se compra pintura. se agrega al usuario si hay suficiente.
        if pintura.comprar(cantidad):
            self.pinturas.append((pintura,cantidad))
            compra=Compra(self,pintura,cantidad)  # se registra la compra.
            self.historial_compras.append(compra)
            return True
        return False
    
    def cambiar_pintura(self,pintura,cantidad,defecto=False):
        # se cambia pintura. puede ser por defecto o por decisión del usuario.
        for pint,cant in self.pinturas:
            if pint==pintura and cant>=cantidad:
                if pintura.cambiar(cantidad,defecto):
                    if cant==cantidad:
                        self.pinturas.remove((pint,cant))  # se elimina si se devuelve todo.
                    else:
                        self.pinturas.remove((pint,cant))
                        self.pinturas.append((pint,cant-cantidad))  # se actualiza la cantidad.
                    return True
        return False
    
    def listar_pinturas(self):
        # se listan las pinturas compradas.
        return self.pinturas
    
    def ver_historial_compras(self):
        # se muestra el historial de compras.
        return self.historial_compras

# definición de la clase almacen
class Almacen:
    # esta clase representa el almacén de pinturas.
    
    def __init__(self,nombre):
        # se asigna el almacén con su nombre y listas vacías.
        self.nombre=nombre
        self.pinturas=[]  # lista de pinturas disponibles.
        self.usuarios=[]  # lista de usuarios registrados.
    
    def agregar_pintura(self,pintura):
        # se agrega pinturas al almacén.
        self.pinturas.append(pintura)
    
    def registrar_usuario(self,usuario):
        # se registra usuarios en el almacén.
        self.usuarios.append(usuario)
    
    def pinturas_disponibles(self):
        # se listan las pinturas disponibles.
        return [pintura for pintura in self.pinturas if pintura.disponible]
    
    def pinturas_agotadas(self):
        # se listan las pinturas agotadas.
        return [pintura for pintura in self.pinturas if not pintura.disponible]

# ejemplo de uso
def main():
    # se crea el almacén de pinturas
    almacen=Almacen("Pintuco")
    
    # se crean pinturas disponibles en el almacén
    pintura1=Pintura("pintura mate","rojo",50)
    pintura2=Pintura("pintura satinada","azul",30)
    pintura3=Pintura("pintura brillante","verde",20)
    
    # se agregan pinturas al almacén
    almacen.agregar_pintura(pintura1)
    almacen.agregar_pintura(pintura2)
    almacen.agregar_pintura(pintura3)
    
    # se crea y a la vez se registra un usuario en el almacén
    usuario=Usuario("IngDaniel")
    almacen.registrar_usuario(usuario)
    
    # se muestra estado inicial del almacén
    print("estado inicial:")
    for pintura in almacen.pinturas:
        print(" - "+str(pintura))
    
    # el usuario compra una pintura
    usuario.comprar_pintura(pintura1,10)
    print("\ndespués de la compra:")
    for pintura in almacen.pinturas:
        print(" - "+str(pintura))
    
    # se muestra las pinturas compradas por el usuario
    print("\npinturas de IngDaniel:")
    for pintura,cantidad in usuario.listar_pinturas():
        print(" - "+str(pintura)+" - cantidad: "+str(cantidad))
    
    # el usuario devuelve pintura por defecto
    usuario.cambiar_pintura(pintura1,5,True)
    print("\ndespués de la devolución por defecto:")
    for pintura in almacen.pinturas:
        print(" - "+str(pintura))
    
    # se muestra el historial de compras del usuario
    print("\nhistorial de compras de IngDaniel:")
    for compra in usuario.ver_historial_compras():
        print(" - "+str(compra))

# ejecutar el programa
if __name__=="__main__":
    main()
