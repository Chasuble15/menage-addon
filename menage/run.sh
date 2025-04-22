#!/bin/bash
echo "Démarrage de l'add-on Ménage..."

# Créer le fichier de stockage si absent
if [ ! -f /data/storage.json ]; then
  echo "Initialisation du fichier de données..."
  cp /storage.json.template /data/storage.json
fi

python3 /webserver.py