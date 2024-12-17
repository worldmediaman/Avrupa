#!/bin/bash
set -e  # Skript bei Fehlern abbrechen
set -x  # Debugging aktivieren

# Ausführung des Python-Skripts und Umleitung der Ausgabe
python3 Stream/cnn.py > Stream/cnn.m3u8

exit 0
