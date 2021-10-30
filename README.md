# TAC

Course material for "Traitement automatique de corpus" ([STIC-B545](https://www.ulb.be/fr/programme/stic-b545)) taught at [ULB](https://ulb.be).

Caution: Python 3.6 or higher required to handle [f-strings](https://www.python.org/dev/peps/pep-0498/) (3.9 or even 3.10 is better).

There are two ways to run this code:

## Recommended: Docker

- Install Docker: <https://docs.docker.com/get-docker/>
- Start Docker

```bash
git clone git@github.com:madewild/tac.git
cd tac
docker-compose build
docker-compose up
```

Then everything will be available here: <http://localhost:8888/lab>

In that way you can use the Jupyter notebooks (`\*.ipynb` files) at the root of each module and ignore the raw scripts.

## Traditional Pythonic way

It is recommended to run this code in a virtual environment:

```bash
git clone git@github.com:madewild/tac.git
cd tac
virtualenv venv --python=python3
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python -m spacy download fr_core_news_md
```

In that way you can use the scripts `\*.py` (in the subdirectory `raw_scripts` of each module).
They should be executed from the root of this repository.

## Module 1

`s1_sql`: querying a simple relational database

`s2_sparql`: querying the Wikidata SPARQL endpoint

`s3_api`: playing with OpenStreetMap and EUcountries APIs

`s4_scrape`: scraping the AVB to retrieve 2833 PDF bulletins

## Module 2

`s1_convert`: script to convert PDFs to TXTs, move them to dedicated folder and aggregate them in single big text file

`s2_explore`: playing with various categories (city, year, decade, type...)

`s3_freq`: basic frequency analysis, hapaxes, long words...

## Module 3

### Keyword extraction

`s1_keyword`: using YAKE to extract French keywords in each text file

`s2_wordcloud`: generating a wordcloud for a given year (calling `filtering.py` in the background)

### Named-entity recognition

Install SpaCy from requirements then run this command to download French model: `python -m spacy download fr_core_news_sm`

`s3_ner`: perform NER with SpaCy FR model

### Sentiment analysis

`s4_sentiment`: analyse positive/negative sentences with textblob

## Module 4

`s1_classification`: supervised classification of 20 newsgroups

`s2_clustering`: unsupervised clustering with k-means

`s3_sentence_tokenizer`: split big text into sentences

`s4_word_embeddings`: train and explore a word2vec model on corpus

## Module 5

`s1_language_detection`: language identification with langid

`s2_anonymization`: de-identification of data with Faker

## Module 6

`s1_extraction`: extract text from various file types
