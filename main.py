import openai

# Ustaw swój klucz API
openai.api_key = "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"

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

# Przykład użycia
if __name__ == "__main__":
    # Ścieżka do pliku z artykułem
    nazwa_pliku_wejsciowego = "artykul"
    
    # Wczytanie treści artykułu z pliku
    tresc_artykulu = wczytaj_plik_tekstowy(nazwa_pliku_wejsciowego)
    if tresc_artykulu.startswith("Błąd"):
        print(tresc_artykulu)
    else:
        # Wygenerowanie kodu HTML za pomocą OpenAI
        tresc_html = generuj_html_dla_artykulu(tresc_artykulu)
        
        # Zapisanie wygenerowanego kodu HTML do pliku
        zapisz_do_html(tresc_html)
