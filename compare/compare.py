# %%
import matplotlib.pyplot as plt
import compare_utils as utils
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# %% [markdown]
# Download and prepare data

# %%
# !wget http://data.statmt.org/wmt19/translation-task/kazakhtv.kk-en.tsv.gz
# !gunzip kazakhtv.kk-en.tsv.gz

# %%
# !wget http://data.statmt.org/wmt19/translation-task/crawl.2019-06.tsv.gz
# !gunzip crawl.2019-06.tsv.gz

# https://drive.google.com/drive/folders/0B3f-xwS1hRdDM2VpZXRVblRRUmM?usp=sharing

#%%
# !cat ../corpus/*.tsv > corpus.tsv

# %%
!cut crawl.2019-06.tsv -f 1 > crawl_kaz.txt
!cut crawl.2019-06.tsv -f 2 > crawl_eng.txt
!cut crawl.2019-06.tsv -f 3 > crawl_scores.txt

!sacremoses -j 4 normalize < crawl_kaz.txt > crawl_kaz_norm.txt
!sed '/^$/d' crawl_kaz_norm.txt > crawl_kaz_norm2.txt
!sacremoses -j 4 tokenize -x < crawl_kaz_norm2.txt > crawl_kaz_tok.txt
!mv crawl_kaz_tok.txt crawl_kaz.txt
!rm crawl_kaz_norm.txt crawl_kaz_norm2.txt

!sacremoses -j 4 normalize < crawl_eng.txt > crawl_eng_norm.txt
!sed '/^$/d' crawl_eng_norm.txt > crawl_eng_norm2.txt
!sacremoses -j 4 tokenize -x < crawl_eng_norm2.txt > crawl_eng_tok.txt
!mv crawl_eng_tok.txt crawl_eng.txt
!rm crawl_eng_norm.txt crawl_eng_norm2.txt

# %%
!cut kazakhtv.kk-en.tsv -f 1 > kazakhtv_kaz.txt
!cut kazakhtv.kk-en.tsv -f 2 > kazakhtv_eng.txt
!cut kazakhtv.kk-en.tsv -f 3 > kazakhtv_scores.txt

!sacremoses -j 4 normalize < kazakhtv_kaz.txt > kazakhtv_kaz_norm.txt
!sed '/^$/d' kazakhtv_kaz_norm.txt > kazakhtv_kaz_norm2.txt
!sacremoses -j 4 tokenize -x < kazakhtv_kaz_norm2.txt > kazakhtv_kaz_tok.txt
!mv kazakhtv_kaz_tok.txt kazakhtv_kaz.txt
!rm kazakhtv_kaz_norm.txt kazakhtv_kaz_norm2.txt

!sacremoses -j 4 normalize < kazakhtv_eng.txt > kazakhtv_eng_norm.txt
!sed '/^$/d' kazakhtv_eng_norm.txt > kazakhtv_eng_norm2.txt
!sacremoses -j 4 tokenize < kazakhtv_eng_norm2.txt > kazakhtv_eng_tok.txt
!mv kazakhtv_eng_tok.txt kazakhtv_eng.txt
!rm kazakhtv_eng_norm.txt kazakhtv_eng_norm2.txt

#%%
!cut KEKC.tsv -f 1 > old_corpus_kaz.txt
!cut KEKC.tsv -f 2 > old_corpus_eng.txt

#%%
!cut corpus.tsv -f 1 > corpus_kaz.txt
!cut corpus.tsv -f 2 > corpus_eng.txt
!cut corpus.tsv -f 3 > corpus_scores.txt

# %% [markdown]
# Compare number of unique sentence pairs


# %%
def compare_unique_pairs():
    crawl_len = !cat crawl.2019-06.tsv | sort | uniq | wc -l
    kazakhtv_len = !cat kazakhtv.kk-en.tsv | sort | uniq | wc -l
    old_corpus_len = !cat KEKC.tsv | sort | uniq | wc -l
    corpus_len = !cat corpus.tsv | sort | uniq | wc -l

    print("crawl size:\t", int(crawl_len[0]))
    print("kazakhtv size:\t", int(kazakhtv_len[0]))
    print("old_corpus size:", int(old_corpus_len[0]))
    print("corpus size:\t", int(corpus_len[0]))

    names = ["crawl", "kazakhtv", "old_corpus", "corpus"]
    sizes = [
        int(crawl_len[0]),
        int(kazakhtv_len[0]),
        int(old_corpus_len[0]),
        int(corpus_len[0])
    ]

    plt.bar(x=names, height=sizes)
    plt.show()


