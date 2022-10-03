class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # checked for the answer
        # the idea is to put all characters in the same group if they are equal
    # in order to do that, we can use Disjoint Set Union (dsu) aka Union Find
    # for dsu tutorial, please check out https://wingkwong.github.io/leetcode-the-hard-way/tutorials/graph-theory/disjoint-set-union
    def equationsPossible(self, equations: List[str]) -> bool:
        # find the root of node x. 
        # here we are not using parent[x] 
        # because it may not contain the updated value of the connected component that x belongs to. 
        # Therefore, we walk the ancestors of the vertex until we reach the root.
        def find(x):
            # with path compress
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
            # without path compression
            #return x if parent[x] == x else find(parent[x])
        # at the beginning, put each character in its own group
        # so we will have 26 groups with one character each
        # i.e. 'a' in group 0, 'b' in group 1, ..., 'z' in group 25
        parent = [i for i in range(26)]
        for e in equations:
            if e[1] == '=':
                # e.g. a == b
                # then we group them together
                # how? we use `find` function to find out the parent group of the target character index
                # then update parent. a & b would be in group 1 (i.e. a merged into the group where b belongs to)
                # or you can also do `parent[find(ord(e[3]) - ord('a'))] = find(ord(e[0]) - ord('a'))`
                # i.e. b merged into the group where a belongs to
                parent[find(ord(e[0]) - ord('a'))] = find(ord(e[3]) - ord('a'))
        # handle != case
        for e in equations:
            # if two characters are not equal
            # then which means their parent must not be equal
            if e[1] == '!' and find(ord(e[0]) - ord('a')) == find(ord(e[3]) - ord('a')):
                return False
        return True

        
        # Approached, but could be incorrect
        """case1 = 0
        case2 = 0
        case3 = 0
        dic = {}
        for eq in equations:
            term1 = eq[0]
            term2 = eq[-1]

            t1_present = 0
            t2_present = 0
            if term1 in dic.keys():
                locals()[term1] = dic[term1]
                t1_present = 1
            else:
                locals()[term1] = 1

            if term2 in dic.keys():
                locals()[term2] = dic[term2]
                t2_present = 1
            else:
                locals()[term2] = 1
            
            if eval(eq):
                case1 += 1
            # locals()[term1] = 1
            # locals()[term2] = 1
            if not eval(eq):
                case1 += 1
            locals()[term1] = 1
            locals()[term2] = 2
            if not eval(eq):
                case2 += 1
            locals()[term1] = 2
            locals()[term2] = 1
            if not eval(eq):
                case3 += 1
        if case1 == 0 or case2 == 0 or case3 == 0:
            return True
        else:
            return False
    
    def cases(self, ):"""


sol = Solution()
equations = ["a==b","b!=a"]
print(sol.equationsPossible(equations))
