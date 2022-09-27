

def conversor(tipo_peso, valor_dolar): 
    pesos = input('¿Cuantos pesos ' + tipo_peso + ' tienes?: ')
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')


menu = """
Bienvenido al conversor de monedas 💱

1- Pesos Colombianos
2- Pesos Argentinos
3- Pesos Mexicanos

Elige una opción: """



opcion = int(input(menu))


if opcion == 1: 
    conversor('Colombianos', 4565)

elif opcion == 2:
    conversor('Argentinos', 146)
elif opcion == 3: 
    conversor('Mexicanos', 20)
else: 
    print("Por favor ingresa una opcion correcta") 









