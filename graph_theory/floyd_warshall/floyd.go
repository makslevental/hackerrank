package main
import "fmt"
func min(a, b int) int {
    if a <= b {
        return a
    }
    return b
}

func main() {
    
    var n,m int
    fmt.Scanf("%v %v\n", &n, &m)
    edges := make([][]int, n+1)

    for i := 0; i <= n ; i++ {
        edges[i] = make([]int, n+1) 
            for j := 0; j <= n; j++ {
                if i == j {
                    edges[i][j] = 0
                } else {
                    edges[i][j] = 999999999999
                }
        }
    }

    var u,v,r int

    for i := 0; i < m  ; i++ {
        fmt.Scanf("%v %v %v\n", &u, &v, &r)
        edges[u][v] = r
    }


    for k := 1; k <= n  ; k++ {
        for i := 1; i <= n  ; i++ {
            for j := 1; j <= n  ; j++ {
                edges[i][j] = min(edges[i][k]+edges[k][j],edges[i][j])
            }
        }
    }

    var q,x,y int
    fmt.Scanf("%v\n", &q)


    for i := 0; i < q; i++ {
        fmt.Scanf("%v %v\n", &x, &y)
        if edges[x][y] == 999999999999 {
            fmt.Println("-1")       
        } else {
            fmt.Println(edges[x][y])
        }

    }
}
