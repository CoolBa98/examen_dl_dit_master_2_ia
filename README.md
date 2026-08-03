OBJECTIF DU PROJET: 
mettre en place une application IA pour l'analyse d'un des sentiments des clients d'une entreprise à partir d'un fichier audio


ARCHITECTURE:
le projet contient 4 dossiers et 2 fichiers principaux:

  DOSSIERS:
  - api: il contient toutes les ressources necessaires pour la mise en place de l'api,
  - gradio: il contient toutes les ressources necessaires pour l'interface gradio,
  - notebook: il contient le notebook telechargeable pour tester gradio en local et toutes les ressources pour la mise en place de l'applicaiton IA:
    - les modèles utilisés,
    - la transcription des fichiers audios en texte,
    - la classification de l'audio selon qu'il soit negatif, neutre ou positif.
  - process: il contient deux fichiers qui sont utilises par l'api:
    - transcription: pour la transcription du fichier en texte,
    - sentiment: pour la classification des transcriptions.

  FICHIERS:
  - procfile: contient des instructions pour le lancement de l'api,
  - requirements: contient les dependances necessaires a l'execution de l'application entiere
