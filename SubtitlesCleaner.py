import SubtitlesClient
import re
import nltk
import contractions
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

def get_unique_words_from_subtitles(data):
    lines = get_lines_from_subtitles(data)
    lemmatized_lines = lemmatize_lines(lines)
    unique_words = remove_duplicates(lemmatized_lines)
    unique_words = remove_single_character_words(unique_words)
    return unique_words

def clean_subtitle_line(line):
    # Remove HTML tags, special characters, and timestamps
    regex = r"<\w>|<\/\w>|[^a-zA-Z\s\'\.]|(\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3})"

    line = re.sub(regex, '', line)
    line = line.replace('.', ' ') 
    
    return line

def get_lines_from_subtitles(data):
    lines = []
    for line in data:
        cleaned_line = clean_subtitle_line(line) # Clean the subtitle line
        cleaned_line = cleaned_line.strip() # Remove leading and trailing whitespace

        if cleaned_line != "":
            lines.append(cleaned_line) # Add the line to the list if it's not empty

    return lines

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return 'a'
    elif tag.startswith('V'):
        return 'v'
    elif tag.startswith('N'):
        return 'n'
    elif tag.startswith('R'):
        return 'r'
    else:
        return 'n'

def lemmatize_lines(lines):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
   
    lemmatized_lines = []
    for line in lines:
        line = contractions.fix(line) # Expand contractions
        tokens = word_tokenize(line.lower())
       
        filtered_tokens = [word for word in tokens if word not in stop_words] # Remove stop words
        tagged_tokens = pos_tag(filtered_tokens) 
        lemmatized_line = []
        for word, tag in tagged_tokens:
                lemmatized_line.append(lemmatizer.lemmatize(word, get_wordnet_pos(tag)))
        lemmatized_lines.append(lemmatized_line)
    return lemmatized_lines

def remove_single_character_words(words):
    filtered = set()
    for word in words:
        if len(word) > 1:
            filtered.add(word)
    return filtered

def remove_duplicates(lines):
    seen = set()
    
    for line in lines:
        for word in line:
                seen.add(word)
    return seen




    

    


