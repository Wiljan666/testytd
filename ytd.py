import os
import subprocess
import streamlit as st

def verwijder_temp_bestanden():
    temp_map = os.environ.get('TEMP')
    if temp_map:
        for root, dirs, files in os.walk(temp_map):
            for bestand in files:
                bestand_pad = os.path.join(root, bestand)
                subprocess.run(['cmd', '/c', 'del', bestand_pad], shell=True)
                st.write(f"Verwijderd: {bestand_pad}")
            for map in dirs:
                map_pad = os.path.join(root, map)
                subprocess.run(['cmd', '/c', 'rmdir', '/s', '/q', map_pad], shell=True)
                st.write(f"Verwijderd: {map_pad}")
        alert(f"Bestanden in de %temp%-map zijn succesvol verwijderd.", "Succes")

verwijder_temp_bestanden()
