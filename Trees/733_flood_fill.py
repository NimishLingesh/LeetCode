# Checked the solution

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        color = image[sr][sc]
        ROW = len(image)
        COL = len(image[0])
        visited = set()
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        def dfs(r, c, color):
            
            image[r][c] = newColor
            visited.add((r,c))
            for row, col in directions:
                new_row =r+row
                new_col = c+col
                if (0<=new_row<ROW and 0<=new_col<COL and (new_row, new_col) not in visited and 
                   image[new_row][new_col] == color
                   ):
                    dfs(new_row, new_col, color)
            

        dfs(sr, sc, color) 
        return image

# C++ method
# class Solution {
#     public int[][] floodFill(int[][] image, int sr, int sc, int color) {
#         int[][]vst = new int[image.length][image[0].length];
#         int s = image[sr][sc];
#        recursive(image,sr,sc,color,vst,s);
#         image[sr][sc] = color;
#         return image;
#     }
#     void recursive(int[][]image , int i,int j,int color,int[][]vst,int s){
#         if(i>=image.length || i<0 || j>=image[0].length || j<0 || (image[i][j]!=s) || vst[i][j]==1)return;
#         vst[i][j] = 1;
#         image[i][j] = color;
#         recursive(image,i+1,j,color,vst,s);
#         recursive(image,i,j+1,color,vst,s);
#         recursive(image,i-1,j,color,vst,s);
#         recursive(image,i,j-1,color,vst,s);
#     }
# }