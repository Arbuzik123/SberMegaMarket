import regex as re
def similarity_percentage(str1, str2):
    def extract_words(s):
        return re.findall(r'\w+', s)
    words1 = set(extract_words(str1))
    words2 = set(extract_words(str2))
    common_words = words1.intersection(words2)
    total_words = len(words1) + len(words2)
    similarity = len(common_words) / total_words
    return similarity * 100