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
    
#i did not need the while loop because the string is never going to change in length
    for letter in dnaseq:       
#if i want to compare the letters, i need to make it a string because and A does not equal the interger A
        if letter == 'A':    
#removed the newA because it becomes conditional to whether i actually see A or not. If i dont then newA becomes useless

            A = A + 1
        if letter == 'G':
            G = G + 1
        if letter == 'C':
            C = C + 1
        if letter == 'T':
            T = T + 1
            
    print (A, G, C, T)

#i am doing it from a string not a list!!!!!
if __name__ == "__main__":
    dnaseq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
    selectsort (dnaseq)
    print (dnaseq)


#Problem 2
#Catherine
#RNA is A, G, C, U
#transcribe the T to U

#input
#GATGGAACTTGACTACGTAAATT
#Output 
#GAUGGAACUUGACUACGUAAAUU

def transcribe (dnaseq):

#running from the front all the way to the end
    T = dnaseq[0:]    
#this is the newstring replacing the T with U
    dnaseq = T.replace ("T", "U")
    print (dnaseq)
    
#printing the rna strand

if __name__ == '__main__':
    dnaseq = 'GATGGAACTTGACTACGTAAATT'
    transcribe (dnaseq)
    print (dnaseq)


#problem 3
#catherine

#input:
#AAAACCCGGT
#output:
#ACCGGGTTTT

def reverse(dnaseq):

#this is making the computer read the list backwards
    reverse = dnaseq[::-1]
#this is individually changing the code by having a "temp"
    reverse = reverse.replace('A', 't')
    reverse = reverse.replace('T', 'a')
    reverse = reverse.replace('G', 'c')
    reverse = reverse.replace('C', 'g')
    reverse = reverse.upper()    
#printing out the new statement

    print (reverse)
    
#calling the function

if __name__ == "__main__":
    dnaseq = 'AAAACCCGGT'
    reverse (dnaseq)

#problem 4
#Catherine Lou

#input
#GAGCCTACTAACGGGAT
#CATCGTAATGACGGCCT

#output

def hamming (dnaseq1, dnaseq2):
   
# Return the Hamming distance between dnaseq1 and dnaseq2.
    hammingdistance = 0
    DNASEQ1 = len(dnaseq1)
    for i in range(DNASEQ1):
        
#telling my computer to add one to the "hammingdistance" variable if there is one that doesnt match
        if dnaseq1[i] != dnaseq2[i]:
#in addition to adding one, also look past it and scan the next letter
            hammingdistance += 1   
#return the final hamming distance

    return hammingdistance

if __name__ == "__main__":
    finaldist = hamming('GAGCCTACTAACGGGAT','CATCGTAATGACGGCCT')
    print (finaldist)
    
#problem 5
#Catherine

#input 
#GATATATGCATATACTT
#ATAT

#output
# 2, 4, 10

#Functions
def findmotif(dnaseq, motif):

#making the locations a list so i can add stuff at the end easily
    locations = []
#turning the motif and dnaseq into lengths so it makes it easy for comparison and also accurate
    motiflen = len(motif)
    dnaseqlen = len(dnaseq)
#this is me telling my code that for i in my dnaseq length, if they find something that starts with ATAT (the Motif)
    for i in range(dnaseqlen):
        if dnaseq[i:].startswith("ATAT"):
#then they can add one to i within the locations list
            locations.append(i + 1)  

    return locations

if __name__=='__main__':
    motif = 'ATAT'
    dnaseq = 'GATATATGCATATACTT'

    print (findmotif ('GATATATGCATATACTT', 'ATAT'))
    
