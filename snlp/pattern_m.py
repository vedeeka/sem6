

def build_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    lps = build_lps(pattern)
    i = j = 0
    result = []

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == len(pattern):
            result.append(i - j)
            j = lps[j - 1]

        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return result




def regex_match(text, regex):
    matches = []


    pattern = regex[1:-1]


    if '[' not in pattern:
        return kmp_search(text, pattern)


    inner = pattern[1:-1]


    if inner.startswith('^'):
        excluded = set(inner[1:])
        for i, ch in enumerate(text):
            if ch not in excluded:
                matches.append(i)
        return matches


    if '^' in inner:
        first, not_char = inner.split('^')
        for i in range(len(text) - 1):
            if text[i] == first and text[i + 1] != not_char:
                matches.append(i)
        return matches

    allowed = set(inner)
    for i, ch in enumerate(text):
        if ch in allowed:
            matches.append(i)

    return matches




sentence = input("Enter sentence: ")

patterns = ["/at/", "/[at]/", "/[a^t]/", "/[^at]/"]

for p in patterns:
    print(p, "→ matches at index:", regex_match(sentence, p))
