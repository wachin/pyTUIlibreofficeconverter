import curses
import subprocess
import os

def convert_all_files():
    """Convierte todos los archivos .docx a .odt en el directorio actual usando LibreOffice en modo headless."""
    docx_files = [f for f in os.listdir('.') if f.endswith('.docx')]
    results = []

    for docx_file in docx_files:
        command = f'libreoffice --headless --convert-to odt "{docx_file}"'
        try:
            subprocess.run(command, shell=True, check=True)
            results.append(f"Convertido: {docx_file}")
        except subprocess.CalledProcessError as e:
            results.append(f"Error al convertir {docx_file}: {e}")

    return results

def main(stdscr):
    curses.curs_set(0)  # Oculta el cursor
    stdscr.clear()

    # Título
    stdscr.addstr(0, 0, "Conversor de .docx a .odt", curses.A_BOLD)
    stdscr.addstr(1, 0, "Presione cualquier tecla para convertir todos los archivos .docx a .odt.", curses.A_UNDERLINE)

    stdscr.refresh()
    stdscr.getch()  # Esperar una tecla

    # Convertir todos los archivos
    results = convert_all_files()

    # Mostrar resultados
    stdscr.clear()
    stdscr.addstr(0, 0, "Resultados de la conversión:", curses.A_BOLD)
    for i, result in enumerate(results):
        stdscr.addstr(i + 1, 0, result)

    stdscr.addstr(len(results) + 2, 0, "Presione cualquier tecla para salir.")
    stdscr.refresh()
    stdscr.getch()  # Esperar una tecla para salir

if __name__ == "__main__":
    curses.wrapper(main)
