hisat2 -x ../../data/reference/yeast_ref -U ../../data/RNA-seq/SRR1916152.1.fastq |samtools view -bS -| samtools sort - -o EV_strain_3.srt.bam
