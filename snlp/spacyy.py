import time
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize, blankline_tokenize
import spacy
from flair.data import Sentence
from flair.tokenization import SegtokSentenceSplitter

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)


nlp = spacy.load("en_core_web_sm")


flair_splitter = SegtokSentenceSplitter()


text = """Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence. 
It is concerned with the interactions between computers and human language.

Challenges in natural language processing frequently involve speech recognition, natural language understanding, and natural language generation. 
Many different classes of machine learning algorithms have been applied to NLP tasks.

These algorithms take as input a large corpus of text and learn rules from them. 
This is a standard text block to test our tokenizers and check their execution times."""

def nltk_tokenization(text):
    start_time = time.time()
    
    words = word_tokenize(text)
    sentences = sent_tokenize(text)
    paragraphs = blankline_tokenize(text)
    
    end_time = time.time()
    return end_time - start_time, len(words), len(sentences), len(paragraphs)


def spacy_tokenization(text):
    start_time = time.time()
    
    doc = nlp(text)
    
    words = [token.text for token in doc]

    sentences = [sent.text for sent in doc.sents]
    paragraphs = text.split('\n\n')
    
    end_time = time.time()
    return end_time - start_time, len(words), len(sentences), len(paragraphs)

def flair_tokenization(text):
    start_time = time.time()
    
    sentences = flair_splitter.split(text)
    
    words = []
    for sent in sentences:
        words.extend([token.text for token in sent.tokens])
        
    paragraphs = text.split('\n\n')
    
    end_time = time.time()
    return end_time - start_time, len(words), len(sentences), len(paragraphs)

if __name__ == "__main__":
    print("Running Tokenization & Benchmarking...\n")
    print("-" * 50)
    
    nltk_time, nltk_w, nltk_s, nltk_p = nltk_tokenization(text)
    print(f"NLTK:\n Execution Time: {nltk_time:.5f} seconds")
    print(f" Counts -> Words: {nltk_w}, Sentences: {nltk_s}, Paragraphs: {nltk_p}\n")
    
    spacy_time, spacy_w, spacy_s, spacy_p = spacy_tokenization(text)
    print(f"SpaCy:\n Execution Time: {spacy_time:.5f} seconds")
    print(f" Counts -> Words: {spacy_w}, Sentences: {spacy_s}, Paragraphs: {spacy_p}\n")
    
    flair_time, flair_w, flair_s, flair_p = flair_tokenization(text)
    print(f"Flair:\n Execution Time: {flair_time:.5f} seconds")
    print(f" Counts -> Words: {flair_w}, Sentences: {flair_s}, Paragraphs: {flair_p}\n")
    
    print("-" * 50)
    print("Speed Comparison (Fastest to Slowest depends on system load):")
    print(f"1. NLTK Time:  {nltk_time:.5f}s")
    print(f"2. SpaCy Time: {spacy_time:.5f}s")
    print(f"3. Flair Time: {flair_time:.5f}s")