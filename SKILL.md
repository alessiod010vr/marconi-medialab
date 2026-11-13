---
name: "marconi-media-lab"
description: "Da descrizione e foto di un evento del L.T. Marconi di Verona crea carosello Instagram 4:5, banner sito 2000×700, didascalia IG con hashtag e articolo per il sito."
---

# Marconi Media Lab

Kit della redazione social del **Liceo Tecnologico G. Marconi di Verona** (ex ITI; Instagram @itimarconiverona).
Input tipico: un testo inviato da un docente + alcune foto (+ eventualmente il brand kit / logo).
Output, sempre tutti e quattro salvo richiesta diversa:

1. **Carosello Instagram 4:5** (1080×1350), 3 slide di default (2–6 se richiesto)
2. **Banner sito** 2000×700
3. **Didascalia Instagram** con hashtag
4. **Articolo per il sito** della scuola

## Flusso

1. **Leggi tutto il materiale.** Guarda ogni foto e scegli: foto più forte (relatore/azione) → copertina e banner; foto della slide/locandina dell'evento → slide informativa; foto d'aula/gruppo → collage di chiusura. Estrai dalle foto solo testi leggibili davvero (titoli di slide, nomi di enti).
2. **Niente fatti inventati.** Date, luoghi, nomi, numeri solo dal testo del docente o dalle foto. Se manca un dato essenziale, usa un segnaposto [DATO] e segnalalo.
3. **Logo.** Usa sempre il logo nuovo "L.T. MARCONI verona" (sei tessere colorate + scritta). I loghi "I.T.I." del vecchio brand kit sono superati: non usarli. Se il logo arriva su sfondo nero, rendilo trasparente e crea la versione con testo scuro (script sotto).
4. **Scegli i layout** dal catalogo, variando rispetto all'ultimo post se l'utente lo indica. Dichiara in una riga quali hai usato.
5. **Grafiche** → un canvas del tipo artifact **Design** (un artboard per slide + uno per il banner, banner in una riga sotto le slide, 120 px di distanza). Carica foto e loghi come asset; mai data URI.
6. **Testi** → carica la skill **scrittura-italiana** (`anthropic-skills:scrittura-italiana`) PRIMA di scrivere didascalia e articolo e applicala a entrambi: niente tic da AI (triadi, "non è X ma Y", gerundi a catena, avverbi in -mente, trattini lunghi, frasi fatte tipo "un'esperienza indimenticabile", "toccare con mano" ripetuto). Didascalia e articolo vanno nella risposta in chat, pronti da copiare.
7. Chiudi con una riga sugli assunti (layout scelti, dati mancanti).

## Brand

| Token | Valore | Uso |
|---|---|---|
| Sfondo | `#F6F3EC` | fondo di tutte le grafiche |
| Inchiostro | `#1C1C24` | testi, pill scure |
| Giallo | `#F7B500` | forma decorativa, accento |
| Azzurro | `#1497CC` (testo: `#1078A3`) | forma decorativa, card, occhielli |
| Verde | `#7DB83A` (testo: `#5E9A1F`) | pill, card, parola chiave del titolo |
| Magenta | `#E0075F` | card, accento |
| Bordeaux | `#A62A4A` | card |
| Viola | `#7B3DB8` | card |

Regole:
- **Font**: Montserrat (Google Fonts) 500/600/700/800/900. Titoli 900, letter-spacing negativo (-2/-2.5px), line-height ~1.
- **Forma "tessera"** (dal logo): `border-radius: 24px 130px 130px 0` (scala i valori sulla dimensione). Usala per forme decorative, card e un angolo delle foto.
- **Firma grafica fissa**: sfondo chiaro + forme arrotondate **gialla e azzurra nell'angolo in alto a destra** (parzialmente fuori dal bordo). Sempre presenti, posizione variabile di poco.
- **Vietato**: la "scaletta" colorata del logo come fascia in basso, gradienti, emoji nelle grafiche, testo sopra i volti.
- **Colore con uno scopo**: un solo colore di accento per titolo (di default verde; adattalo al tema: azzurro per tecnologia, magenta per eventi/sport, viola per aeronautica, giallo per informatica, bordeaux per meccatronica/robotica).
- Grassetto solo per termini chiave. Testo minimo 23 px su 1080.
- Margini: 80 px sul carosello, 120 px sul banner. Footer a 56 px dal fondo.
- Contrasto ≥ 4.5:1: su verde e giallo testo scuro (`#14240A` / `#1C1C24`), su azzurro/magenta/viola/bordeaux testo bianco.

