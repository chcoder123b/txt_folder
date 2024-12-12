import os

def generate_directory_structure(path, output_file):
    # Funktion zum Durchlaufen der Ordnerstruktur und Erzeugen der Ausgabe
    def traverse_directory(dir_path, indent, output_file):
        for entry in os.scandir(dir_path):
            if entry.is_dir():
                # Wenn es ein Verzeichnis ist, füge es hinzu
                output_file.write(f"{indent}├── Ordner {entry.name}\n")
                # Rekursiv den Inhalt des Verzeichnisses auflisten
                traverse_directory(entry.path, indent + "│   ", output_file)
            else:
                # Wenn es eine Datei ist, füge die Datei hinzu
                output_file.write(f"{indent}├── {entry.name}\n")

    # Öffnen der Ausgabedatei im Schreibmodus mit UTF-8 Encoding
    with open(output_file, 'w', encoding='utf-8') as f:
        # Beginne die Struktur vom angegebenen Pfad aus
        traverse_directory(path, "", f)

def remove_first_line(output_file):
    # Lese den Inhalt der Datei und entferne die erste Zeile
    with open(output_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Entferne die erste Zeile
    lines = lines[1:]

    # Schreibe den modifizierten Inhalt wieder in die Datei
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)

if __name__ == "__main__":
    # verwende Raw String oder doppelte Backslashes
    folder_path = r"???"  # Hier den gewünschten Ordnerpfad angeben
    
    # Der Name der Ausgabedatei basiert auf dem Ordnernamen und wird im selben Ordner gespeichert
    output_txt_file = os.path.join(folder_path, os.path.basename(folder_path) + "_struktur.txt")
    
    # Aufruf der Funktion zum Erzeugen der Ordnerstruktur
    generate_directory_structure(folder_path, output_txt_file)
    # Entferne die erste Zeile (erstellte txt-Datei aus der Liste)
    remove_first_line(output_txt_file)
    print(f"Die Ordnerstruktur wurde in {output_txt_file} gespeichert.")