from django.shortcuts import render, redirect
from orm.views import save_new_project, get_similar_projects
from render_form.forms import ProjectDetailForm
from MatchRecord.settings import(
    MOCK_DB, MOCK_FORM_DATA, NON_SUBJECTIVE_KEYS, SIMILARITY_CUTOFF
)
import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import wordnet, stopwords


# Create your views here.
def nlp_view(request):

    # For actual form data coming from webpage
    if request.method == 'POST':
        post_data = request.POST.items()
        form = {k: v for k, v in post_data if k != 'csrfmiddlewaretoken'}
        similarity_data = filter_duplicates_by_similarities(form)
        if len(similarity_data):
            request.session['matches'] = similarity_data
            request.session['form_persistent_data'] = form
            return redirect('/')
        else:
            MOCK_DB.append(form)
            request.session['success'] = True
            return redirect('/')

    # For testing purposes
    elif request.method == 'GET':
        similarity_data = filter_duplicates_by_similarities(MOCK_FORM_DATA[0])


def filter_duplicates_by_similarities(form_data):
    form_tags = get_tagged_tokens(form_data)
    form_stems = get_stems(get_lemmas(form_tags))

    calculated_similarities = list()
    possible_duplicates = get_possible_duplicates(form_data)

    for duplicate in possible_duplicates:
        dup_tags = get_tagged_tokens(duplicate)
        dup_stems = get_stems(get_lemmas(dup_tags))
        similarity = round(calc_similarity(form_stems, dup_stems), 3)*100
        if similarity >= SIMILARITY_CUTOFF:
            obj = {'duplicate': duplicate, 'similarity_rating': similarity}
            calculated_similarities.append(obj)
    
    return calculated_similarities


def get_lemmas(tagged_tokens):
    lemmas = list()
    lemmatizer = WordNetLemmatizer()
    for word, tag in tagged_tokens:
        if tag is not None:
            lemmas.append(lemmatizer.lemmatize(word, tag))
    return lemmas


def get_stems(lemmas):
    stems = list()
    stemmer = PorterStemmer().stem
    for lemma in lemmas:
        stems.append(stemmer(lemma))
    return stems


def get_possible_duplicates(form_data):
    dups = list()
    for record in MOCK_DB:
        is_possible_match = True
        for key in NON_SUBJECTIVE_KEYS:
            if record[key] != form_data[key]:
                is_possible_match = False
        if is_possible_match:
            dups.append(record)
    return dups


# function to convert nltk tag to wordnet tag
def wordnet_tag(nltk_tag):
    meaningful_tags = {
        'J': wordnet.ADJ,
        'V': wordnet.VERB,
        'N': wordnet.NOUN,
    }
    return meaningful_tags.get(nltk_tag[0], None)


# remove words which do not contribute sufficient meaning to the text
def tokens_without_stop_words(tokens):
    custom_stops = ['project', 'purpose']
    words_to_remove = stopwords.words('english') + custom_stops
    return [tok for tok in tokens if tok not in words_to_remove]


def get_tagged_tokens(proj_dict):
    text = f"{proj_dict['project_description']} {proj_dict['project_name']}."
    tokens = [tok.lower() for tok in nltk.word_tokenize(text)]

    nltk_tags = nltk.pos_tag(tokens_without_stop_words(tokens)) 
    return map(lambda x: (x[0], wordnet_tag(x[1])), nltk_tags)


def calc_similarity(new_entry, old_entry, intersect_count=0):
    order_by_len = [new_entry, old_entry]

    len_diff = len(new_entry) - len(old_entry)
    if len_diff > 0:
        order_by_len.reverse()

    intersection = list()
    for stem in order_by_len[0]:
        if stem in order_by_len[1]:
            intersect_count += order_by_len[1].count(stem)
            intersection.append(stem)

    pure_intersect = list(dict.fromkeys(intersection))

    union_count = len(new_entry) + len(old_entry) - len(pure_intersect)

    return intersect_count/union_count
