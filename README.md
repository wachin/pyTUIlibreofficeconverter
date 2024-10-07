# pyTUIlibreofficeconverter



### Cómo funciona el script

1. **Función convert_all_files**: Esta función busca todos los archivos `.docx` en el directorio actual y los convierte a `.odt` utilizando el comando `libreoffice --headless --convert-to odt`. Los resultados de cada conversión (éxito o error) se almacenan en una lista `results`.
2. **Interfaz con curses**:
   - La función `main` utiliza `curses` para mostrar una interfaz simple.
   - Al iniciar, muestra un mensaje indicando que se presione cualquier tecla para comenzar la conversión.
   - Al presionar una tecla, se llama a `convert_all_files` para convertir todos los archivos.
   - Luego, se muestran los resultados de la conversión y se espera otra tecla para salir.

### Ejecución

Abra una terminal y ponga:

```
python3 LOconverter.py
```

Este script convertirá automáticamente todos los archivos `.docx` a `.odt` en el directorio actual y mostrará los resultados de la conversión.