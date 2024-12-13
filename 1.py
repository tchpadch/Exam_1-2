import pefile

def analyze_pe(file):
    try:
        pe = pefile.PE(file)
        if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
            print(f"Импортированные библиотеки и функции в файле {file}:\n")
            for entry in pe.DIRECTORY_ENTRY_IMPORT:
                print(f"Библиотека: {entry.dll.decode('utf-8')}")
                for imp in entry.imports:
                    print(f"  Функция: {imp.name.decode('utf-8') if imp.name else 'Неизвестно'}")
                print()
        else:
            print(f"Импортированные библиотеки не найдены в файле {file}.")
    except FileNotFoundError:
        print(f"Файл {file} не найден.")
    except pefile.PEFormatError:
        print(f"Файл {file} не является PE-файлом.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

file_path = "C:\\Program Files (x86)\\Roblox\\Versions\\version-1088f3c8e4a44cc7\\RobloxPlayerBeta.exe"
analyze_pe(file_path)

