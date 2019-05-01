import csv
import re

roots = []
meanings = []
words = []
c = ""

with open('C:/Users/Bryan/Desktop/root_words.txt', 'r') as f:
    c = f.read()

with open('C:/Users/Bryan/Desktop/root_words.txt', 'w') as f:
    c = re.sub('\t+', '\t', c)
    f.write(c)
    f.close

with open('C:/Users/Bryan/Desktop/root_words.txt', 'r') as f:
    reader = csv.reader(f, dialect='excel', delimiter='\t')
    for row in reader:
        roots.append(row[0].upper())
        meanings.append(', '.join(row[1].split(',')))
        words.append(', '.join(row[2].split(',')))
   
with open('C:/Users/Bryan/Desktop/root_output.txt', 'w') as f:
    for i in range(len(roots)):
        print(f"\\begin{{flashcard}}[Roots]{{{roots[i]}}}\n"
              f"{meanings[i]}\\\\\n"
              "\\vspace{0.2in}\n"
              f"{words[i]}\\\\\n"
              "\\end{flashcard}\n", file=f)

'''        
\begin{flashcard}[Root Word]{FRONT OF CARD}
meanings
\vspace{0.2in}
list,of,words
\end{flashcard}
'''