---
name: marconi-media-lab
description: Da descrizione e foto di un evento del L.T. Marconi di Verona crea carosello Instagram 4:5, banner sito 2000×700, didascalia IG con hashtag e articolo per il sito.
---

# Marconi Media Lab

Kit della redazione social del **Liceo Tecnologico G. Marconi di Verona** (L.T., ex ITI; Instagram @itimarconiverona).
Input tipico: un testo inviato da un docente + foto (a volte video, PDF, .docx, zip).

Output, **sempre tutti**, salvo richiesta diversa:

1. **Carosello Instagram 4:5** (1080×1350), 3 slide di default (2–6 se richiesto)
2. **Banner sito** 2000×700, **sempre con un elemento grafico del Marconi** (vedi «Banner»)
3. **Didascalia Instagram** con **5 hashtag** e firma finale (vedi «Didascalia»)
4. **Articolo per il sito**
5. **Export in Figma**, automatico se il connettore Figma è collegato (vedi «Export in Figma»)

## Regola d'oro: ogni post ha un layout diverso

I post devono riconoscersi subito come «del Marconi» (palette, forme a tessera, logo, font) ma **non devono mai sembrare uguali**: chi scorre il profilo non deve vedere due caroselli di fila con la stessa impaginazione.

- Ogni post usa una **combinazione nuova** di layout: copertina + slide interne + chiusura + banner.
- **La copertina non ripete nessuna delle copertine degli ultimi 3 post**; slide interne, chiusura e banner non ripetono quelli del post precedente.
- Varia anche **colore di accento** (vedi «Colore per tema») e **tipo di immagine dominante** (foto a tutta pagina / foto in tessera / blocco colore / collage).
- Se l'utente chiede «cambia layout», scegli una combinazione che non ha ancora visto in questa conversazione.

**Come sapere cosa è già stato usato** (fallo all'inizio, in silenzio):
1. Guarda i post già fatti in questa conversazione.
2. Cerca i canvas precedenti: `list_artifacts` con query `Post IG` e poi con `Carosello IG`; per i 3–5 più recenti leggi `project/canvas.json` e cerca la nota `layout` (formato: `Layout: C2 · I5 · F3 · B4`).
3. Se non trovi nulla, considera lo storico qui sotto.
4. Scrivi **sempre** la combinazione scelta nel `canvas.json` del nuovo post, come nota sticky con id `layout`, sopra le slide: `{"layout":{"x":0,"y":-560,"w":700,"text":"Layout: C7 · I6 · F4 · B5","fill":"gray"}}`, e nel titolo del canvas usa `Post IG – <tema breve>`.

Storico iniziale (post già pubblicati, dal più vecchio):
| Post | Copertina | Interne | Chiusura | Banner | Accento |
|---|---|---|---|---|---|
| Educazione finanziaria (UniVR) | C1 | I1 | F1 | B1 | verde |
| NoPanicSim (AOUI) | C5 | I2 | I4 | B2 | fucsia |
| Museo Africano (3CI/3BI) | C2 | I4 | F1 | B3 | bordeaux |

## Flusso

1. **Leggi tutto il materiale**: ogni foto (correggi la rotazione EXIF), i testi (.docx con pandoc, PDF renderizzati), estrai 4–5 fotogrammi dai video con ffmpeg. Estrai dalle foto solo testi leggibili davvero.
2. **Controlla i fatti**: date (giorno della settimana coerente con la data?), nomi, classi. Niente fatti inventati: se manca un dato usa `[DATO]` e segnalalo. Testo del docente in prima persona → riportalo alla terza persona.
3. **Scegli la combinazione di layout** (regola d'oro) e il colore di accento.
4. **Grafiche** → un canvas del tipo artifact **Design**: un artboard per slide + il banner in una riga sotto (120 px). Carica foto e loghi come asset (mai data URI), **sempre compreso il logo Media Lab trasparente** (nero e/o bianco). Nota `layout` nel `canvas.json`.
5. **Testi** → carica la skill **scrittura-italiana** (`anthropic-skills:scrittura-italiana`) PRIMA di scrivere didascalia e articolo, e applicala a entrambi.
6. **Export in Figma** se disponibile.
7. **Consegna**: link al canvas (card), una riga con i layout usati, didascalia e articolo pronti da copiare, link Figma, dati da verificare.

## Brand

### Colori ufficiali (Guida colori Marconi)
Usa **solo** questi HEX. Ogni indirizzo ha il suo colore.

| Ruolo | HEX | Indirizzo / uso |
|---|---|---|
| Viola | `#8439BD` | Conduzione del mezzo aereo |
| Verde | `#85B835` | Logistica |
| Azzurro | `#1E9DC8` | Telecomunicazioni |
| Giallo | `#F9BD28` | Informatica |
| Bordeaux | `#A72F4A` | Elettronica (e robotica) |
| Fucsia | `#E4105D` | Costruzione del mezzo |
| Testo | `#404040` | testi, pill scure, velature (`rgba(64,64,64,.82)`) |
| Sfondo | `#ECECEC` | fondo delle grafiche chiare |

Contrasto (≥ 4.5:1 testo normale, ≥ 3:1 titoli ≥ 48 px):
- Testo piccolo su sfondo chiaro: `#404040`, bordeaux, viola.
- Titoli grandi su chiaro: anche fucsia; azzurro e verde solo nelle varianti scure `#157EA3` e `#5A8A1E`.
- Giallo e verde mai come testo su chiaro: usali come riempimento (con testo `#404040` sopra) o come testo su fondo scuro/foto velata.
- Su azzurro, viola, bordeaux, fucsia: testo bianco.

### Colore per tema
Un solo accento per post, legato al tema; ruota rispetto al post precedente.
- Evento di un indirizzo → il suo colore.
- Salute/emergenza/sport → fucsia; cultura/storia/musei → bordeaux o viola; economia/ambiente → verde; tecnologia/media/STEM → azzurro; creatività/orientamento/open day → giallo.

### Forme e tipografia
- **Font**: Montserrat (Google Fonts) 500–900, titoli 900 con letter-spacing negativo. Montserrat c'è anche in Figma. I font del brand kit (`assets/fonts/`: Berlin Sans FB, Franklin Gothic Demi Cond) servono per presentazioni e documenti, non per il canvas.
- **Forma "tessera"** (dal logo): un angolo quasi retto + angoli molto arrotondati, es. `border-radius: 24px 130px 130px 0`. Per forme, card, angoli delle foto.
- **Firma grafica**: due tessere (gialla `#F9BD28` e azzurra `#1E9DC8`) nell'angolo in alto a destra, in parte fuori bordo. Sempre presenti, ma la posizione può cambiare (in alto a destra, oppure in basso a sinistra nei layout dove l'alto è occupato da una foto piena).
- **Vietato**: la scaletta colorata del logo usata come fascia decorativa in basso; gradienti; emoji nelle grafiche; testo sopra i volti; loghi "I.T.I." (il nome attuale è L.T. / Liceo Tecnologico).
- Margini 80 px (carosello), 120–200 px (banner); footer a 56 px dal fondo; testo minimo 23 px su 1080.

### Asset inclusi (`assets/`)
| Cartella | Contenuto | Quando |
|---|---|---|
| `loghi-lt/` | logo **L.T. MARCONI verona** (tessere + scritta): `lt_colorato_testo_scuro.png` (su chiaro), `lt_colorato_testo_bianco.png` (su scuro/foto), `lt_solo_tessere.png` (footer slide interne), originale su nero | logo principale, sempre |
| `loghi-marconi/` | logo «MARCONI verona» a scaletta: colorato testo nero/bianco, tutto bianco, tutto nero | come elemento di marca nel banner o in copertine grandi, **mai** come fascia decorativa |
| `loghi-speciali/` | logo natalizio e logo estivo | post di dicembre/vacanze di Natale, post di giugno–agosto |
| `loghi-progetti/` | «In cattedra per un giorno» | solo per quel progetto (la grafica riporta ancora "ITI": segnalalo) |
| `media-lab/` | logo Marconi Media Lab **su sfondo trasparente**: `medialab_rotondo_nero.png` / `medialab_rotondo_bianco.png` (1139 px, da preferire), `medialab_rettangolare_nero.png` / `_bianco.png` (bassa risoluzione, solo fino a ~60 px) | **sempre**, piccolo, in ogni slide finale e in ogni banner (vedi «Logo Media Lab») |
| `icone/tessere/` | icone degli indirizzi su tessera: `ele` (elettronica), `ini` (informatica), `tele`, `log` (logistica), `cdm` (costruzione del mezzo), `cdma` (conduzione aereo) | per post di un indirizzo, card, elenchi |
| `icone/scalette/` | icone indirizzo a gradino verticale | decorazione laterale in layout verticali |
| `icone/svg/` | le stesse icone in SVG | da caricare come immagine (`<img>`) |
| `foto-scuola/` | 6 foto aeree/esterne dell'edificio (1920 px) | sfondi, banner istituzionali, quando le foto dell'evento sono poche o deboli |
| `fonts/` | Berlin Sans FB, Franklin Gothic Demi Cond | presentazioni e documenti |

Esclusi perché superati: `logo_nuovo_ridotto`, `logo_thumb`, intestazione presentazioni (riportano "I.T.I."/"Istituto Tecnico Industriale"). Il modello di slide del brand kit non è incluso.

### Logo Media Lab (obbligatorio)
Ogni post porta la firma della redazione: il logo **Marconi Media Lab** compare **sempre**, piccolo.
- **Dove**: nell'ultima slide del carosello e nel banner, come minimo. Può stare anche in copertina se il layout lo permette senza affollare.
- **Quale file**: solo i PNG trasparenti di `assets/media-lab/`. Mai la versione con il riquadro bianco dietro, mai su un rettangolo bianco aggiunto.
- **Colore**: `_nero` su sfondi chiari (`#ECECEC`, giallo, verde), `_bianco` su foto, velature e colori scuri (viola, bordeaux, fucsia, azzurro, `#404040`). Se lo sfondo sotto è una foto molto chiara e varia, spostalo su una zona uniforme o su una tessera di colore.
- **Misura**: rotondo 64–96 px di lato nel carosello, 80–110 px nel banner. Deve essere più piccolo del logo L.T., mai in competizione con esso.
- **Posizione**: in un angolo libero o nel footer, allineato al logo L.T. o alla paginazione «n / n», con almeno 24 px di aria intorno. Mai sopra volti o testo.
- Nel banner convive con il logo del Marconi: logo L.T. (o scaletta) come elemento di marca, Media Lab piccolo come firma.

## Catalogo layout

Coordinate su 1080×1350. Quando i layout di una categoria sono già stati usati di recente, **generane uno nuovo** con il metodo di «Generare layout nuovi» (sotto il catalogo).

### Copertine
- **C1 Titolo + foto grande**: pill (data, tema) in alto; titolo 92 px su 3 righe, parola chiave in accento; foto 920×560 in basso con un angolo a tessera; logo scuro + «Scorri →».
- **C2 Foto a tutta pagina + velatura**: foto full-bleed, velatura piatta `#404040` all'82% solo nella parte bassa; pill e titolo bianco 96 px sopra; parola chiave in giallo; logo bianco.
- **C3 Foto in tessera grande**: titolo a sinistra in alto; foto dentro una tessera enorme (radius 40/0/0/300) che esce dal bordo destro.
- **C4 Numero gigante**: un dato forte del testo (data, edizione, n° classi) a 300 px in accento, titolo sotto, foto piccola a tessera.
- **C5 Split verticale**: metà sinistra blocco colore pieno con titolo spezzato su più righe, metà destra foto a tutta altezza; pill «Scorri» chiara.
- **C6 Citazione**: virgolette grandi in accento, frase breve detta da qualcuno (solo se presente nel materiale), nome sotto, foto piccola.
- **C7 Mosaico**: griglia 2×2 di foto a tutta pagina con 16 px di spazio; al centro una tessera chiara con titolo e pill.
- **C8 Titolo tipografico**: titolo enorme (130–160 px) che riempie metà pagina, una sola foto in una tessera piccola in basso a destra, icona dell'indirizzo in tessera.
- **C9 Cornice colore**: fondo pieno nel colore d'accento, foto inserita con 60 px di cornice e angolo a tessera, titolo bianco sotto la foto.
- **C10 Foto della scuola**: foto dell'edificio (`foto-scuola/`) come fondo velato, logo scaletta MARCONI grande, titolo dell'evento: per post istituzionali (open day, avvisi, risultati).

### Slide interne
- **I1 Testo + foto + 3 card**: occhiello, titolo 76 px, paragrafo; foto 920×420; tre card tessera colorate con contenuti reali.
- **I2 Timeline verticale**: 3–5 tappe con pallino colorato numerato e linea.
- **I3 Due foto + testo**: due foto affiancate con tessere speculari, testo sotto.
- **I4 Grande foto con riquadro**: foto 920×860, riquadro chiaro a tessera sovrapposto in basso a sinistra con occhiello, titolo, testo.
- **I5 Elenco numerato**: 3–5 punti con numeri 64 px nei colori degli indirizzi.
- **I6 Righe foto + testo**: 3 righe, ciascuna con foto a tessera 380×270 a sinistra e titoletto + testo a destra.
- **I7 Prima / dopo**: due metà (sopra/sotto o sinistra/destra) che contrappongono due momenti o stati (es. «caos» / «ritmo comune»), con foto e una riga ciascuna.
- **I8 Dato in evidenza**: un numero o una parola chiave enorme in accento, una frase che la spiega, foto in basso a tutta larghezza.

### Chiusure (ultima slide)
- **F1 Collage**: testo in alto con parola chiave in accento; griglia 1.35fr/1fr con foto grande a sinistra e due a destra; pill finale; logo + «n / n».
- **F2 Ringraziamenti**: «Grazie a…» con enti/persone citati, logo L.T. grande centrato, logo Media Lab piccolo, handle @itimarconiverona.
- **F3 Call to action**: domanda grande, pill-pulsante con il link (sito scuola), foto piccola.
- **F4 Split testo / foto verticale**: colonna di testo a sinistra (420 px), foto verticale a tutta altezza a destra con angolo inferiore sinistro a tessera.
- **F5 Foto piena + firma**: foto a tutta pagina, fascia chiara in basso con frase finale, logo L.T. e logo Media Lab.

Slide non finali: «n / n» nel footer a destra; a sinistra logo o solo tessere (h 52).
Slide finale: in ogni chiusura c'è anche il logo Media Lab piccolo (vedi «Logo Media Lab»).

### Banner sito 2000×700
**Ogni banner contiene almeno un elemento del Marconi** (logo L.T. scuro o bianco, logo scaletta MARCONI, fila di tessere degli indirizzi o icona dell'indirizzo) **e il logo Media Lab piccolo**. Contenuti importanti nella fascia centrale di 1600 px.
- **B1 Testo sinistra / foto destra**: colonna testo 860 px, foto 820×520 a destra con angolo a tessera; logo L.T. in basso a sinistra.
- **B2 Foto piena + riquadro**: foto full-bleed, riquadro chiaro a tessera a sinistra con pill, titolo, sottotitolo e logo L.T.
- **B3 Striscia di foto**: titolo a sinistra, tre foto strette affiancate a destra; fila di tessere sotto il titolo.
- **B4 Blocco colore + foto**: metà sinistra colore d'accento con titolo bianco e logo L.T. bianco, metà destra foto.
- **B5 Mosaico**: 4–5 foto in griglia irregolare a destra, titolo e logo scaletta MARCONI a sinistra.
- **B6 Scuola + evento**: foto dell'edificio velata come fondo, una foto dell'evento in tessera, titolo, logo bianco.

## Generare layout nuovi

Il catalogo è un punto di partenza, non un limite. Crea un layout nuovo quando:
- tutti i layout di quella categoria compaiono negli ultimi 3 post;
- l'utente ha già chiesto «cambia layout» e le alternative del catalogo sono finite;
- il materiale non si adatta a nessun layout (es. una sola foto verticale, nessuna foto, tanti numeri).

### 1. Combina gli ingredienti
Ogni layout è una combinazione di cinque scelte. Per costruirne uno nuovo, prendi un valore per ciascuna riga.

| Ingrediente | Valori possibili |
|---|---|
| **Struttura** | colonna unica · split 50/50 · split asimmetrico 1/3–2/3 · bande orizzontali · griglia 2×2 · mosaico irregolare · cornice · sovrapposizione (foto piena + riquadro) · composizione diagonale a gradini (richiama la scaletta del logo, ma con blocchi, non come fascia) |
| **Ruolo della foto** | a tutta pagina · dentro una tessera · striscia stretta · più foto in sequenza · foto piccola come dettaglio · nessuna foto (solo tipografia, icone, colore) · panoramica che continua da una slide all'altra |
| **Gerarchia** | foto protagonista · titolo protagonista (130–160 px) · numero o data gigante · domanda · citazione · elenco/tappe |
| **Colore** | fondo `#ECECEC` + accento · blocco pieno del colore d'accento · fondo `#404040` con testo chiaro · due colori di indirizzi affiancati |
| **Segno distintivo** | icona dell'indirizzo grande · linea di tappe · fila di tessere · numero · freccia · foto della scuola · logo scaletta grande |

**Regola di novità**: un layout nuovo deve differire in almeno **2 ingredienti su 5** da ogni layout usato negli ultimi 3 post e dal catalogo della stessa categoria.

### 2. Idee da cui partire
- **Biglietto**: per gite e uscite, la copertina come un biglietto (striscia con data, luogo, classi in «campi» separati da linee tratteggiate) accanto alla foto.
- **Percorso a gradini**: le tappe di una giornata come blocchi a scalino collegati, ognuno con una foto piccola.
- **Panoramica**: una foto larga divisa tra slide 1 e 2, così scorrendo l'immagine continua.
- **Domanda in copertina**: «Cosa fai se…?», con la risposta nelle slide dopo.
- **Calendario**: data enorme in un riquadro a tessera, per eventi e scadenze.
- **Scheda indirizzo**: icona dell'indirizzo grande con il suo colore, per attività di un'articolazione.
- **Fotoromanzo**: 3–4 foto in sequenza con didascalie brevi numerate.
- **Solo tipografia**: nessuna foto, titolo enorme su blocco colore, per avvisi o post senza immagini buone.

### 3. Rendilo bello: checklist
- **Un solo punto focale** per slide; si capisce cosa guardare in un secondo.
- **Griglia**: margini 80 px, spazi in multipli di 8 (16, 24, 32, 48, 80). Tutto si allinea a 2–3 assi verticali.
- **Gerarchia**: al massimo 3 dimensioni di testo per slide; titolo leggibile sul telefono (≥ 72 px in copertina, ≥ 56 px nelle interne).
- **Poche parole**: ≤ 12 in copertina, ≤ 40 nelle slide interne.
- **Colore**: un accento più i neutri; al massimo due colori di indirizzi nella stessa slide.
- **Forma tessera** ripetuta almeno due volte (foto, card, forme), così il post resta riconoscibile.
- **Foto**: inquadra i soggetti, niente teste tagliate, niente testo sopra i volti; testo su foto solo con velatura piatta o su riquadro.
- **Aria**: niente elementi che toccano il bordo per caso; se escono dal bordo, devono uscire chiaramente (≥ 60 px).
- **Coerenza nel carosello**: stesso margine, stessa posizione del footer e dei loghi in tutte le slide; composizione diversa slide per slide.
- **Marca**: tessere gialla e azzurra, logo L.T. in copertina o footer, logo Media Lab nell'ultima slide.
- **Niente decorazioni senza funzione**: ogni forma deve guidare l'occhio o contenere qualcosa.

### 4. Registra il layout nuovo
Dai al layout un codice libero nella sua categoria (C11, I9, F6, B7…) e scrivilo nella nota `layout` del canvas con una riga di descrizione, es.:
`Layout: C11 (biglietto: foto a sinistra, campi data/luogo/classi a destra) · I6 · F5 · B4`.
Così il post successivo lo trova nello storico e non lo ripete.

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
<div style="width: 1080px; height: 1350px; position: relative; overflow: hidden; background: #ECECEC; font-family: 'Montserrat', sans-serif; color: #404040">
<div aria-hidden="true" style="position: absolute; top: -90px; right: 150px; width: 260px; height: 260px; background: #F9BD28; border-radius: 24px 120px 120px 0"></div>
<div aria-hidden="true" style="position: absolute; top: 70px; right: -70px; width: 280px; height: 280px; background: #1E9DC8; border-radius: 24px 130px 130px 0"></div>
<!-- contenuti del layout -->
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"accent":{"editor":"color","default":"#A72F4A"},"$preview":{"width":1080,"height":1350}}'>
class Component extends DCLogic {
renderVals() { return { accent: this.props.accent ?? '#A72F4A' }; }
}
</script>
</body>
</html>
```
- Il primo `<div style="width: …">` è la radice dell'artboard: lo script di export lo usa come frame Figma, quindi tienilo così.
- Controlla a calcolo (non con screenshot) che titoli e pill non tocchino le forme in alto a destra (circa x > 670, y < 350) né il footer.
- Logo Media Lab nella slide finale, es. nel footer: `<img src="/_blob/<id medialab_rotondo_nero>" alt="Marconi Media Lab" style="height: 80px; width: auto; display: block">`.
- Foto: `object-fit: cover` con `object-position` scelto per non tagliare i volti.

## Logo da sfondo nero a trasparente
I loghi pronti sono in `assets/`. Per un logo nuovo su nero: `python scripts/logo_trasparente.py logo.png cartella_output/`.

## Didascalia Instagram

Scritta con **scrittura-italiana** (registro social: frasi brevi, niente tic da AI, niente fatti aggiunti). Struttura fissa:

```
<Titolo / gancio, max ~60 caratteri>

<2–4 frasi: cosa, quando, dove, chi; un dettaglio concreto dell'attività>

#LTMarconiVerona #LiceoTecnologico #<tema1> #<tema2> #<tema3>

Post a cura di <Nome Cognome> - Marconi Media Lab
```

- **Esattamente 5 hashtag**: i due fissi `#LTMarconiVerona #LiceoTecnologico` + 3 sul tema (ente, attività, indirizzo). Niente hashtag generici (#love, #instagood).
- **Firma sempre in fondo**, dopo gli hashtag: `Post a cura di Nome Cognome - Marconi Media Lab`. Il nome è quello di chi realizza il post: prendilo da ciò che sai dell'utente; se non lo sai, chiedilo una volta e poi riusalo.
- Al massimo 1 emoji, facoltativa. Virgolette dritte (registro social).

## Articolo per il sito

- **Titolo** (max ~70 caratteri) e **sommario** di una frase.
- 3–5 paragrafi, 200–400 parole: il fatto (chi, cosa, quando, dove); le attività; la partecipazione degli studenti; chiusura con ringraziamenti a enti e docenti citati. Terza persona, registro istituzionale ma vivo. Virgolette basse « ».
- Indica la foto di apertura e la galleria, con testo alternativo per ciascuna.
- Passa tutto con scrittura-italiana.

## Export in Figma (automatico)

Se nella sessione ci sono gli strumenti del connettore Figma (`mcp__Figma__*`, anche come strumenti differiti: cercali con ToolSearch «figma»), esporta **sempre**, senza chiedere, **un file Figma per post** con le slide e il banner. Se il connettore non c'è, salta questo passo e scrivi una riga: «Collega il connettore Figma per avere i post già nel tuo account».

1. **Prima** dell'export rileggi dal canvas i file `project/*.dc.html` (l'utente può averli modificati a mano) e salvali in locale.
2. `whoami` → `planKey` (se ci sono più team, chiedi quale una volta sola).
3. `create_new_file` con `fileName` = titolo del canvas, `editorType: "design"` → `create_session` con la `fileKey`.
4. Scrivi una mappa JSON `{id_asset: percorso_locale}` per tutti gli asset caricati sul canvas (l'id è la parte dopo `/_blob/`) e genera l'HTML:
   `python scripts/build_figma.py <cartella project> export.html mappa.json Main Slide2 Slide3 Banner`
   Lo script incorpora le immagini ridotte (≤ 1200 px) e marca ogni artboard con `class="board"`.
5. `html_to_figma` con `fileKey`, `cssSelector: ".board"`, `sessionId`, un `promptId` nuovo (UUID) → POST del file all'URL restituito:
   `curl -sS -X POST "<submitUrl>" -H "Content-Type: text/html" --data-binary @export.html`
   L'URL è monouso: se risponde 500, riduci le immagini o togli risorse esterne, chiedi un nuovo URL e riprova una volta.
6. Controllo: `get_screenshot` della copertina (nodeId restituito) e verifica che testo e foto ci siano.
7. Consegna il link al file Figma.

## Consegna
Risposta breve, senza ripetere ciò che si vede sul canvas:
- una riga con i layout usati (es. «Copertina C7 a mosaico, interne I6, chiusura F5, banner B4; accento viola»);
- la didascalia in un blocco citato, pronta da copiare (con 5 hashtag e firma);
- l'articolo sotto;
- il link Figma (se esportato);
- i dati da verificare (date incoerenti, nomi mancanti, foto assenti).
