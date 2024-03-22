PySort
===

<img align="left" height="28" src="https://european-union.europa.eu/sites/default/files/styles/oe_theme_small_no_crop/public/2022-02/Flag_of_Germany.png?itok=phTw6mGR"/>

[German/Deutsch]

PySort ist ein [Python](https://python.org) Projekt der Fachinformatiker für Anwendungsentwicklung FI21-1 des [SBSZ - Hermsdorf](https://sbsz-hsp.de/schulteil-hermsdorf).

Das Ziel des Projekts ist eine Visualisierung verschiedener Sortierverfahren, darunter Bubblesort, Minsort, Insertionsort und Shellsort.

Als GUI Framework wird [kivy](https://kivy.org/) genutzt.

Kivy Python Unstützung

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/kivy)

Projektumfeld
----------------------------------------

Das Projekt wurde in der folgenden Umgebung erstellt und getestet.

- Python 3.11.6
- Kivy 2.3.0
- PyInstaller 6.5.0

Betriebssysteme als Produktions- und Testumgebungen.

- Windows 10
- Kubuntu 23.10

Benutzung
----------------------------------------

Die Abhängigkeiten des Projektes befinden sich in der `requirements.txt` in `./kivysort`.

Es wird empfohlen eine virtuelle Umgebung mit [venv](https://docs.python.org/3/library/venv.html) einzurichten und die Abhängikeiten mit [pip](https://pip.pypa.io/en/stable/) zu installieren.

Die Applikation kann über die `main.pyw` in `./kivysort` gestartet werden.

Das `.pyw` Format verhindert das erscheinen eines Konsolenfensters.

Installation
----------------------------------------

PySort kann für Windows 8/10/11 mit [PyInstaller](https://pyinstaller.org/en/stable/) als Anwendung `.exe` gebaut werden.
Dafür liegt ein automatisiertes Bauskript bei: `windows_builder.py`

Der Programmordner befindet sich nach dem Bau in dem Verzeichnis `dist`. Mehr Informationen gibt es auf der [Kivi wiki](https://kivy.org/doc/stable/guide/packaging-windows.html).

Einbindung Sortierverfahren
----------------------------------------

Sortierverfahren können als Module unter `./kivysort/sorting` eingebunden werden, dazu müssen folgende Kriterien erfüllt werden

- Modulname: `{sortiername}_sort.py`
- Klassenname: `class {Sortiername}sort(Sort):`
- Import: `from src.sorting.sort import Sort`
- Attribut in Konstruktor: `self.sort_name = {Sortiername}`
- Zuweisung vor der Sortierung: `i_list = self.numbers`
- Zuweisung nach Sortierung: `self.sorted_numbers = i_list`
- Verständnis zu Vergleichs- und Tauschschritten
- Übergabe der Indexes mit Aktionstyp in `self.schedule_event(typ, index_1, index_2)`

`sort_handler.py` findet Sortiermodule automatisch, solange diese Kriterien erfüllt sind.

### Beispiel bubble_sort.py

```py
"""Bubblesort module."""

from src.sorting.sort import Sort


class Bubblesort(Sort):
    """Bubblesort class."""
    # pylint: disable=all
    def __init__(self, **kwargs):
        super(Bubblesort, self).__init__(**kwargs)
        self.sort_name = 'Bubblesort'

    def sort(self) -> None:
        """Bubblesort algorithm."""
        i_list = self.numbers
        length = len(i_list)
        for i in range(length-1):
            for j in range(length-1-i):
                self.schedule_event("compare", j, j+1)
                if i_list[j] > i_list[j+1]:
                    tmp = i_list[j]
                    i_list[j] = i_list[j+1]
                    i_list[j+1] = tmp
                    self.schedule_event("switch", j, j+1)
        self.sorted_numbers = i_list
```

## Projektteam

Das Projektteam von PySort.

- [Dustopheles](https://github.com/Dustopheles)
- [dnzkrkmz](https://github.com/dnzkrkmz)
- [realAnzary](https://github.com/realAnzary)

### Mitwirkende

Dieses Projekt existiert außerdem in diesem Zustand dank [all den Leuten, die daran mitgearbeitet haben](https://github.com/Dustopheles/PySort/graphs/contributors).
