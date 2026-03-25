from sys import argv,exit
from os import name as OS,path

def validar_num_args(min:int, uso:str, max:int | None = None) -> bool:
    """Valida la cantidad de argumentos pasados por línea de comandos.En caso contrario, muestra un mensaje de error
        indicando el uso correcto del programa según el sistema operativo.

        Args:
            min (int): Número mínimo de argumentos permitidos.
            uso (str): Cadena que describe el uso correcto del script
            max (int | None, optional): Número máximo de argumentos permitidos.
                Si es None, se asume que el máximo es igual al mínimo. Por defecto
                es None.

        Returns:
            bool: `True` si la cantidad de argumentos está dentro del rango
            permitido, `False` en caso contrario.

        Nota:
            Imprime un mensaje de error en la salida estándar cuando la cantidad
            de argumentos es insuficiente o excede el límite permitido.
    """

    if max is None:
        max = min
    if min <= (len(argv)-1) <= max:
        return True

    elif len(argv) > max:

        if OS == "nt":
            print(f"Límite de argumentos excedido. Uso: python {uso}")
        else:
            print(f"Límite de argumentos excedido. Uso: python3 {uso}")
        return False

    elif (len(argv)-1) < min:

        if OS == "nt":
            print(f"Argumentos insuficientes. Uso: python {uso}")
        else:
            print(f"Argumentos insuficientes. Uso: python3 {uso}")
        return False

def convertir_a_entero(texto:str | list[str], msg_error:str ) -> int | list[int]:
    """Convierte una cadena o una lista de cadenas a entero(s).

        Si `texto` es una cadena, intenta convertirla a `int`.
        Si `texto` es una lista de cadenas, convierte cada elemento a `int`
        usando `map`.

        En caso de error durante la conversión, se muestra `msg_error`
        y se finaliza la ejecución del programa.

        Args:
            texto (str | list[str]): Cadena o lista de cadenas a convertir.
            msg_error (str): Mensaje que se mostrará si ocurre un error.

        Returns:
            int | list[int]: Un entero si `texto` es una cadena, o una lista
            de enteros si `texto` es una lista.

        Raises:
            SystemExit: Si la conversión falla.
    """
    if isinstance(texto,str):
        try:
            texto = int(texto)
            return texto
        except ValueError:
            print(msg_error)
            exit()
    try:
        texto = list(map(int,texto))
        return texto
    except ValueError:
        print(msg_error)
        exit()

def verificar_archivos(*args:str) -> bool:
    """
    Verifica si todos los archivos especificados existen.

    Recorre cada ruta de archivo pasada como argumento y comprueba si existe.
    Imprime un mensaje indicando si todos los archivos existen o si falta alguno.

    Args:
        *args: Una o más rutas de archivos a verificar (como cadenas).

    Returns:
        bool: `True` si todos los archivos existen, `False` si alguno no existe."""

    if all(path.exists(ruta) for ruta in args):
        print("Todos los archivos existen")
        return True
    else:
            faltantes = [ruta for ruta in args if not path.exists(ruta)]
            print(f"No se encontraron los siguientes archivos: {",".join(faltantes)}. Verifica que estos estén en la misma carpeta donde ejecutas el script")
            return False

def convertir_a_float(texto:str | list[str], msg_error:str ) -> float | list[float]:
    """Convierte una cadena o una lista de cadenas a entero(s).

        Si `texto` es una cadena, intenta convertirla a `float`.
        Si `texto` es una lista de cadenas, convierte cada elemento a `float`
        usando `map`.

        En caso de error durante la conversión, se muestra `msg_error`
        y se finaliza la ejecución del programa.

        Args:
            texto (str | list[str]): Cadena o lista de cadenas a convertir.
            msg_error (str): Mensaje que se mostrará si ocurre un error.

        Returns:
            float | list[float]: Un entero si `texto` es una cadena, o una lista
            de enteros si `texto` es una lista.

        Raises:
            SystemExit: Si la conversión falla.
    """
    if isinstance(texto,str):
        try:
            texto = float(texto)
            return texto
        except ValueError:
            print(msg_error)
            exit()
    try:
        texto = list(map(float,texto))
        return texto
    except ValueError:
        print(msg_error)
        exit()