#!usr/bin/env python3

sequence = 'GAACTCCAAAAATGAAAACATAGTAGCAATCAAAGCATCCCACTATTTTTTGTCTCTCGTTTCATTAGCGTTGTAAATTACTGATACCCTACTATACCTCTACAAGGCCTTTGTCATCTTTTTACTCAAGTGTGAAATCATCACTTATTGTATGAAGGATGAGCTTTCCGTTCGCTAGTTTGCTGAAAAGGCCTTCTGCAATAAGCTCTCTATTATCTTTAAAAAAACCTGGTTCCTGGTCTTCCATTCTGCTAAAAGCTGTAGGGGTTTTATCACGAGATTCCCGTTGGCATTCTGACTTATTAAAAATGCTTACAGAAGAAATGGATTCTTTAAATGGTCAAATTAATACGTGGACAGATAATAATCCTTTATTAGATGAAATTACGAAGCCATACAGAAAATCTTCAACTCGTTTTTTTCATCCGCTTCTTGTACTTCTAATGTCTAGAGCATCAGTAAATGGGGATCCACCGAGTCAGCAACTATTTCAAAGGTACAAACAACTTGCCCGTGTAACAGAATTGATTCATGCTGCCAATATAATTCATATTAATATTGGAGAAGAACAAAGCAACGAACAGATTAAACTTGCAACGTTGGTTGGAGATTATTTACTCGGAAAGGCGTCTGTTGATTTAGCACATTTAGAAAACAACGCTATTACAGAAATTATGGCTTCTGTTATTGCAAACTTAGTTGAAGGGCACTTCGGAAGCCGACAAAATGGCTCTGTTGGTTTGTCAAACGAACGAACCATCCTTCTGCAATCAGCCTTTATGCCAGCAAAGGCATGTTTATGCGCAAGCATATTGAATAACTCATCACAATACATTAATGATGCGTGTTTCAATTATGGAAAATTTCTAGGCTTATCGCTGCAACTGGCCCATAAGCCTGTATCTCCTGACGCCCAAGTTTTGCAAAAGAATAATGACATTTTGAAAACATATGTTGAGAATGCCAAGAGCTCATTGTCTGTTTTCCCCGATATAGAGGCTAAGCAAGCTCTCATGGAAATCGCTAATAGTGTTTCGAAGTAATCGACAGGTATTGTATCCTGGATTAATATTAGGGTGGCTCATGCATGCTCGTGCAATCGTAACAAATATGTCTTTCTTTTACGAATTTTAACGCTTCAATATAAATCATATTTTTCCTCA'

nucleotides = set(sequence)

#nucleotides = set(input('Enter your sequence:'))

nt_count = {}
for nt in nucleotides:
  count = sequence.count(nt)
  nt_count[nt] = count  
  print(nt, count)
print(nt_count)

GC_content = round((int(nt_count['G']) + int(nt_count['C']))/len(sequence),2)
print('GC content is: {}'.format(GC_content))
