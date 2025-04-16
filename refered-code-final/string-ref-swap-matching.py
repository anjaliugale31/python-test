# Write a program to find the given sentence are exact match 
# Even word swap it should be exact map 

# Kpmg India private limited
# Kpmg private India limited
# Limited private Kpng India

def are_sentence_match(referance, sentence):
    ref_wors=referance.lower().split()
    print("-->",sorted(ref_wors))
    sentence_word=sentence.lower().split()
    return sorted(ref_wors)==sorted(sentence_word)

referance='Kpmg India private limited'

sentences = [
   "Kpmg private India limited",
    "Limited private Kpmg India" 
]

for i, sentence in enumerate(sentences,start=1):
    result=are_sentence_match(referance,sentence)
    print(f"Sentence {i}:{'Match' if result else 'Not a Match'}")