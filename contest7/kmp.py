def compute_lps(p):
    m = len(p)
    lps = [0] * m

    length = 0
    i = 1

    while i < m:
        if p[i] == p[length]:
            length += 1
            lps[i] = length
            i += 1

        elif length != 0:
            length = lps[length - 1]

        else:
            lps[i] = 0
            i += 1

    return lps


def kmp(text, pattern):
    if not pattern:
        return list(range(len(text) + 1))

    n = len(text)
    m = len(pattern)

    lps = compute_lps(pattern)
    matches = []

    i = 0  # Índice no texto
    j = 0  # Índice no padrão

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            matches.append(i - j)
            j = lps[j - 1]

        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches