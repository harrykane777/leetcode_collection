class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        p_dict = {}
        search = ""
        search += searchWord[0]
        i = 0
        p_dict[searchWord[0]] = []
        for product in products:
            if product[0] == searchWord[0]:
                p_dict[searchWord[0]].append(product)
        p_dict[searchWord[0]].sort()
        i = 1
        for s in searchWord[1:]:
            search += s 
            p_dict[search] = []
            for word in p_dict[search[:-1]]:
                if len(word) > i and word[i] == s:
                    p_dict[search].append(word)
            i += 1
        
        print(p_dict)
        result = []
        for key in p_dict.keys():
            if len(p_dict[key]) >= 3:
                result.append(p_dict[key][0:3])
            else:
                result.append(p_dict[key][0:(len(p_dict[key]))])
        return result
soln = Solution()
print(soln.suggestedProducts(["havana"], "havana"))