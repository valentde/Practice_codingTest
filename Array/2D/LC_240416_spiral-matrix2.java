// https://leetcode.com/problems/spiral-matrix-ii/
public class ch4_05_snailNumberSquare {
    public int[][] generateMatrix(int n) {
        int cnt=1, r=0, c=0, d=0, grid [][] = new int[n][n];
        int[][] dxdy = new int[][]{ {0,1}, {1,0}, {0,-1}, {-1,0}};

        if(n==1) return new int[][]{{1}};

        while(grid[r][c] == 0){
            grid[r][c] = cnt++;
            int nr=r+dxdy[d][0], nc=c+dxdy[d][1];
            if(nr<0 || nc<0 || nr>=n || nc>=n || grid[nr][nc]>0){
                d = (d + 1)%4;
                r=r+dxdy[d][0];
                c=c+dxdy[d][1];
                continue;
            }else {
                r = nr;
                c = nc;
            }
        }
        return grid;
    }
}