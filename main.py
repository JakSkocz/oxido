import openai

openai.api_key = "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"

def generuj_odpowiedz(zapytanie):
    try:
        odpowiedz = openai.ChatCompletion.create(
            model="gpt-4o-mini",   # Model chatowy
            messages=[
                {"role": "user", "content": zapytanie}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return odpowiedz.choices[0].message['content'].strip()
    except Exception as e:
        return f"Błąd: {e}"
    
if __name__ == "__main__":
    zapytanie = input("Wpisz swoje zapytanie: ")
    odpowiedz = generuj_odpowiedz(zapytanie)
    print("Odpowiedź od modelu:")
    print(odpowiedz)