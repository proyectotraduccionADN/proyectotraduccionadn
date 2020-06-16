#dna=open("unacadena.txt","r")
#dna=dna.read()

dna= input ('escriba aqui la cadena de ADN')
dic_aminos={'GGG':'Gly','GGA':'Gly','GGU':'Gly','GGC':'Gly','GAG':'Glu','GAA':'Glu','GAU':'Asp','GAC':'Asp','GUG':'Val','GUA':'Val','GUU':'Val','GUC':'Val','GCG':'Ala','GCA':'Ala','GCU':'Ala','GCC':'Ala',
'AGG':'Arg','AGA':'Arg','AGU':'Ser','AGC':'Ser','AAG':'Lys','AAA':'Lys','AAU':'Asn','AAC':'Asn','AUG':'Met','AUA':'Iso','AUU':'Iso','AUC':'Iso','ACG':'Thr','ACA':'Thr','ACU':'Thr','ACC':'Thr',
'UGG':'Try','UGA':'STOP','UGU':'Cys','UGC':'Cys','UAG':'STOP','UAA':'STOP','UAU':'Tyr','UAC':'Tyr','UUG':'Leu','UUA':'Leu','UUU':'Phe','UUC':'Phe','UCG':'Ser','UCA':'Ser','UCU':'Ser','UCC':'Ser',
'CGG':'Arg','CGA':'Arg','CGU':'Arg','CGC':'Arg','CAG':'Gln','CAA':'Gln','CAU':'His','CAC':'His','CUG':'Leu','CUA':'Leu','CUU':'Leu','CUC':'Leu','CCG':'Pro','CCA':'Pro','CCU':'Pro','CCC':'Pro'}
dna=dna.upper()
for i in dna:
    if i != "A" and i != "G" and i != "T" and i != "C":
            dna=dna.replace(i,"")
#print(dna)
 
def RNA (cadena):
    for i in dna:
        if i=="T":
            rna=dna.replace("T","U")
    return rna
   

def INVERSO(cadena):
    adn=""
    for i in cadena:
        if i =="A":
            adn.append("T")
        if i=="T":
            adn.append("A")
        if i=="C":
            adn.append("G")
        if i=="G":
            adn.append("C")
    #a=print( "".join(x for x in adn))
    dna=adn
    return dna


def Transcripicion(cadena):
    rna=""
    for i in cadena:
        if i =="A":
            rna.append("U")
        if i=="T":
            rna.append("A")
        if i=="C":
            rna.append("G")
        if i=="G":
            rna.append("C")
    #print( "".join(x for x in rna))
    return rna
    
    
def Proteinas(cadena):
    rna=RNA(cadena)
    count=0
    amino=""
    proteina=""
    #print(a)
    for i in rna:
        amino=amino+i
        count=count+1
        if count==3:
            an=dic_aminos[amino]
            proteina=proteina+an+", "
            count=0
            amino=""
    return proteina

print(Proteinas(dna))
