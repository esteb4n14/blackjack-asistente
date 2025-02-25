# Representación completa de la tabla de estrategia básica del Blackjack
estrategia = {
    'duros': {
        4: {'2': 'P', '3': 'P', '4': 'P', '5': 'P', '6': 'P', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        5: {'2': 'P', '3': 'P', '4': 'P', '5': 'P', '6': 'P', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        6: {'2': 'P', '3': 'P', '4': 'P', '5': 'P', '6': 'P', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        7: {'2': 'P', '3': 'P', '4': 'P', '5': 'P', '6': 'P', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        8: {'2': 'P', '3': 'P', '4': 'P', '5': 'P', '6': 'P', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        9: {'2': 'P', '3': 'D', '4': 'D', '5': 'D', '6': 'D', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        10: {'2': 'D', '3': 'D', '4': 'D', '5': 'D', '6': 'D', '7': 'D', '8': 'D', '9': 'D', '10': 'P', 'A': 'P'},
        11: {'2': 'D', '3': 'D', '4': 'D', '5': 'D', '6': 'D', '7': 'D', '8': 'D', '9': 'D', '10': 'D', 'A': 'D'},
        12: {'2': 'P', '3': 'P', '4': 'Q', '5': 'Q', '6': 'Q', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        13: {'2': 'Q', '3': 'Q', '4': 'Q', '5': 'Q', '6': 'Q', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        14: {'2': 'Q', '3': 'Q', '4': 'Q', '5': 'Q', '6': 'Q', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        15: {'2': 'Q', '3': 'Q', '4': 'Q', '5': 'Q', '6': 'Q', '7': 'P', '8': 'P', '9': 'P', '10': 'R', 'A': 'P'},
        16: {'2': 'Q', '3': 'Q', '4': 'Q', '5': 'Q', '6': 'Q', '7': 'P', '8': 'P', '9': 'R', '10': 'R', 'A': 'R'},
        17: {'2': 'Q', '3': 'Q', '4': 'Q', '5': 'Q', '6': 'Q', '7': 'Q', '8': 'Q', '9': 'Q', '10': 'Q', 'A': 'Q'},
        18: {'2': 'Q', '3': 'Q', '4': 'Q', '5': 'Q', '6': 'Q', '7': 'Q', '8': 'Q', '9': 'Q', '10': 'Q', 'A': 'Q'},
        19: {'2': 'Q', '3': 'Q', '4': 'Q', '5': 'Q', '6': 'Q', '7': 'Q', '8': 'Q', '9': 'Q', '10': 'Q', 'A': 'Q'},
        20: {'2': 'Q', '3': 'Q', '4': 'Q', '5': 'Q', '6': 'Q', '7': 'Q', '8': 'Q', '9': 'Q', '10': 'Q', 'A': 'Q'},
        21: {'2': 'Q', '3': 'Q', '4': 'Q', '5': 'Q', '6': 'Q', '7': 'Q', '8': 'Q', '9': 'Q', '10': 'Q', 'A': 'Q'}
    },
    'blandos': {
        'A,2': {'2': 'P', '3': 'P', '4': 'P', '5': 'D', '6': 'D', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        'A,3': {'2': 'P', '3': 'P', '4': 'D', '5': 'D', '6': 'D', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        'A,4': {'2': 'P', '3': 'P', '4': 'D', '5': 'D', '6': 'D', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        'A,5': {'2': 'P', '3': 'P', '4': 'D', '5': 'D', '6': 'D', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        'A,6': {'2': 'P', '3': 'D', '4': 'D', '5': 'D', '6': 'D', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        'A,7': {'2': 'Q', '3': 'Q', '4': 'Q', '5': 'D', '6': 'D', '7': 'Q', '8': 'Q', '9': 'P', '10': 'P', 'A': 'P'},
        'A,8': {'2': 'Q', '3': 'Q', '4': 'Q', '5': 'Q', '6': 'Q', '7': 'Q', '8': 'Q', '9': 'Q', '10': 'Q', 'A': 'Q'},
        'A,9': {'2': 'Q', '3': 'Q', '4': 'Q', '5': 'Q', '6': 'Q', '7': 'Q', '8': 'Q', '9': 'Q', '10': 'Q', 'A': 'Q'}
    },
    'pares': {
        '2,2': {'2': 'S', '3': 'S', '4': 'S', '5': 'S', '6': 'S', '7': 'S', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        '3,3': {'2': 'S', '3': 'S', '4': 'S', '5': 'S', '6': 'S', '7': 'S', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        '4,4': {'2': 'P', '3': 'P', '4': 'P', '5': 'S', '6': 'S', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        '5,5': {'2': 'D', '3': 'D', '4': 'D', '5': 'D', '6': 'D', '7': 'D', '8': 'D', '9': 'D', '10': 'P', 'A': 'P'},
        '6,6': {'2': 'S', '3': 'S', '4': 'S', '5': 'S', '6': 'S', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        '7,7': {'2': 'S', '3': 'S', '4': 'S', '5': 'S', '6': 'S', '7': 'S', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        '8,8': {'2': 'S', '3': 'S', '4': 'S', '5': 'S', '6': 'S', '7': 'S', '8': 'S', '9': 'S', '10': 'S', 'A': 'S'},
        '9,9': {'2': 'S', '3': 'S', '4': 'S', '5': 'S', '6': 'S', '7': 'P', '8': 'S', '9': 'S', '10': 'P', 'A': 'P'},
        '10,10': {'2': 'Q', '3': 'Q', '4': 'Q', '5': 'Q', '6': 'Q', '7': 'Q', '8': 'Q', '9': 'Q', '10': 'Q', 'A': 'Q'},
        'A,A': {'2': 'S', '3': 'S', '4': 'S', '5': 'S', '6': 'S', '7': 'S', '8': 'S', '9': 'S', '10': 'S', 'A': 'S'}
    }
}

def determinar_tipo_mano(mano):
    """Determina si la mano es dura, blanda o par."""
    if len(mano) == 2 and mano[0] == mano[1]:
        return 'pares'
    elif 1 in mano:
        # Si hay un As, es una mano blanda
        total = sum(mano)
        if total + 10 <= 21:
            return 'blandos'
        else:
            return 'duros'  # Si el As solo puede valer 1, entonces es una mano dura
    return 'duros'

def obtener_valor_blando(mano):
    """Obtiene el valor de una mano blanda en formato 'A,X'."""
    mano.sort()
    ases = [carta for carta in mano if carta == 1]
    otras_cartas = [carta for carta in mano if carta != 1]
    if len(ases) == 1:
        return f"A,{otras_cartas[0]}"
    return None

def obtener_accion(jugador, crupier):
    """Devuelve la acción recomendada basada en la tabla."""
    tipo_mano = determinar_tipo_mano(jugador)
    
    if tipo_mano == 'duros':
        total = sum(jugador)
        return estrategia['duros'][total][str(crupier)]
    elif tipo_mano == 'blandos':
        valor_blando = obtener_valor_blando(jugador)
        return estrategia['blandos'][valor_blando][str(crupier)]
    else:
        par = ','.join(map(str, jugador))
        return estrategia['pares'][par][str(crupier)]

def validar_entrada_jugador(cartas):
    """Valida que las cartas del jugador sean números entre 1 y 11."""
    for carta in cartas:
        if carta < 1 or carta > 11:
            return False
    return True

def main():
    print("Bienvenido al Asistente de Estrategia de Blackjack!")
    while True:
        try:
            # Entrada del jugador
            jugador_input = input("Ingresa tus cartas separadas por comas (ejemplo: 10,6): ")
            jugador = list(map(int, jugador_input.split(',')))
            
            if not validar_entrada_jugador(jugador):
                print("Error: Las cartas deben ser números entre 1 y 11.")
                continue
            
            # Entrada del crupier
            crupier_input = input("Ingresa la carta visible del crupier (2-11 o 'A' para As): ")
            if crupier_input.upper() == 'A':
                crupier = 'A'  # Usamos 'A' directamente para buscar en la tabla
            else:
                crupier = int(crupier_input)
                if crupier < 2 or crupier > 11:
                    print("Error: La carta del crupier debe ser un número entre 2 y 11 o 'A'.")
                    continue
            
            # Obtener la acción recomendada
            accion = obtener_accion(jugador, crupier)
            
            # Mostrar la acción
            acciones_legibles = {
                'P': 'Pedir',
                'Q': 'Quedarse',
                'D': 'Doblar',
                'S': 'Separar',
                'R': 'Rendirse'
            }
            print(f"Recomendación: {acciones_legibles.get(accion, 'Acción desconocida')}")
        
        except Exception as e:
            print(f"Error: {e}. Por favor, intenta de nuevo.")
        
        continuar = input("\n¿Deseas realizar otra consulta? (s/n): ").lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()