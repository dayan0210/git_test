import sys
#print(sys.argv[1])
acc_file = sys.argv[1]   
ref = sys.argv[2]
fq_dir = sys.argv[3]
with open(acc_file) as acc_file_handle:
    for line in acc_file_handle:
        line = line.rstrip()
        ele = line.split("\t")
        #print(ele)
        cmd_str = "hisat2 -x {ref} -U {fq_dir}/{srr_acc}.1.fastq |samtools view -bS - | samtools sort - -o {sample_real_name}.srt.bam\nsamtools index {sample_real_name}.srt.bam".format(ref = ref, fq_dir = fq_dir, srr_acc=ele[0], sample_real_name = ele[1])
        print(cmd_str) 

