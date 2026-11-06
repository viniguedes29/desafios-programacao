class Node:
    def __init__(self, depth=0, start=-1, suffix_index=None):
        self.children = {}
        self.depth = depth
        self.start = start
        self.suffix_index = suffix_index


def counting_sort(sa, rank, k, n, max_rank):
    # Ordenação sugerida no slide 
    count = [0] * (max_rank + 1)

    for i in sa:
        r = rank[i + k] if i + k < n else 0
        count[r] += 1

    total = 0
    for i in range(len(count)):
        count[i], total = total, total + count[i]

    result = [0] * n

    for i in sa:
        r = rank[i + k] if i + k < n else 0
        result[count[r]] = i
        count[r] += 1

    return result




def suffix_array(s):
    n = len(s)
    if n == 0:
        return []

    sa = list(range(n))

    caracteres = sorted(set(s))
    alphabet = {} #indices da order da string pra desempatar no counting sort.

    for i in range(len(caracteres)):
        c = caracteres[i]
        alphabet[c] = i + 1
    rank = [alphabet[c] for c in s]
    max_rank = len(alphabet)
    k = 1

    while k < n:
        sa = counting_sort(sa, rank, k, n, max_rank)
        sa = counting_sort(sa, rank, 0, n, max_rank)

        new_rank = [0] * n
        classes = 1

        for j in range(1, n):
            a, b = sa[j - 1], sa[j]

            par_a = (
                rank[a],
                rank[a + k] if a + k < n else 0
            )
            par_b = (
                rank[b],
                rank[b + k] if b + k < n else 0
            )

            if par_a != par_b:
                classes += 1

            new_rank[b] = classes - 1

        rank = [r + 1 for r in new_rank]
        max_rank = classes

        if classes == n:
            break

        k *= 2

    return sa


def lcp_array(s, sa):
    n = len(s)
    rank = [0] * n

    for j, i in enumerate(sa):
        rank[i] = j

    lcp = [0] * n
    h = 0

    for i in range(n):
        if rank[i] == 0:
            h = 0
            continue

        j = sa[rank[i] - 1]

        while (i + h < n and j + h < n
               and s[i + h] == s[j + h]):
            h += 1

        lcp[rank[i]] = h

        if h:
            h -= 1

    return lcp

def suffix_tree(s):
    s += "$"
    n = len(s)

    sa = suffix_array(s)
    lcp = lcp_array(s, sa)

    root = Node()
    stack = [root]

    for pos, i in enumerate(sa):
        common = lcp[pos]
        last = None

        # Volta até a profundidade compartilhada
        while stack[-1].depth > common:
            last = stack.pop()

        # Divide uma aresta, se necessário
        if stack[-1].depth < common:
            parent = stack[-1]

            split = Node(
                depth=common,
                start=last.start
            )

            parent.children[s[split.start]] = split

            last.start += common - parent.depth
            split.children[s[last.start]] = last

            stack.append(split)

        # Adiciona a folha do sufixo atual
        parent = stack[-1]

        leaf = Node(
            depth=n - i,
            start=i + common,
            suffix_index=i
        )

        parent.children[s[leaf.start]] = leaf
        stack.append(leaf)

    return root, s

def dfs(root):
    # DFS pra calcular o tamanho do ramo
    stack = [(root, False)]

    while stack:
        node, visited = stack.pop()

        if visited:
            if node.suffix_index is not None:
                node.count = 1
            else:
                node.count = sum(
                    child.count
                    for child in node.children.values()
                )
        else:
            stack.append((node, True))

            for child in node.children.values():
                stack.append((child, False))

    return root.count

def count_pattern(root, s, pattern):
    node = root
    i = 0

    while i < len(pattern):
        edge = node.children.get(pattern[i])

        if edge is None:
            return 0

        child = edge

        start = child.start
        end = start + child.depth - node.depth

        for j in range(start, end):
            if i == len(pattern):
                return child.count

            if s[j] != pattern[i]:
                return 0

            i += 1

        node = child

    return node.count


def main():
    s = input()
    n = int(input())
    entradas = []

    for _ in range(n):
        ent = input()
        entradas.append(ent)
    
    root, texto  = suffix_tree(s)
    dfs(root)

    for p in entradas:
        print(count_pattern(root, texto, p))
        
        

        

if __name__ == "__main__":
    main()