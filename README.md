# Lebanon News Embeddings Explorer <img src="/explorer/static/images/flagbtn" alt="logo" width="25" height="25" href='https://lebanesenewsembeddings.pythonanywhere.com/'>
Web application developed using flask to explore the word embeddings trained on the lebanese news. <br><br>
  Link to the web application: <a href='https://lebanesenewsembeddings.pythonanywhere.com/' size="+5" style="font-size: 150px;"><font size="+2">https://lebanesenewsembeddings.pythonanywhere.com/</font></a>
  
## word2vec
__word2vec__ is a technique in NLP that implements a neural network to embed words in a euclidean space. Hence, each word in the training corpus is mapped to a vector. This mapping allows the detection of synonyms and semantically related words, by computing the cosine similarity between their attributed vectors. Namely, similar words will be "close" in the euclidean space. <br>
Another interesting property is the ability of this technqiue to produce vectors that reflect analogies in natural language. For example, "king" is for "man" as "queen" is for "woman", then the nearest neighbor to vector('king') - vector('man') + vector('woman') would be the vector('queen'). <br>

This website has 3 different tools: <br>
### 1-Word analogies: 
This tool compares the relationship between two pairs of words.  For instance, giving 3 words A, B and C, the fourth word D will be found in a way that relation between A and B will be same as between C and D (B - A = D - C). To do so, the tool finds the top 10 similar words to B - A + C. <br><br>
![analogy](/explorer/images/analogy.png)
### 2-Similarity score:
This tool finds the cosine similarity score between 2 words.<br><br>
![similarity score](/explorer/images/sim-score.png)
### 3-Top similar words:
this tool finds the top 10 closest words of the input according to the similarity score between the vectors.
![most similar](/explorer/images/most-similar.png)
<br><br>
## To use locally:
1-Clone the repository.<br>
2-Download the word vectors file <a href="https://drive.google.com/file/d/1TQO30Q396XMOx3nDOp6f4CfQuksYgjXF/view?usp=sharing">here</a> and place it in a folder called models.<br>
3-Place the cloned repository and the folder "models" in the same path.<br>
4-Run "run.py" in the explorer folder using python3
