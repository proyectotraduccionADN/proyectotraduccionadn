
import re
def lector(archivo):
    f=open("AC005021.txt","r", encoding="utf-8", errors="ignore")
    t=f.read()
    t=re.sub('[1()234567890/\.,;*><_,.!?¿#:¡()@]',' ', t)
    t=t.upper()
    t=t.replace("\n", "")
    t=t.replace("\r", "")
    f.close()
    return t

cadena=lector("AC005021.txt")


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
   
def Nucleotidos(cadena):
    a=0
    g=0
    t=0
    c=0
    for i in cadena:
        if i =="A":
            a+=1
        if i=="T":
            t+=1
        if i=="C":
            c+=1
        if i=="G":
            g+=1
            
    d=print("A =" ,a,"C=",c,"G=",g,"T=",t)
    return d

def INVERSO(cadena):
    adn=""
    for i in reversed(cadena):
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
    
def traductor(seq):
    proteina = ""
    table = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K','AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L','CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V','GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S','TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':' _ ', 'TAG':' _ ', 'TGC':'C', 'TGT':'C', 'TGA':' _ ', 'TGG':'W',}
      
    if len(seq)%3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i : i+3]
            proteina += table[codon]
    return proteina

print(traductor(cadena))

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

