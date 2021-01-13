#Catherine Lou
#Lab 4
#Ms. DeRanek
#Rosalind

#AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
#my results should return 20 12 17 21


#make a selecttion sort function
def selectsort (dnaseq):

#this is how i make the letters integers
    A = 0
    G = 0
    C = 0
    T = 0

    numseq = []
    
    while len (dnaseq) > 0:

        for letter in dnaseq:
#the code below should be saying that if there is and A in the dna sequence, then i will make a newA that adds up to the old A

            if letter = A:
                newA += 1
                newA = newA + 1
            if letter = G:
                newG += 1
                newG = newG + 1
            if letter = C:
                newC += 1
                newC = newC + 1
            if letter = T:
                newT += 1
                newT = newT + 1
                
#i will return the "new" number and it should be an integer
            return (newA, newG, newC, newT)

#calling
if __name__ == "__main__":
    dnaseq = [AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC]
    selectsort (dnaseq)
    print (numseq)
    
#Problem 2
#Catherine
#RNA is A, G, C, U
#transcribe the T to U

#input
#GATGGAACTTGACTACGTAAATT
#Output 
#GAUGGAACUUGACUACGUAAAUU

def transcribe (dnaseq):


    while len(dnaseq) > 0:
        
        rna = dnaseq[0:]
        rna = rna.replace ("T", "U")

if __name__ == "__main__":
    dnaseq = ["GATGGAACTTGACTACGTAAATT"]
    transcribe (dnaseq)
    print (dnaseq)



