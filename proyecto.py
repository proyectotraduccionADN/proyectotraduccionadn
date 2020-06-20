#dna=open("unacadena.txt","r")
#dna=dna.read()

dna= input ('escriba aqui la cadena de ADN')
dic_aminos={'GGA':'Gly','GGG':'Gly','GGU':'Gly','GGC':'Gly','GAG':'Glu','GAA':'Glu','GAC':'Asp','GAU':'Asp','GUG':'Val','GUA':'Val','GUU':'Val','GUC':'Val','GCG':'Ala','GCA':'Ala','GCU':'Ala','GCC':'Ala',
'AGG':'Arg','AGA':'Arg','AGU':'Ser','AGC':'Ser','AAG':'Lys','AAA':'Lys','AAU':'Asn','AAC':'Asn','AUG':'Met','AUA':'Iso','AUU':'Iso','AUC':'Iso','ACG':'Thr','ACA':'Thr','ACU':'Thr','ACC':'Thr',
'UGG':'Try','UGA':'STOP','UGU':'Cys','UGC':'Cys','UAG':'STOP','UAA':'STOP','UAU':'Tyr','UAC':'Tyr','UUG':'Leu','UUA':'Leu','UUU':'Phe','UUC':'Phe','UCG':'Ser','UCA':'Ser','UCU':'Ser','UCC':'Ser',
'CGG':'Arg','CGA':'Arg','CGU':'Arg','CGC':'Arg','CAG':'Gln','CAA':'Gln','CAU':'His','CAC':'His','CUG':'Leu','CUA':'Leu','CUU':'Leu','CUC':'Leu','CCG':'Pro','CCA':'Pro','CCU':'Pro','CCC':'Pro'}
dna=dna.upper()
for i in dna:
    if i != "A" and i != "G" and i != "T" and i != "C" and i != "U":
            dna=dna.replace(i,"")
#print(dna)
 
def RNA (cadena):
    for i in cadena:
        if i=="T":
            rna=cadena.replace("T","U")
    return rna
   

def INVERSO(cadena):
    adn=""
    for i in cadena:
        if i =="A":
            adn=adn+"T"
        if i=="T":
            adn=adn+"A"
        if i=="C":
            adn=adn+"G"
        if i=="G":
            adn=adn+"C"
    dna=adn
    return dna


def Transcripcion(cadena):
    rna=""
    for i in cadena:
        if i =="A":
            rna=rna+"U"
        if i=="T":
            rna=rna+"A"
        if i=="C":
            rna=rna+"G"
        if i=="G":
            rna=rna+"C"
    return rna
    
    
def Proteinas(cadena):
    rna=RNA(cadena)
    count=0
    amino=""
    proteina=""
    for i in rna:
        amino=amino+i
        count=count+1
        if count==3:
            an=dic_aminos[amino]
            count=0
            amino=""
            if an =="STOP":
                proteina=proteina+an
                break
            proteina=proteina+an+", "
    return proteina

#print(Proteinas(dna),"proteina")
#print(Transcripcion(dna),"trans")
#print(RNA(dna),"rna")
#print(INVERSO(dna),"inverso")

