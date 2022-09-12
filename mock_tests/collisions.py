class Solution:
    def collisions(mat):
        rows = len(mat)
        cols = len(mat[0])
        # 1. A move right, B move left - till the edges
        # collision - dust
        total_trucks = {}
        for i in mat[0]:
            total_trucks[i] = 2

        while len(total_trucks) !=0:
            for r_idx, row in enumerate(rows):
                for c_idx, ele in mat[r_idx]:
                    if ele == "A":
                        a_truck = c_idx
                        mat[r_idx][a_truck] = "o"
                    if ele == "B":
                        b_truck = c_idx
                        mat[r_idx][b_truck] = "o"
                if a_truck < rows-1:
                    # if mat[r_idx][a_truck + 1] == "x":
                    mat[r_idx][a_truck + 1] = "A"
                else:
                    total_trucks[r_idx] -= 1
                    if total_trucks[r_idx] == 0:
                        total_trucks.pop(r_idx)
                if b_truck > 0:
                    # check for the collision
                    if mat[r_idx][b_truck - 1] == "A":
                        mat[r_idx][b_truck] = "x"
                        mat[r_idx][b_truck - 2] = "x"
                        mat[r_idx][b_truck - 1] = "x"
                        mat[r_idx - 1][b_truck] = "x"
                        mat[r_idx - 1][b_truck - 2] = "x"
                        mat[r_idx - 1][b_truck - 1] = "x"
                        mat[r_idx + 1][b_truck] = "x"
                        mat[r_idx + 1][b_truck - 2] = "x"
                        mat[r_idx + 1][b_truck - 1] = "x"
                    else:
                        mat[r_idx][b_truck - 1] = "B"
                else:
                    total_trucks[r_idx] -= 1
                    if total_trucks[r_idx] == 0:
                        total_trucks.pop(r_idx)

        return mat
                

sol = Solution()
sol.collisions()