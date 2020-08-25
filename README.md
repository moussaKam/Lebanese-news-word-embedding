# Lebanon News Embeddings Explorer
Web application developed using flask to explore the word embeddings trained on the lebanes news. <br><br>

This website has 3 different tools: <br>
### 1-Word analogies: 
This tool compares the relationship between two pairs of words.  For instance, giving 3 words A, B and C, the fourth word D will be found in a way that relation between A and B will be same as between C and D (B - A = D - C). To do so, the tool finds the top 10 similar words to B - A + C. <br><br>
### 2-Similarity score:
This tool finds the cosine similarity score between 2 words.<br><br>
### 3-Top similar words:
this tool finds the top 10 closest words of the input according to the similarity score between the vectors.