## Catalogo layout

Coordinate su 1080×1350. Le forme gialla/azzurra in alto a destra sono implicite in ogni layout.

### Copertine (slide 1)
- **C1 Titolo + foto grande** — pill (data, tema) a y 190; titolo 92 px su 3 righe, ultima parola chiave in accento; foto 920×560 a y 600 con angolo in alto a destra 160 px; footer: logo scuro (h 96) a sinistra, "Scorri →" a destra.
- **C2 Foto a tutta pagina** — foto full-bleed con velo scuro solo nella metà bassa (overlay piatto `rgba(28,28,36,.55)`, non gradiente); titolo bianco 96 px in basso; pill colorate sopra; logo bianco.
- **C3 Foto a tessera** — foto ritagliata dentro una tessera grande (800×800, radius 40/300/300/0) a destra in basso; titolo a sinistra in alto su 4 righe.
- **C4 Numero gigante** — se l'evento ha un dato forte (data, numero partecipanti, edizione): numero 300 px in accento, titolo sotto, foto piccola rotonda-tessera.
- **C5 Split verticale** — metà sinistra colore pieno (accento) con titolo bianco/scuro, metà destra foto; forme in alto a destra sopra la foto.
- **C6 Citazione** — virgolette grandi in accento, frase breve del relatore/docente (solo se presente nel testo), nome sotto, foto piccola.

