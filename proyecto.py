a= input ('escriba aqui la cadena de ADN')
dic_aminos={'GGG':'Gly','GGA':'Gly','GGU':'Gly','GGC':'Gly','GAG':'Glu','GAA':'Glu','GAU':'Asp','GAC':'Asp','GUG':'Val','GUA':'Val','GUU':'Val','GUC':'Val','GCG':'Ala','GCA':'Ala','GCU':'Ala','GCC':'Ala',
'AGG':'Arg','AGA':'Arg','AGU':'Ser','AGC':'Ser','AAG':'Lys','AAA':'Lys','AAU':'Asn','AAC':'Asn','AUG':'Met','AUA':'Iso','AUU':'Iso','AUC':'Iso','ACG':'Thr','ACA':'Thr','ACU':'Thr','ACC':'Thr',
'UGG':'Try','UGA':'STOP','UGU':'Cys','UGC':'Cys','UAG':'STOP','UAA':'STOP','UAU':'Tyr','UAC':'Tyr','UUG':'Leu','UUA':'Leu','UUU':'Phe','UUC':'Phe','UCG':'Ser','UCA':'Ser','UCU':'Ser','UCC':'Ser',
'CGG':'Arg','CGA':'Arg','CGU':'Arg','CGC':'Arg','CAG':'Gln','CAA':'Gln','CAU':'His','CAC':'His','CUG':'Leu','CUA':'Leu','CUU':'Leu','CUC':'Leu','CCG':'Pro','CCA':'Pro','CCU':'Pro','CCC':'Pro'}
a=str(a)
count=0
amino=None
for i in a:
    #print (i)
    while count<=3:
        amino=amino+i
        count=count+1
        if count==3:


