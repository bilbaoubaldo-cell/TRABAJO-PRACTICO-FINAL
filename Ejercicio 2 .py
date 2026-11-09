class EquipoEnergetico():
  def__init__(self, codigo: str, nombre: str, precio: float, stock: int): # type: ignore
             
      self.codigo = codigo # type: ignore
      self.nombre = nombre # pyright: ignore[reportUndefinedVariable]
      self.precio = precio # type: ignore
      self.__stock = 0  # type: ignore
      self.asignar_stock(stock) # type: ignore
  def asignar_stock(self, nuevo_stock):
        if nuevo_stock < 0:
            raise StockInvalidoError(“El stock no puede ser negativo”) # pyright: ignore[reportUndefinedVariable]
         self.__stock = nuevo_stock
   def obtener_stock(self):
          return self.__stock
   def mostrar_ficha_tecnica(self):
    return f”Codigo: {self.codigo} | Precio: ${self.nombre} | Stock: {self.precio}”
class PanelFotovoltaico(EquipoEnergetico):
    def__init__(self, codigo, nombre, precio, stock, potencia_watts, eficiencia):
       super().__init__(codigo, nombre, precio, stock)
       self.potencia_watts = potencia_watts
       self.eficiencia = eficiencia
    def mostrar_ficha_tecnica(self):
       return f”Codigo: {self.codigo} | Precio: ${self.nombre} | Stock: {self.precio} | Potencia: {self.potencia_watts} | Eficiencia: {self.eficiencia}”
class AdministradorCatalogo():
  def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):
         catalogo = []
         for dispositivo in lista_dispositivos:
               producto = {
                    “codigo”: dispositivo.codigo, 
                    “nombre”: dispositivo.nombre,
                    “precio”: dispositivo.precio,
                    “stock”: dispositivo.obtenerstock(),
                }
                if type(dispositivo) == PanelFotovoltaico:
                    producto[“potencia_watts”] = dispositivo.potencia_watts
                    producto[“eficiencia”] = dispositivo.eficiencia
                  catalogo.append(producto)
                with open(ruta_archivo. “W”, encoding=”utf-8”) as file:
                       json.dump(catalogo, file, indent=4)
                 print(“Catálogo guardado correctamente.”)
panel1 = PanelFotovoltaico (
          “PF-001”,
          “Panel Solar Residencial”,
           250_000,
           15,
           450,
            21.5
)
panel2 = PanelFotovoltaico (
           “PF-002”,
           “Panel Solar Industrial”,
            420_000,
            8,
            600,
            23.5
)
equipo1 = EquipoEnergetico(
            “EE-001”,
             “Controlador de Carga”,
              85_000,
              5
)
try:
    panel_invalido = PanelFotovoltaico(
           “PF-003”,
           “Panel Solar Defectuoso”,
            400_000,
            -5,
            850,
            26.5
)
except StockInvalidoError as error:
     print(f “Error controlado: {error}”)
try:
     panel1.asignar_stock(-5)
except StockInvalidoError as error:
     print(f”Error controlado: {error}”)
productos = [panel1, panel2, equipo1]
for producto in productos:
     print(producto.mostrar_ficha_tecnica())
admin_catalogo = AdministradorCatalogo()
admin_catalogo.guardar_catalogo_json(productos, “catalogo_greentech.json”)

[
  {
     “codigo”: “PF-001”,
     “nombre”: “Panel Solar Residencial”,
     “precio”: 250000,
     “stock”: 15,
     “potencia_watts”: 450,
     “eficiencia”: 21.5
   }
  {
     “codigo”: “PF-002”,
     “nombre”: “Panel Solar Industrial”,
     “precio”: 420000,
     “stock”: 8,
     “potencia_watts”: 600,
     “eficiencia”: 23.5
   }
    {
     “codigo”: “EE-001”,
     “nombre”: “Controlador de Carga”,
     “precio”: 85000,
     “stock”: 5,
   }
]