# read srr accession number file
# SRR00000
# wget https://sra-downloadb.be-md.ncbi.nlm.nih.gov/sos1/sra-pub-run-5/SRR1916152/SRR1916152.1
# read accession file
#    for each line:
#      generate wget cmd
import sys
#print(sys.argv[1])
acc_file = sys.argv[1]   
with open(acc_file) as acc_file_handle:
    for line in acc_file_handle:
        line = line.rstrip()
        #print(line)
        cmd_str = "wget https://sra-downloadb.be-md.ncbi.nlm.nih.gov/sos1/sra-pub-run-5/{srr_acc}/{file}".format(srr_acc=line,file=line+".1")
        print(cmd_str) 

