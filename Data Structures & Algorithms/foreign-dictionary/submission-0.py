class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        dictionary = {}
        visiting = set()
        visited = set()
        res = []

        def buildDict(words):
            for word in words:
                for c in word:
                    if c not in dictionary:
                        dictionary[c] = set()
        buildDict(words)

        for i in range(len(words)-1):

            a = words[i]
            b = words[i+1]

            if len(a) > len(b) and a[:len(b)] == b:
                return ""

            for j in range(min(len(a), len(b))):

                if a[j] != b[j]:
                    dictionary[a[j]].add(b[j])
                    break

            
        def dfs(k):

            if k in visiting:
                return True

            if k in visited: 
                return False

            visiting.add(k)

            neighbors = dictionary[k]

            for neighbor in neighbors:
                cycle = dfs(neighbor)
                if cycle:
                    return True
            visiting.remove(k)
            visited.add(k)
            res.append(k)
            return False
        
        for k in dictionary.keys():
            cycle = dfs(k)
            if cycle:
                return ""


        return "".join(res[::-1])
