# Mathekalender Klasse 10+ 2022

## Aufgabe 1
mit Blatt Papier gelöst

## Aufgabe 2
Brute force durchprobiert in python:
```
a=10, b=15, c=40, d=80
a=10, b=20, c=40, d=75
a=10, b=25, c=40, d=70
a=10, b=30, c=40, d=65
a=10, b=35, c=40, d=60
```
Es gibt 5 Möglichkeiten

## Aufgabe 3
Erste Teilaufgabe  
Wahrscheinlichkeiten:
```
1* 1/2 * 2/3 * ... * 11/12 = 1/12
```
Zweite Teilaufgabe  
Wahrscheinlichkeiten: 
```
1+1/2+...+1/12 =  3.1 ~ 3
```
## Aufgabe 4
[Beweis](4/beweis.md) 

## Aufgabe 5
Eine Lösung mit sieben Vergleichen ist: 
0-1,1-2,2-0, 3-4,4-5,5-3, 6-7 die Reihenfolge ist egal und wird durch den folgenden Graph ausgedrückt:
![Lösung](5/result.png)
[Programm zum Berechnen der Strategie ](5/bf.py) und zum Nachweis, dass es keine Lösung mit 5 Vergleichen gibt.
[Beschreibung Algorithmus](5/description.md)
### Erklärung zur Lösung

In den Dreierklicken kann maximal eine rote Lampe vorhanden sein, in der zweierklicke ebenfalls. Bei 4 roten Lampen ist mindestens eine dieser Bedingungen verletzt.

## Aufgabe 6
[Programm](6/run.py)
