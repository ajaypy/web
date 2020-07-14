"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

https://leetcode.com/articles/longest-increasing-path-matrix/
"""

#1. DFS

dirs = [[0,1],[1,0],[0,-1],[-1,0]]
def dfs_dfs(matrix,m,n,i,j,res):
    ans = 0
    for d in dirs:
        x = i + d[0]
        y = j + d[i]

        if (x >= 0 and x < m and y >= 0 and y < n):
            if matrix[x][y] > matrix[i][j]:
                ans = max(ans,dfs_dfs(matrix,m,n,x,y)
    ans += 1
    return ans


def solution_dfs(matrix):
    m = len(matrix)
    if m == 0:
        return 0
    n = len(matrix[0])

    ans = 0

    for i in range(m):
        for j in range(j):
            ans = max(ans,dfs_dfs(matrix,m,n,i,j)




