# SpeakBot Python
## Installation

### FFMPeg

#### Windows
* Télécharge le fichier zip de FFmpeg depuis le site officiel. https://ffmpeg.org/download.html
* Extrayez-le et ajoutez le dossier `bin` de FFmpeg à votre variable d'environnement PATH.

#### Linux
> sudo apt install ffmpeg

#### MacOS
> brew install ffmpeg

### Création de l'environnement python
> python3 -m venv .env

Activer l'environnementn, grace à `Activate` qui se trouve dans `.env/bin` pour linux et `.env/Scripts` pour Windows

> .\.env\Scripts\Activate

### Packages Python

> pip install discord\
> pip install discord-py-interaction\
> pip install PyNaCl