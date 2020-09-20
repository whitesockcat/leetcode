# 一排n个方块，现有3种颜色，要给这n个方块涂上颜色。要求：相邻方块颜色不同；第一个方块和最后一个方块颜色不同。

# f(1) = 3
# f(2) = 6
# f(3) = 6
# f(n) = f(n-1) + 2*f(n-2) n>=4

# 1、假设第n-1块的颜色和第1块不同，那前n-1个方块就是f(n-1)问题。由于第n块的颜色既不能和第n-1块颜色相同，也不能第1块相同，那么第n块只能选择剩下的那种颜色，唯一的一种选法。这时有f(n-1)种情况。

# 2、假设第n-1块的颜色和第1块是相同的，那知道第n-2块的颜色必定和第1块不同了，那前n-2个方块就是f(n-2)问题。此时，第n块有两种选择，只要颜色和第n-1块的颜色不同即可。这时有2*f(n-2)种情况。

# 上面两种情况综合起来，就得到了递推关系：  f(n) = f(n-1) + 2*f(n-2)