compare_unique_pairs()

# %% [markdown]
# Read data from files

# %%
crawl_kaz = utils.read_text_from_file_with_lower(file_name="crawl_kaz.txt")
crawl_eng = utils.read_text_from_file_with_lower(file_name="crawl_eng.txt")
crawl_scores = utils.read_floats_from_file(file_name="crawl_scores.txt")

kazakhtv_kaz = utils.read_text_from_file_with_lower(file_name="kazakhtv_kaz.txt")
kazakhtv_eng = utils.read_text_from_file_with_lower(file_name="kazakhtv_eng.txt")
kazakhtv_scores = utils.read_floats_from_file(file_name="kazakhtv_scores.txt")

old_corpus_kaz = utils.read_text_from_file_with_lower(file_name="old_corpus_kaz.txt")
old_corpus_eng = utils.read_text_from_file_with_lower(file_name="old_corpus_eng.txt")

corpus_kaz = utils.read_text_from_file_with_lower(file_name="corpus_kaz.txt")
corpus_eng = utils.read_text_from_file_with_lower(file_name="corpus_eng.txt")
corpus_scores = utils.read_floats_from_file(file_name="corpus_scores.txt")

# %% [markdown]
# Compare number of tokens in each language


# %%
def compare_number_of_tokens():
    crawl_kaz_tok_num = utils.count_tokens(texts=crawl_kaz)
    crawl_eng_tok_num = utils.count_tokens(texts=crawl_eng)

    kazakhtv_kaz_tok_num = utils.count_tokens(texts=kazakhtv_kaz)
    kazakhtv_eng_tok_num = utils.count_tokens(texts=kazakhtv_eng)

    old_corpus_kaz_tok_num = utils.count_tokens(texts=old_corpus_kaz)
    old_corpus_eng_tok_num = utils.count_tokens(texts=old_corpus_eng)

    corpus_kaz_tok_num = utils.count_tokens(texts=corpus_kaz)
    corpus_eng_tok_num = utils.count_tokens(texts=corpus_eng)

    names = ["crawl", "kazakhtv", "old_corpus", "corpus"]
    sizes_kaz = [
        crawl_kaz_tok_num,
        kazakhtv_kaz_tok_num,
        old_corpus_kaz_tok_num,
        corpus_kaz_tok_num
    ]
    sizes_eng = [
        crawl_eng_tok_num,
        kazakhtv_eng_tok_num,
        old_corpus_eng_tok_num,
        corpus_eng_tok_num
    ]

    for item in zip(names, sizes_kaz, sizes_eng):
        print(
            item[0], ": Kazakh tokens:", item[1], "English tokens:", item[2]
        )

    ind = np.arange(len(names))
    width = 0.35
    fig, ax = plt.subplots()
    rects1 = ax.bar(
        x=ind - width/2, height=sizes_kaz, width=width, label="kaz tokens"
    )
    rects2 = ax.bar(
        x=ind + width/2, height=sizes_eng, width=width, label="eng tokens"
    )
    ax.set_xticks(ind)
    ax.set_xticklabels(names)
    ax.legend()
    plt.grid(b=True, axis="y")
    plt.show()


compare_number_of_tokens()

# %% [markdown]
# Analyse and compare hunalign scores


# %%
def compare_hunalign_scores():
    print("Hunalign scores analysis for crawl.2019-06 corpus:")
    utils.analyze_scores(file_name="crawl_scores.txt")

    print("Hunalign scores analysis for kazakhtv corpus:")
    utils.analyze_scores(file_name="kazakhtv_scores.txt")

    print("Hunalign scores analysis for new corpus:")
    utils.analyze_scores(file_name="corpus_scores.txt")


compare_hunalign_scores()

# %% [markdown]
# Analyse and compare sentence lengths


