# Aineopintojen harjoitustyö: Algoritmit ja tekoäly

## Dokumentaatio

- [Määrittelydokumentti](dokumentaatio/maarittelydokumentti.md)
- [Toteutusdokumentti](dokumentaatio/toteutusdokumentti.md)
- [Testausdokumentti](dokumentaatio/testausdokumentti.md)

- [Viikkoraportti 1](dokumentaatio/viikkoraportti_1.md)
- [Viikkoraportti 2](dokumentaatio/viikkoraportti_2.md)
- [Viikkoraportti 3](dokumentaatio/viikkoraportti_3.md)
- [Viikkoraportti 4](dokumentaatio/viikkoraportti_4.md)
- [Viikkoraportti 5](dokumentaatio/viikkoraportti_5.md)
- [Viikkoraportti 6](dokumentaatio/viikkoraportti_6.md)

## Käyttöohje

Ohjelman käyttö vaatii pythonista vähintään version 3.10 ja poetrystä vähintään version 2.0.

1. Kopioi ohjelma etärepositoriosta itsellesi.

2. Asenna riippuvuudet:

```bash
poetry install
```

3. Käynnistä virtuaaliympäristö:

```bash
eval $(poetry env activate)
```

4. Käynnistä ohjelma

```bash
python3 src/analyser.py
```

## Testit

Testit voit ajaa virtuaaliympäristössä käskyllä:

```bash
pytest src
```

## Testikattavuus

Testikattavuuden saat näkyviin komennoilla:

```bash
coverage run --branch -m pytest src
coverage report -m
```

Voit myös pyytää testikattavuuden html-raporttina:

```bash
coverage html
```

## Lopetus

Virtuaaliympäristöstä pääset ulos kirjoittamalla:

```bash
deactivate
```

