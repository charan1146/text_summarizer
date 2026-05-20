import streamlit as st
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

from collections import defaultdict

# Download nltk data
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Page settings
st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📝"
)

# Title
st.title("AI Text Summarizer")

# Description
st.write("Generate short summaries from long text.")

# User input
text = st.text_area("Enter your paragraph:")

# Summarize button
if st.button("Generate Summary"):

    # Stopwords
    stop_words = set(stopwords.words("english"))

    # Tokenize words
    words = word_tokenize(text.lower())

    # Word frequency
    freq = defaultdict(int)

    for word in words:

        if word.isalnum() and word not in stop_words:
            freq[word] += 1

    # Tokenize sentences
    sentences = sent_tokenize(text)

    # Sentence scores
    sentence_scores = defaultdict(int)

    for sentence in sentences:

        for word in word_tokenize(sentence.lower()):

            if word in freq:
                sentence_scores[sentence] += freq[word]

    # Generate summary
    summary_sentences = sorted(
        sentence_scores,
        key=sentence_scores.get,
        reverse=True
    )[:2]

    summary = " ".join(summary_sentences)

    # Display summary
    st.subheader("Summary")

    st.write(summary)

# Footer
st.write("---")
st.caption("Developed using Python, Streamlit, and NLP")