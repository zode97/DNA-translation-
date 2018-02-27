def read_seq(inputfile):
    ''' Reads and returns the input sequence with special charecters removed'''
    with open(inputfile, "r") as f:
        seq = f.read()
    seq = seq.replace("\n", "") # strings are immutable so now this is a new string and we have to assign it to a new veriable 
    seq = seq.replace
    return seq
DNA = read_seq("DNA.txt.py")
inputfile = "DNA.txt.py"
with open(inputfile, "r") as f:
    seq = f.read()

inputfile = "DNA.txt.py"
f = open(inputfile, "r")
seq = f.read()
# remove the cherecters \n from the list DNA 
seq = seq.replace("\n", "") # strings are immutable so now this is a new string and we have to assign it to a new veriable 
seq = seq.replace("\r", "")
def translate(seq):
    ''' Translate a string containing a nucleotide sequence into a string containing the corresponding sequence of amino acids''' 
    table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    '''To translate the DNA I am going to use table above. 
    1. First, I need to check if the lenght of the sequence can be devided by 3 (len(sequence%3 == 0)
    2. Second, I need to look up if the 3 letter string is anywhere in the table and then store the result 
    3. Third steps, I will do step 1 & 2 untill the end of the sequence'''
    protein = ""
    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            x = seq
            protein += table[x]
    return protein
print translate ("GCC")
print seq[40:50]
