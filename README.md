# 3140 Gruppeoppgave
Gruppeoppgave for å lage en dansende robot-arm
av Eirik, Elias og Dennis

Dette programmet krever i tillegg til ROS følgende pakker:
Librosa:
*install på linux med*
``` markdown
**pip install librosa**
```
*eller på conda med*
``` markdown
**conda install -c conda-forge librosa**
```
Pyglet:
*Install på linux med*
``` markdown
 **pip install pyglet**
 ```
*eller på conda med*
``` markdown
 **conda install -c conda-forge pyglet**
```
BeatPlanner
------
Denne filen tar inn en musikkfil som kjøres gjennom Librosa for å få ut hvilke
tidspunkter i filen det finnes en *beat*. Den publiserer dette til **Point-to-point**.
Videre publiserer den også til **Player** for å starte musikk.

Player
------
Player spiller musikk, og starter ikke å spille musikk før den får ok signal fra
**Point-to-point**, den publiserer også til **xx** for å synkronisere musikken til bevegelsen.
