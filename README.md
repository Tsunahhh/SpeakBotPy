# SpeakBot Python
## Installation

### Python

Installez python depuis le site : https://www.python.org/downloads/

### FFMPeg

#### Windows
* Télécharge le fichier zip de FFmpeg depuis le site officiel. https://ffmpeg.org/download.html
* Extrayez-le et ajoutez le dossier `bin` de FFmpeg à votre variable d'environnement PATH.

#### Linux
> sudo apt install ffmpeg

#### MacOS
> brew install ffmpeg

### Création du projet et de l'environnement

Installer l'environnement
> python3 -m venv .env

Créez un fichier `token.txt` à la raçine du projet et glissez le token de votre bot dedans.

Activer l'environnement, grace à `Activate` qui se trouve dans `.env/bin` pour linux et `.env/Scripts` pour Windows

> .env\Scripts\Activate

### Packages Python

> pip install discord\
> pip install discord-py-interaction\
> pip install PyNaCl