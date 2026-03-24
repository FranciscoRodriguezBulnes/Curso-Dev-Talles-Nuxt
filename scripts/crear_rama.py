import subprocess
import datetime
import sys

# Tipos de rama permitidos
TIPOS = ["feature", "fix", "hotfix", "release"]

def main():
    print("Tipos de rama disponibles:")
    for t in TIPOS:
        print(f" - {t}")

    tipo = input("Elige el tipo de rama: ").strip().lower()
    if tipo not in TIPOS:
        print("❌ Tipo no válido.")
        sys.exit(1)

    descripcion = input("Descripción de la rama (sin espacios): ").strip().lower()
    descripcion = descripcion.replace(" ", "-")

    fecha = datetime.datetime.now().strftime("%Y-%m-%d")
    nombre_rama = f"{tipo}/{fecha}-{descripcion}"

    print(f"\nCreando rama: {nombre_rama}")

    # Ejecutar git checkout -b
    subprocess.run(["git", "checkout", "-b", nombre_rama])

if __name__ == "__main__":
    main()
