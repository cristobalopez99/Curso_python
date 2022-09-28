def run():
    el_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    # print(el_diccionario['llave1'])
    # print(el_diccionario['llave2'])
    # print(el_diccionario['llave3'])

    poblacion_de_paises = {
        'Colombia': 48789320,
        'Mexico': 128789510,
        'Argentina': 46110820,
    }

    # for pais in poblacion_de_paises.values():
    #     print(pais)

    for pais, poblacion in poblacion_de_paises.items():
        print(pais  + ' tiene  ' + str(poblacion) + ' habitantes')



if __name__ == '__main__':
    run()