import sys
#print(sys.argv[1])
acc_file = sys.argv[1]
with open(acc_file) as acc_file_handle:
    for line in acc_file_handle:
        line = line.rstrip()
        cmd_str = "fastq-dump {srr_file}\nfastqc {fq_file}".format(srr_file=line+".1", fq_file = line + ".1.fastq") 
        print(cmd_str)
       
