import patoolib
from pathlib import Path
from sys import argv
from lib_sistemas import validar_num_args
def verificar_archivos(ruta_dict: Path, ruta_rar: Path) -> bool:
    return ruta_dict.exists() and ruta_rar.exists()

def descomprimir_archivo(diccionario: Path, archivo: Path):
    with open(diccionario, "r") as f:
        for linea in f.read().splitlines():
            try:
                patoolib.extract_archive(str(archivo), outdir='destino', password=linea)
            except Exception:
                pass
            else:
                return True
def main():
    if validar_num_args(2, "[RUTA_DICCIONARIO] [RUTA_ARCHIVO]"):
        ruta_dict = Path(argv[1])
        ruta_archivo = Path(argv[2])
        if verificar_archivos(ruta_dict,ruta_archivo):
            descomprimir_archivo(ruta_dict,ruta_archivo)
        else:
            print("Alguna de las rutas no existe")
if __name__ == "__main__":
    main()




