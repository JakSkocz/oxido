# Opis działania aplikacji:

Tworzą się nowe pliki: 
- artykul.html - sformatowany plik tekstowy artykulu gotowy do wklejenia do szablonu html
- szablon.html - szablon strony html z miejscem zeby wkleić plik artykul.html
- podglad.html - gotowy do podglądu artykuł

# Instrukcja uruchomienia:

W tym projekcie klucz API przechowywany jest jako zmienna środowiskowa na komputerze lokalnym. Więc przed uruchomieniem programu nalezy go ustawić:

W systemie Linux/Mac:
```bash
export OPENAI_API_KEY="twój_klucz_api"
```

W systemie Windows(PowerShell):
```bash
$env:OPENAI_API_KEY="twój_klucz_api" 
```

Teraz, zeby uruchomić aplikację nalezy skompilować plik main.py