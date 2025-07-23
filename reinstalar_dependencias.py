import subprocess
import sys

# Lista de paquetes críticos
packages = [
    "lightfm",
    "cython",
    "numpy",
    "scipy",
    "pandas",
    "matplotlib",
    "seaborn",
    "scikit-learn",
    "ipykernel",
    "prophet"
]

def reinstall(package):
    print(f"Reinstalando {package} ...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--force-reinstall", package])

if __name__ == "__main__":
    for pkg in packages:
        reinstall(pkg)
    print("¡Reinstalación completa! Reinicia VS Code y prueba tu notebook.")