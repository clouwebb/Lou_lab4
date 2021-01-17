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


