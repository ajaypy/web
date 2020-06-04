"""
in a list describing tree types, find the max number of N different types of
fruits that can be picked in

generic sliding window solution
as we iterate over the tree lists:
    1. reach a new tree but still within the limit
       just add the tree to list of current trees
       update the counts
    2. reach a new tree and limit of max number of trees
       update the max
       pop the first
       insert new in list of current
       update the counts
    3. reach the last element
    4. number of buckets is more than the actual number of different fruits
"""
def fruits_in_baskets(trees ,k):
    if len(trees) == 0 or k == 0:
        return 0

    print (trees)
    # pointers to the window
    l = 0
    r = 1
    # max values
    f_max = 1
    max_indexes = [0,0]
    # windows 
    cur_trees = [trees[0]]



    while r < len(trees):

        if trees[r] not in cur_trees:
            if len(cur_trees) == k:
                # with new tree
                # 1. update the max length
                if (r - l) > f_max:
                    f_max = (r - l)
                    max_indexes = [l,r-1]

                # 2. move the left window pointer
                #    the left pointer has to be moved from the right
                for i in range(r,l-1,-1):
                    if trees[i] == trees[l]:
                        l = i+1
                        break
                cur_trees.pop(0)
            cur_trees.append(trees[r])
        elif r == len(trees) - 1:
            if (r - l + 1) > f_max:
                f_max = (r - l +1)
                max_indexes = [l,r]
        r += 1
    if len(cur_trees) < k:
        return ([0,len(trees) - 1])
    return (max_indexes)





k = 2

trees = [[0,1,2,2]]
trees = [[3,3,3,1,2,1,1,2,3,3,4],[0,1,2,2],[1,2,3,2,2],[1,2,1],[7,7,7,7,7]]
for tree in trees:
    max_l,max_r = fruits_in_baskets(tree ,k)
    print (max_r+1, max_l, max_r+1 - max_l, tree[max_l:max_r+1])
    print ("------------------------- -------------------")
