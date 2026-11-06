class Node:
    def __init__(self, depth=0, start=-1, suffix_index=None):
        self.children = {}
        self.depth = depth
        self.start = start
        self.suffix_index = suffix_index


def suffix_array(s):
    n = len(s)
    sa = list(range(n))
    rank = [ord(c) for c in s]
    k = 1

    while k < n:
        
        sa.sort(key=lambda i: (
            rank[i],
            rank[i + k] if i + k < n else -1
        ))

        new_rank = [0] * n

        for j in range(1, n):
            a, b = sa[j - 1], sa[j]

            par_a = (
                rank[a],
                rank[a + k] if a + k < n else -1
            )
            par_b = (
                rank[b],
                rank[b + k] if b + k < n else -1
            )

            new_rank[b] = new_rank[a] + (par_a != par_b)

        rank = new_rank

        if rank[sa[-1]] == n - 1:
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
    total = 0
    stack = [root]

    while stack:
        parent = stack.pop()

        for child in parent.children.values():
            comprimento = child.depth - parent.depth

            # Desconsidera o terminador
            if child.suffix_index is not None:
                comprimento -= 1

            total += comprimento
            stack.append(child)

    return total



def main():
    n = int(input())
    entradas = []

    for _ in range(n):
        ent = input()
        entradas.append(ent)

    for p in entradas:
        root, texto  = suffix_tree(p)
        print(dfs(root))
        

        

if __name__ == "__main__":
    main()