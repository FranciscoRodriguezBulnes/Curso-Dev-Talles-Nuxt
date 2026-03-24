import subprocess

def run(cmd):
    return subprocess.check_output(cmd).decode("utf-8").strip()

# 1. Obtener la rama actual
branch = run(["git", "rev-parse", "--abbrev-ref", "HEAD"])

# 2. Añadir todos los cambios
subprocess.run(["git", "add", "."])

# 3. Crear commit usando el nombre de la rama como mensaje
commit_message = f"Update on branch {branch}"
subprocess.run(["git", "commit", "-m", commit_message])

# 4. Hacer push (crea la rama remota si no existe)
subprocess.run(["git", "push", "-u", "origin", branch])

print(f"✔ Cambios subidos a la rama '{branch}' con el commit: {commit_message}")
