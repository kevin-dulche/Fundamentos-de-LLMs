import time

def pausar_y_continuar(mensaje="Presiona Enter para continuar..."):
    """Función para pausar la ejecución y esperar al usuario."""
    input(f"\n{mensaje}")
    print("-" * 60)

def obtener_numeros_del_usuario():
    """Pide al usuario que ingrese números y los valida."""
    while True:
        entrada = input("➡️ Ingresa tus números separados por espacios (ej: 3.14 -2.5 100): ")
        try:
            # Intenta convertir cada elemento ingresado en un número flotante.
            numeros = [float(n) for n in entrada.split()]
            if not numeros: # Si la lista está vacía
                print("❌ Error: No ingresaste ningún número. Inténtalo de nuevo.")
                continue
            return numeros
        except ValueError:
            # Si la conversión falla, es porque hay un valor no numérico.
            print("❌ Error: Asegúrate de ingresar solo números separados por espacios.")

def cuantizar_paso_a_paso(lista_numeros, tipo):
    """
    Función interactiva que guía al usuario a través de la cuantización
    simétrica o asimétrica, explicando cada cálculo.
    """
    if tipo == 'simetrico':
        print("\n" + "="*60)
        print("🔵 TUTORIAL: CUANTIZACIÓN SIMÉTRICA (a int8)")
        print("="*60)
        print("Este método centra el mapa en el cero. Ideal para datos balanceados.")
        
        pausar_y_continuar("Presiona Enter para encontrar el rango...")
        
        # --- PASO 1: CALCULAR RANGO ---
        max_absoluto = max(abs(n) for n in lista_numeros)
        print(f"PASO 1: Encontrar el valor más lejano del cero (máximo absoluto).")
        print(f"   - El valor más lejano es: {max_absoluto:.4f}")
        print(f"   - Por lo tanto, nuestro 'mapa' irá de {-max_absoluto:.4f} a +{max_absoluto:.4f}")
        
        pausar_y_continuar("Presiona Enter para calcular la Escala...")

        # --- PASO 2: CALCULAR ESCALA ---
        escala = max_absoluto / 127 if max_absoluto > 0 else 1
        print(f"PASO 2: Calcular la Escala (S).")
        print(f"   - Dividimos el rango real ({max_absoluto:.4f}) entre el rango de enteros (127).")
        print(f"   - Fórmula: S = max_absoluto / 127")
        print(f"   - ✅ Escala (S) = {escala:.6f}")
        
        # En la simétrica, el punto cero es siempre 0.
        punto_cero = 0
        print(f"\n   - En la cuantización simétrica, el Punto Cero (Z) siempre es 0.")
        
        pausar_y_continuar("Presiona Enter para ver la tabla de resultados finales...")

    else: # tipo == 'asimetrico'
        print("\n" + "="*60)
        print("🟢 TUTORIAL: CUANTIZACIÓN ASIMÉTRICA (a uint8)")
        print("="*60)
        print("Este método crea un mapa a medida para el rango exacto de tus datos.")
        
        pausar_y_continuar("Presiona Enter para encontrar el rango...")

        # --- PASO 1: CALCULAR RANGO ---
        min_real = min(lista_numeros)
        max_real = max(lista_numeros)
        print(f"PASO 1: Encontrar el valor mínimo y máximo exacto.")
        print(f"   - Mínimo real: {min_real:.4f}")
        print(f"   - Máximo real: {max_real:.4f}")

        pausar_y_continuar("Presiona Enter para calcular la Escala...")

        # --- PASO 2: CALCULAR ESCALA ---
        rango_real = max_real - min_real
        escala = rango_real / 255 if rango_real != 0 else 1
        print(f"PASO 2: Calcular la Escala (S).")
        print(f"   - Dividimos el tamaño del rango real ({rango_real:.4f}) entre el de enteros (255).")
        print(f"   - Fórmula: S = (max_real - min_real) / 255")
        print(f"   - ✅ Escala (S) = {escala:.6f}")

        pausar_y_continuar("Presiona Enter para calcular el Punto Cero...")

        # --- PASO 3: CALCULAR PUNTO CERO ---
        punto_cero = round(0 - min_real / escala) if escala != 0 else 0
        print(f"PASO 3: Calcular el Punto Cero (Z).")
        print(f"   - Este valor nos dice a qué entero corresponde el 0.0 del mundo real.")
        print(f"   - Fórmula: Z = round(0 - min_real / S)")
        print(f"   - ✅ Punto Cero (Z) = {punto_cero}")

        pausar_y_continuar("Presiona Enter para ver la tabla de resultados finales...")

    # --- PASO FINAL: MOSTRAR RESULTADOS ---
    print("PASO FINAL: Aplicar las fórmulas a cada número y mostrar los resultados.")
    _imprimir_tabla_resultados(lista_numeros, escala, punto_cero, tipo)


def _imprimir_tabla_resultados(lista_numeros, escala, punto_cero, tipo):
    """Función auxiliar para no repetir el código de la tabla de resultados."""
    print(f"\n{'Original':>12} → {'Cuantizado':>12} → {'Recuperado':>12} | {'Error':>10}")
    print("-"*60)
    
    errores = []
    q_min, q_max = (-127, 127) if tipo == 'simetrico' else (0, 255)

    for num in lista_numeros:
        q = round(num / escala) + punto_cero
        q = max(q_min, min(q_max, int(q)))
        recuperado = (q - punto_cero) * escala
        error = abs(num - recuperado)
        errores.append(error)
        print(f"{num:>12.4f} → {q:>12} → {recuperado:>12.4f} | {error:>10.6f}")
    
    print("-"*60)
    print(f"{'Error promedio:':>47} | {sum(errores)/len(errores):>10.6f}")
    
    print(f"\n✅ Resumen de ahorro:")
    print(f"   • Memoria original (float32): {len(lista_numeros) * 4} bytes")
    print(f"   • Memoria cuantizada (int8):   {len(lista_numeros)} bytes")
    print(f"   • Ahorro de memoria: 75%")

# ========== BUCLE PRINCIPAL INTERACTIVO ==========
if __name__ == "__main__":
    while True:
        print("\n" + "#"*60)
        print("###   TUTORIAL INTERACTIVO DE CUANTIZACIÓN DE NÚMEROS   ###")
        print("#"*60)
        
        numeros = obtener_numeros_del_usuario()
        
        while True:
            print("\n¿Qué tipo de cuantización quieres ver paso a paso?")
            print("  1. Simétrica (ideal para datos centrados en cero)")
            print("  2. Asimétrica (se adapta a cualquier rango de datos)")
            print("  3. Ambas (para comparar)")
            opcion = input("Elige una opción (1, 2, o 3): ").strip()

            if opcion in ['1', '2', '3']:
                break
            else:
                print("❌ Opción no válida. Por favor, elige 1, 2, o 3.")
        
        if opcion == '1':
            cuantizar_paso_a_paso(numeros, 'simetrico')
        elif opcion == '2':
            cuantizar_paso_a_paso(numeros, 'asimetrico')
        elif opcion == '3':
            cuantizar_paso_a_paso(numeros, 'simetrico')
            cuantizar_paso_a_paso(numeros, 'asimetrico')

        # Preguntar si quiere volver a empezar
        while True:
            repetir = input("\n¿Quieres probar con otros números? (s/n): ").lower().strip()
            if repetir in ['s', 'n']:
                break
            else:
                print("❌ Opción no válida. Por favor, ingresa 's' para sí o 'n' para no.")
        
        if repetir == 'n':
            print("\n¡Hasta la próxima!")
            break