# %%
def compare_sentence_lengths():
    crawl_kaz_sen_lens = [len(line) for line in crawl_kaz]
    crawl_eng_sen_lens = [len(line) for line in crawl_eng]

    kazakhtv_kaz_sen_lens = [len(line) for line in kazakhtv_kaz]
    kazakhtv_eng_sen_lens = [len(line) for line in kazakhtv_eng]

    old_corpus_kaz_sen_lens = [len(line) for line in old_corpus_kaz]
    old_corpus_eng_sen_lens = [len(line) for line in old_corpus_eng]

    corpus_kaz_sen_lens = [len(line) for line in corpus_kaz]
    corpus_eng_sen_lens = [len(line) for line in corpus_eng]

    print("Sentense lengths analysis for crawl.2019-06 corpus (kazakh side):")
    utils.analyze_sen_lens(lens=crawl_kaz_sen_lens)

    print("Sentense lengths analysis for kazakhtv corpus (kazakh side):")
    utils.analyze_sen_lens(lens=kazakhtv_kaz_sen_lens)

    print("Sentense lengths analysis for old corpus (kazakh side):")
    utils.analyze_sen_lens(lens=old_corpus_kaz_sen_lens)

    print("Sentense lengths analysis for new corpus (kazakh side):")
    utils.analyze_sen_lens(lens=corpus_kaz_sen_lens)

    print("Sentense lengths analysis for crawl.2019-06 corpus (english side):")
    utils.analyze_sen_lens(lens=crawl_eng_sen_lens)

    print("Sentense lengths analysis for kazakhtv corpus (english side):")
    utils.analyze_sen_lens(lens=kazakhtv_eng_sen_lens)

    print("Sentense lengths analysis for old corpus (english side):")
    utils.analyze_sen_lens(lens=old_corpus_eng_sen_lens)

    print("Sentense lengths analysis for new corpus (english side):")
    utils.analyze_sen_lens(lens=corpus_eng_sen_lens)


compare_sentence_lengths()

# %% [markdown]
# Analyse and compare words


# %%
def analyze_tokens_with_tf_idf():
    print("Kazakh side of corpora.")
    print()
    tf_idf_vectorizer = TfidfVectorizer(max_features=20)

    print("crawl_kaz:")
    model = tf_idf_vectorizer.fit(raw_documents=crawl_kaz)
    print("20 most common tokens:")
    print(model.get_feature_names())
    print()

    print("kazakhtv_kaz:")
    model = tf_idf_vectorizer.fit(raw_documents=kazakhtv_kaz)
    print("20 most common tokens:")
    print(model.get_feature_names())
    print()

    print("old_corpus_kaz:")
    model = tf_idf_vectorizer.fit(raw_documents=old_corpus_kaz)
    print("20 most common tokens:")
    print(model.get_feature_names())
    print()

    print("corpus_kaz:")
    model = tf_idf_vectorizer.fit(raw_documents=corpus_kaz)
    print("20 most common tokens:")
    print(model.get_feature_names())
    print()

    print("English side of corpora.")
    print()
    tf_idf_vectorizer = TfidfVectorizer(max_features=20, stop_words="english")

    print("crawl_eng:")
    model = tf_idf_vectorizer.fit(raw_documents=crawl_eng)
    print("20 most common tokens:")
    print(model.get_feature_names())
    print()

    print("kazakhtv_eng:")
    model = tf_idf_vectorizer.fit(raw_documents=kazakhtv_eng)
    print("20 most common tokens:")
    print(model.get_feature_names())
    print()

    print("old_corpus_eng:")
    model = tf_idf_vectorizer.fit(raw_documents=old_corpus_eng)
    print("20 most common tokens:")
    print(model.get_feature_names())
    print()

    print("corpus_eng:")
    model = tf_idf_vectorizer.fit(raw_documents=corpus_eng)
    print("20 most common tokens:")
    print(model.get_feature_names())
    print()


analyze_tokens_with_tf_idf()

# %% [markdown]
# Analyse and compare chars

# %%
print("Kazakh side of corpora.")
print()
print("crawl_kaz:")
utils.analyze_chars(text=crawl_kaz, n_chars_to_print=None)
print()
print("kazakhtv_kaz:")
utils.analyze_chars(text=kazakhtv_kaz, n_chars_to_print=None)
print()
print("old_corpus_kaz:")
utils.analyze_chars(text=old_corpus_kaz, n_chars_to_print=None)
print()
print("corpus_kaz:")
utils.analyze_chars(text=corpus_kaz, n_chars_to_print=None)


# %%
