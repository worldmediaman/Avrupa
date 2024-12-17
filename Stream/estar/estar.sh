#!/bin/bash
set -e  # Skript bei Fehlern abbrechen
set -x  # Debugging aktivieren

# Verzeichnisinhalt anzeigen
ls -la Stream/estar

# Ausführung des Python-Skripts und Umleitung der Ausgabe
python3 Stream/estar/estar.py > Stream/estar/estar.m3u8

exit 0
