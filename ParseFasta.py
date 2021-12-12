import Bio
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio.Alphabet import SingleLetterAlphabet
handle = open("/home/jbrown/bin/NWMProject/RepeatFiles/AotusFiles/AotusDNAEdited.fasta.masked") # place location of file here
OutPut=open("/home/jbrown/bin/NWMProject/Blat/AotusRMAlu.fasta", "w")#this is the file where the Alu sequences are placed
DraftOutPut=open("/home/jbrown/bin/NWMProject/RepeatFiles/AotusFiles/AotusDraftSeq.fasta","w") #this is where the draft sequences will go 
#Count=open("/home/jbrown/bin/NWMProject/Blat/AotusCount.txt", "a")#this file is to check what file number I'm on 
Aotus_dict = SeqIO.to_dict(SeqIO.parse(handle, "fasta")) #create a dictionary of the handle variable= NWM sequences from NCBI
handle.close()

#keys=['gi|725077502|gb|KM593788.1|','gi|725077500|gb|KM593786.1|','gi|725077504|gb|KM593790.1|']
keys=[keys.strip()for keys in open("/home/jbrown/bin/NWMProject/RepeatFiles/AotusFiles/AotusGI.txt")] #pull keys from text file/GI#s of files you want
UniqueKeys=list(set(keys)) #this gets rid of repetitive keys in the output fasta file
#print(UniqueKeys)
#StartQ=[2,4,5]
StartQ=[StartQ.strip()for StartQ in open("/home/jbrown/bin/NWMProject/RepeatFiles/AotusFiles/AotusStartQ.txt")] #pulls start place of Alu
#EndQ=[350,300,200]
EndQ=[EndQ.strip()for EndQ in open("/home/jbrown/bin/NWMProject/RepeatFiles/AotusFiles/AotusEndQ.txt")] #pull end place of Alu
n=0
#Count.write("This is the number of Unique Keys:\n")
#Count.write(str(len(UniqueKeys)))
if len(keys)!=len(StartQ) and len(EndQ):
    print(" Number of GI/Key values do not equal Start and End Values!!!...Check your files")
for item in UniqueKeys:
    record=(Aotus_dict[item])
    description=record.description
    if "DRAFT" in description:
        SeqIO.write(record,DraftOutPut,"fasta")
    else:
        SeqIO.write(record,OutPut,"fasta")
    # This prints out the sequence of the GI number you input
    # I could create a function so it pull the index numbers from a list for each item so it pulls approximately so much flanking and the
    #alu elment from the file
    n=n+1
    #Count.write(str(n))

OutPut.close()
#Count.close()
