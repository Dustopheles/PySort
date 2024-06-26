PySort
===

<img align="left" height="28" src="https://european-union.europa.eu/sites/default/files/styles/oe_theme_small_no_crop/public/2022-02/Flag_of_Germany.png?itok=phTw6mGR"/>

[German/Deutsch]

PySort ist ein [Python](https://python.org) Projekt der Fachinformatiker für Anwendungsentwicklung FI21-1 des [SBSZ - Hermsdorf](https://sbsz-hsp.de/schulteil-hermsdorf).

Das Ziel des Projekts ist eine Visualisierung verschiedener Sortierverfahren, darunter Bubblesort, Minsort, Insertionsort und Shellsort.

Als GUI Framework wird [kivy](https://kivy.org/) genutzt.

Projektumfeld
----------------------------------------

Das Projekt wurde in der folgenden Umgebung erstellt und getestet.

- Python 3.11.6
- Kivy 2.3.0
- PyInstaller 6.5.0

Betriebssysteme als Produktions- und Testumgebungen.

- Windows 10
- Kubuntu [22.04, 23.10]

Benutzung
----------------------------------------

Abhängigkeiten des Projektes befinden sich in der `requirements.txt`

Es wird empfohlen eine virtuelle Python Umgebung mit [venv](https://docs.python.org/3/library/venv.html) einzurichten.

```
python -m venv env
```

und die Abhängikeiten mit [pip](https://pip.pypa.io/en/stable/) aus der `requirements.txt` zu installieren.

```
pip install -r requirements.txt
```

Die Applikation kann über die `main.pyw` in dem Programmverzeichnis `pysort` gestartet werden.

Das `.pyw` Format verhindert das erscheinen eines Konsolenfensters unter Windows.

### Balkendiagramm

[SortExample.webm](https://github.com/Dustopheles/PySort/assets/128293762/7b5e5b21-d9f3-42f7-9120-cc50849bb29b)

Installation
----------------------------------------

PySort kann für Windows 8/10/11 mit [PyInstaller](https://pyinstaller.org/en/stable/) aus dem Projekt eine Anwendung bauen.
Dafür liegt ein automatisiertes Bauskript bei: `windows_builder.py`

PyInstaller empfielt das Programm nicht im Debug Modus zu bauen, ist jedoch mit erhöhten Zeitaufwand möglich.

Um das Projekt mit PyInstaller bauen zu können, werden alle Abhängigkeiten aus `requirements-builder.txt` benötigt.

```
pip install -r requirements-builder.txt
```

Der Programmordner befindet sich nach dem Bau in dem Verzeichnis `dist`. Mehr Informationen gibt es auf der [Kivi wiki](https://kivy.org/doc/stable/guide/packaging-windows.html).

Einbindung Sortierverfahren
----------------------------------------

Sortierverfahren können als Module unter `./pysort/sorting` eingebunden werden, dazu müssen folgende Kriterien erfüllt werden

- Modulname: `{sortiername}_sort.py`
- Klassenname: `class {Sortiername}sort(Sort):`
- Import: `from src.sorting.sort import Sort`
- Attribut in Konstruktor: `self.name = {Sortiername}`
- Zu sortierende Liste: `numbers` aus Übergabeparametern
- Verständnis zu Vergleichs- und Tauschschritten des Sortierverfahrens
- Übergabe des Indexe-Paars mit Aktionstyp in `self.schedule_event(Typ, Index a, Index b)`
- Rückgabe der sortierten Zahlen: `numbers`

`sort_handler.py` findet Sortiermodule automatisch, solange diese Kriterien erfüllt sind.

### Beispiel bubble_sort.py

```py
from src.sorting.sort import Sort


class Bubblesort(Sort):
    """Bubblesort class."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'Bubblesort'

    def sort(self, numbers: list) -> list:
        """Bubblesort algorithm."""
        length = len(numbers)
        for i in range(length-1):
            for j in range(length-1-i):
                self.schedule_event("compare", j, j+1)
                if numbers[j] > numbers[j+1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                    self.schedule_event("switch", j, j+1)
        return numbers
```

## Projektteam

Das Projektteam von PySort.

- [Dustopheles](https://github.com/Dustopheles)
- [dnzkrkmz](https://github.com/dnzkrkmz)
- [realAnzary](https://github.com/realAnzary)
