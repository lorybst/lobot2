
def schoener(s):
    return input(">"+ s + "\n*")
# Bot spricht mit dem Mensch
mensch= schoener("hallo")

if "hallo" in mensch or "hi" in mensch: 
    mensch = schoener ("Wie geht es Dir?")
else:
    mensch = schoener("Ich verstehe dich nicht")

if "gut" in mensch:
    mensch=schoener("prima")
elif "schlecht" in mensch:
    mensch = schoener("schade")
else:
    mensch = schoener ("ich vertsehe dich nicht")

print ("Auf Wiedersehen!")    
