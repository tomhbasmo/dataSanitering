import pandas as pd
import csv

#hardcoded path til .csv fil:
df = pd.read_csv('/Users/tomhenrikmeltingbasmo/Documents/Bruker-eksperiment: Piltaster eller "WASD"-3.csv')

def sjekkValiditet(x):
    #kunne ha fjernet de som ikke bruker datamaskin her, men er ikke så farlig..
    return x


df.fillna('')
df.fillna('', inplace=True)
#lager liste over spørsmål, for å kunne finne riktige svar
listeOverKolonner = [sjekkValiditet(x) for x in df]
validSvarListe = []


def isCurrentRowGamer(row):
    if int(row[listeOverKolonner[8]]) >= 3:
        return True
    else:
        return False


for index, row in df.iterrows():
    if ("Datamaskin" in row[listeOverKolonner[1]]):
        # ser først på keystrokes
        #print(listeOverKolonner[3])
        print(row[listeOverKolonner[3]], index)
        if not isinstance(row[listeOverKolonner[3]], float) or row[listeOverKolonner[3]] != "":
            if "ArrowUp" in row[listeOverKolonner[3]] or "ArrowRight" in row[listeOverKolonner[3]] or "ArrowLeft" in \
                    row[
                        listeOverKolonner[3]] or "ArrowDown" in row[listeOverKolonner[3]]:
                gamerBool = isCurrentRowGamer(row)
                # hvis brukeren brukte arrowskeys først, vil det si at kolonne 4 betyr deres rating for piltastene, og omvendt
                validSvarListe.append((gamerBool, row[listeOverKolonner[4]], row[listeOverKolonner[5]]))
            elif "w" in row[listeOverKolonner[3]] or "a" in row[listeOverKolonner[3]] or "s" in row[
                listeOverKolonner[3]] or "d" in row[listeOverKolonner[3]]:
                gamerBool = isCurrentRowGamer(row)
                validSvarListe.append((gamerBool, row[listeOverKolonner[5]], row[listeOverKolonner[4]]))

            else:
                # hvis keystrokes ikke fins, ser vi bare på selvrapporteringen, dvs data[2]
                gamerBool = isCurrentRowGamer(row)
                if "Piltastene" in row[listeOverKolonner[2]]:
                    validSvarListe.append((gamerBool, row[listeOverKolonner[4]], row[listeOverKolonner[5]]))
                if "WASD" in row[listeOverKolonner[2]]:
                    validSvarListe.append((gamerBool, row[listeOverKolonner[5]], row[listeOverKolonner[4]]))

print(validSvarListe)
print("LOLOLOLOLOL")
with open('sanitizedData.csv', 'w') as out:
    csv_out = csv.writer(out)
    csv_out.writerow(['gamer', 'piltastrating', 'wasdrating'])
    for row in validSvarListe:
        csv_out.writerow(row)
