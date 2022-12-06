
# Beschreibung des Algorithmus 

## Vorbemerkung
Die 8 Lampen werden durch 8 Knoten eines Graphen dargestellt.
Eine Strategie mit n Schritten wird dadurch bestimmt, dass n Paare von Knoten verbunden werden (Bmerkung: Strategien sind kommutativ, die Reihenfolge spielt keine Rolle, wichtig ist das nach dem n-ten Schrit etwas leuchtet und das ist von der Reihenfolge unabhängig)
Eine Belegung ordnet jedem Knoten entweder die Farbe rot oder die Farbe grün zu.
-> Eine Strategie funktioniert nicht, wenn es eine Belegung der 8 Knoten gibt, in der keine der Verbindungen zwei rote Knoten miteinander verbindet.

## Algorithmus zum Bestimmen einer Lösung mit n Schritten
Erzeuge eine Liste aller möglichen Adjazenzmatrizen mit n Kanten.
Erzeuge eine 8 * m Matrix mit allen m möglichen Belegungen, jede Spalte gibt eine Belegung an, 0 steht für grün, 1 für rot.
Beispiel:
```
... 1 ...
... 1 ...
... 1 ...
... 1 ...
... 0 ...
... 0 ...
... 0 ...
... 0 ...
````
steht für die Belegung rot,rot,rot,rot, grün,grün,grün,grün.

Die Matrix aller Belegung wird mit d bezeichnet.

Wir berechnen jetzt für alle `A` die Matrix `B = A * D`.
Für jede Ausgangsbelegung d (=Spalte von D) erhalten wir eine korrespondierende Spalte b von B. Die Testmaschine
spricht an, wenn ein Feld sowohl in d als auch b gesetzt ist.

Beispiel:
```
      1        1
      1        0
      1        0
d =   1     b= 0
      0        0
      0        1
      0        0
      0        0
```
würde bedeuten, dass die Lampe 1  mit einem der Knoten 1,2,3,4 verbunden sein muss (d.h. die Strategie sagt, dass man Lampe 1 und eine von den Lampen 1,2,3 oder 4 in die Testmaschine legt) und deshalb die Testmaschine anschlägt.
Diese Fälle erhält man dadurch, dass man D und B 'punktweise' miteinander multipliziert: `D mul B`.

## Schritte
Für alle `A` berechne `A*D=B` und bilde das punktweise Produkt mit A: `(A*D) mul A`.
Für alle Spalten des Ergebnisses bestimme die Summe (oder das Maximum) d.h. wir haben jetzt für jede Spalte eine Zahl, die entweder 0 ist und bedeutet, dass es eine Belegung gibt in der nichts leuchtet oder eine zahl grösser 0 (minimum über die Summen muss 0 sein)

Wenn für alle Spalten gilt, dass etwas leuchtet haben wir eine Strategie gefunden (egal wie die Belegung ist, nach dem n-ten Schritt leuchtet etwas für alle Belegungen)

Programmsnippet für den Algorithmus:

```
# für alle Adjazenzmatrizen mit n Verbindungen führe folgendes aus, d ist die matrix aller Belegungen
r = a.matmul(d)
lights_on = r.mul(d)
column_sums= torch.sum(lights_on,dim=0)
min_column = torch.min(column_sums)
if(min_column.numpy()!=0):
    print(f"the following matrix defines a strategy for {n}: \n{a}")
```


