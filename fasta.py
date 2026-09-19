from Bio import SeqIO
for record in SeqIO.parse("sequences.fasta", "fasta"):

    seq_id = record.id

    sequence = str(record.seq)

    length = len(sequence)

  
    gc_content = (sequence.upper().count("G") +
                  sequence.upper().count("C")) / length * 100

    print("ID:", seq_id)
    print("Length:", length)
    print("GC Content: {:.2f}%".format(gc_content))
    print()