### Slide interne
- **I1 Testo + foto + 3 card** — occhiello azzurro, titolo 76 px, paragrafo 32 px; foto 920×420 a y 500; griglia di 3 card tessera colorate (titolo 38 px, testo 23 px). Card solo con contenuti reali (punti dell'evento, temi della slide fotografata).
- **I2 Timeline** — 3–4 tappe verticali con pallino colorato e linea; per programmi, giornate, fasi.
- **I3 Due foto + testo** — due foto affiancate (radius tessera specchiati), testo sotto.
- **I4 Grande foto con didascalia** — foto 920×820, box testo sovrapposto in basso a sinistra (sfondo chiaro, radius tessera).
- **I5 Elenco numerato** — 3–5 punti con numeri 64 px in colori diversi del brand.

### Chiusure (ultima slide)
- **F1 Collage** — testo 38 px in alto con parola chiave in accento; griglia 2 colonne (1.35fr/1fr), foto grande a sinistra su 2 righe, due a destra; pill verde con frase finale; logo + "n / n".
- **F2 Ringraziamenti** — "Grazie a…" con enti/persone citati nel testo, logo grande centrato, handle @itimarconiverona.
- **F3 Call to action** — per open day/iscrizioni: domanda grande, pulsante-pill con link (es. sito scuola), foto di sfondo piccola.

In tutte le slide non finali: indicatore "n / n" a destra nel footer; a sinistra logo o la sola fila di tessere (h 52).

### Banner sito 2000×700
- **B1 Testo sinistra / foto destra** — testo in colonna 860 px centrata verticalmente (pill, titolo 88 px, riga con luogo/ente); foto da x 1060 a 1880, y 90–610, angolo in alto a destra 170 px. Niente logo (è già nell'header del sito).
- **B2 Foto piena + box** — foto full-bleed, box chiaro a tessera a sinistra con titolo e pill.
- **B3 Striscia di foto** — tre foto strette affiancate a destra, titolo a sinistra.
Tieni i contenuti importanti nella fascia centrale 1600 px (alcuni temi ritagliano i lati).

## Skeleton di un artboard

```html
<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<title>Copertina</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800;900&amp;display=swap" rel="stylesheet">
<style>body{margin:0}</style>
</helmet>
<div style="width: 1080px; height: 1350px; position: relative; overflow: hidden; background: #F6F3EC; font-family: 'Montserrat', sans-serif; color: #1C1C24">
<div aria-hidden="true" style="position: absolute; top: -90px; right: 150px; width: 260px; height: 260px; background: #F7B500; border-radius: 24px 120px 120px 0"></div>
<div aria-hidden="true" style="position: absolute; top: 70px; right: -70px; width: 280px; height: 280px; background: #1497CC; border-radius: 24px 130px 130px 0"></div>
<!-- contenuti del layout -->
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"accent":{"editor":"color","default":"#5E9A1F"},"$preview":{"width":1080,"height":1350}}'>
class Component extends DCLogic {
renderVals() { return { accent: this.props.accent ?? '#5E9A1F' }; }
}
</script>
</body>
</html>
```
Controlla che titoli e pill non si sovrappongano alle forme in alto a destra (le forme occupano circa x > 670, y < 350).

## Asset inclusi

In `assets/` ci sono i loghi già pronti, da usare se l'utente non ne allega di nuovi:
- `logo_lt_dark.png` — tessere colorate + testo scuro, per lo sfondo chiaro (uso standard)
- `logo_lt_white.png` — tessere colorate + testo bianco, per foto o fondi scuri
- `logo_icons.png` — solo la fila di tessere, per i footer delle slide interne
- `logo_lt_originale_nero.png` — originale su nero

Per rigenerarli da un logo nuovo: `python scripts/logo_trasparente.py logo.png assets/`.

## Logo: da sfondo nero a trasparente

```python
from PIL import Image
import numpy as np
im = Image.open(SRC).convert('RGB'); a = np.asarray(im).astype(float)
m = a.max(axis=2); alpha = np.clip((m-12)/(60-12), 0, 1)
rgb = np.clip(a/np.maximum(alpha[...,None], 1e-3), 0, 255)
o = Image.fromarray(np.dstack([rgb, alpha*255]).astype('uint8'), 'RGBA'); o = o.crop(o.getbbox())
o.save('logo_lt_white.png')
# versione testo scuro: scurisci solo i pixel bianchi SOTTO la fila di tessere
d = np.asarray(o).astype(float); sat = d[...,:3].max(2)-d[...,:3].min(2)
mask = sat < 40; mask[:int(o.height*0.575)] = False   # le icone nelle tessere restano bianche
d[mask,0], d[mask,1], d[mask,2] = 28, 28, 36
Image.fromarray(d.astype('uint8'), 'RGBA').save('logo_lt_dark.png')
o.crop((0, 0, o.width, int(o.height*0.54))).save('logo_icons.png')
```
Controlla il risultato su sfondo chiaro prima di caricarlo.

## Didascalia Instagram

- Prima riga = gancio (titolo del post, max ~60 caratteri), poi 2–4 frasi brevi: cosa, quando, dove, chi; il senso per gli studenti.
- Parti dal testo del docente; puoi riordinarlo e asciugarlo, non aggiungere fatti.
- Al massimo 1 emoji, facoltativa. Niente punti esclamativi a catena.
- Tag degli enti citati solo se l'utente ne conosce l'handle; altrimenti nomi per esteso.
- Hashtag in fondo, 6–10: fissi `#LTMarconiVerona #MarconiVerona #LiceoTecnologico #ScuolaVerona` + 2–6 sul tema (es. `#EducazioneFinanziaria #UniVR`). Niente hashtag generici di massa (#love, #instagood).

## Articolo per il sito

Struttura:
- **Titolo** (max ~70 caratteri) e **occhiello/sommario** di una frase.
- 3–5 paragrafi: apertura con il fatto (chi, cosa, quando, dove); svolgimento (contenuti dell'attività, temi visti nelle foto/slide); partecipazione degli studenti; chiusura con il valore per la scuola o i prossimi passi, solo se noti.
- Registro istituzionale ma vivo, terza persona ("alcune classi del nostro istituto"), 200–400 parole.
- Ringraziamenti a enti e docenti citati nel materiale.
- Suggerisci quali foto usare come apertura e galleria e il testo alternativo (alt) per ciascuna.
- Passa tutto con scrittura-italiana prima di consegnare.

## Consegna

Risposta breve: link al canvas (card), una riga sui layout scelti, poi la didascalia in un blocco citato e l'articolo sotto, pronti da copiare. Offri di cambiare layout o aggiungere slide.