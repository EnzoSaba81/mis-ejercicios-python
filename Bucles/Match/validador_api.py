status_code = int(input("Ingresa el código de estado de la API (ej: 200, 404, 500): "))

match status_code:
    case 200:
        print("✅ Todo OK. Los datos llegaron perfecto.")
    case 404:
        print("❌ Error: No encontré lo que buscabas (Página no existe).")
    case 500:
        print("🔥 Error crítico: El servidor de la empresa explotó.")
    case _:
        print("❓ Código desconocido. Habrá que llamar al Senior.")
