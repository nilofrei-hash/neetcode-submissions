class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        End = []

        for i in strs:
            End.append(("".join(sorted(i)), i))

        End.sort()

        if not End:
            return []

        Resultat = [[End[0][1]]]

        for i in range(1, len(End)):
            if End[i - 1][0] == End[i][0]:
                Resultat[-1].append(End[i][1])
            else:
                Resultat.append([End[i][1]])

        return Resultat