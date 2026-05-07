# 🏦 Bankomat Simulator (Python)

Prosta aplikacja konsolowa imitująca działanie bankomatu. Projekt pozwala na zarządzanie stanem konta, który jest trwale zapisywany w zewnętrznym pliku tekstowym.

---

## 🚀 Główne Funkcje
* **Bezpieczeństwo:** Dostęp do konta chroniony 4-cyfrowym kodem PIN.
* **Limit prób:** System blokuje dostęp po 3 nieudanych próbach logowania.
* **Zarządzanie środkami:** * Sprawdzanie aktualnego salda.
    * Wpłacanie pieniędzy na konto.
    * Wypłacanie środków (z automatyczną blokadą przy próbie wypłaty kwoty większej niż stan konta).
* **Trwałość danych:** Każda operacja finansowa aktualizuje plik `stan.txt`, dzięki czemu stan konta nie resetuje się po wyłączeniu programu.

## 🛠️ Technologie i Mechanizmy
* **Język:** Python 3.x
* **Biblioteka `os`:** Wykorzystana do czyszczenia konsoli (`os.system("cls")`), co poprawia czytelność interfejsu.
* **Obsługa plików:** Zastosowanie metod `open()`, `read()` i `write()` do komunikacji z bazą danych w formie pliku tekstowego.
* **Global Scope:** Użycie słowa kluczowego `global` do zarządzania stanem konta wewnątrz różnych funkcji.

## 📥 Jak uruchomić projekt?
1. Upewnij się, że w folderze z programem znajduje się plik `stan.txt`.
   * *Wpisz w nim dowolną liczbę (np. 1000) jako początkowy stan konta.*
2. Uruchom skrypt:
   ```bash
   python nazwa_twojego_pliku.py
