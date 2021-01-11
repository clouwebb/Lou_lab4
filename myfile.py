#Catherine Lou
#Lab 4
#Ms. DeRanek
#Rosalind

#AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
#my results should return 20 12 17 21


#make a selecttion sort function
def selectsort (dnaseq):

    A = 0
    G = 0
    C = 0
    T = 0

    numseq = []
    
    while len (dnaseq) > 0:

        for numseq in dnaseq:
#the code below should be saying that if there is and A in the dna sequence, then i will make a newA that adds up to the old A
            if dnaseq(A) = A:
                newA = A + 1
            if dnaseq(G) = G:
                newG = G + 1
            if dnaseq(C) = C:
                newC = C + 1
            if dnaseq(T) = T:
                newT = T + 1
#i will return the "new" number and it should be an integer
            return (newA, newG, newC, newT)

if __name__ == "__main__":
    dnaseq = [AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC]
    selectsort (dnaseq)
    print (numseq)


