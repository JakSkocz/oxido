import openai
import os

# Pobierz klucz API z systemu
openai.api_key = os.getenv("OPENAI_API_KEY")

def generuj_html_dla_artykulu(tresc_artykulu):
    prompt = f"""
    Przetwórz poniższy artykuł do struktury HTML zgodnie z następującymi wytycznymi:
    - Użyj odpowiednich tagów HTML, takich jak <h1>, <h2>, <p>, aby strukturyzować treść.
    - Zaznacz miejsca, gdzie warto wstawić grafikę, używając tagu <img> z atrybutem src="image_placeholder.jpg".
    - Każdy <img> powinien zawierać atrybut alt z dokładnym promptem do generowania grafiki.
    - Umieść podpis pod każdą grafiką, używając odpowiedniego tagu HTML (np. <figcaption>).
    - Kod powinien zawierać wyłącznie zawartość do wstawienia między <body> i </body>.
    - Nie dodawaj znaczników <html>, <head>, ani <body>.

    Oto treść artykułu do przetworzenia:
    {tresc_artykulu}
    """

    try:
        odpowiedz = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500,
            temperature=0.7
        )
        # Zwrócenie tylko treści HTML z odpowiedzi
        return odpowiedz.choices[0].message['content'].strip()
    except Exception as e:
        return f"Błąd: {e}"

def wczytaj_plik_tekstowy(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
            return plik.read()
    except Exception as e:
        return f"Błąd podczas odczytu pliku: {e}"

def zapisz_do_html(tresc_html, nazwa_pliku="artykul.html"):
    try:
        with open(nazwa_pliku, 'w', encoding='utf-8') as plik:
            plik.write(tresc_html)
        print(f"Zapisano wygenerowany kod HTML do pliku {nazwa_pliku}")
    except Exception as e:
        print(f"Błąd podczas zapisu pliku HTML: {e}")


# Funkcja do tworzenia szablonu:

def zapisz_szablon():
    szablon_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Podgląd artykułu</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f8f9fa;
        }
        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        h1, h2, h3 {
            color: #333;
        }
        p {
            color: #555;
        }
        img {
            display: block;
            max-width: 100%;
            margin: 20px 0;
        }
        figcaption {
            font-size: 0.9em;
            color: #777;
            text-align: center;
        }
    </style>
</head>
<body>
    <!-- Sekcja gotowa na wklejenie artykułu -->
</body>
</html>
"""
    with open("szablon.html", "w", encoding="utf-8") as f:
        f.write(szablon_html)


# Funkcja do tworzenia zapisu podglądu:

def zapisz_podglad(artykul_html):
    podglad_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Podgląd artykułu</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f8f9fa;
        }}
        .container {{
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}
        h1, h2, h3 {{
            color: #333;
        }}
        p {{
            color: #555;
        }}
        img {{
            display: block;
            max-width: 100%;
            margin: 20px 0;
        }}
        figcaption {{
            font-size: 0.9em;
            color: #777;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="container">
        {artykul_html}
    </div>
</body>
</html>
"""
    with open("podglad.html", "w", encoding="utf-8") as f:
        f.write(podglad_html)


if __name__ == "__main__":
    # Ścieżka do pliku z artykułem
    nazwa_pliku_wejsciowego = "artykul"
    
    # Wczytanie treści artykułu z pliku
    tresc_artykulu = wczytaj_plik_tekstowy(nazwa_pliku_wejsciowego)

    if tresc_artykulu.startswith("Błąd"):
        print(tresc_artykulu)
    else:
        # Wygenerowanie kodu HTML za pomocą OpenAI
        artykul_html = generuj_html_dla_artykulu(tresc_artykulu)
        
        # Zapisanie wygenerowanego kodu HTML do pliku
        zapisz_do_html(artykul_html)
    
    zapisz_szablon()
    zapisz_podglad(artykul_html)
