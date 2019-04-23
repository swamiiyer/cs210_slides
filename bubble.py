import slideutils, sys

def trace1():
    B, Y, X = 'grape300', 'banana300', ''
    T, F = True, False
    A = [[('T', X, F), ('U', X, F), ('R', X, F), ('I', X, F), ('N', X, F), ('G', X, F)],
         [('T', X, F), ('U', X, F), ('R', X, F), ('I', X, F), ('N', Y, F), ('G', Y, F)],
         [('T', X, F), ('U', X, F), ('R', X, F), ('I', X, F), ('G', X, F), ('N', X, F)],
         [('T', X, F), ('U', X, F), ('R', X, F), ('I', Y, F), ('G', Y, F), ('N', X, F)],
         [('T', X, F), ('U', X, F), ('R', X, F), ('G', X, F), ('I', X, F), ('N', X, F)],
         [('T', X, F), ('U', X, F), ('R', Y, F), ('G', Y, F), ('I', X, F), ('N', X, F)],
         [('T', X, F), ('U', X, F), ('G', X, F), ('R', X, F), ('I', X, F), ('N', X, F)],
         [('T', X, F), ('U', Y, F), ('G', Y, F), ('R', X, F), ('I', X, F), ('N', X, F)],
         [('T', X, F), ('G', X, F), ('U', X, F), ('R', X, F), ('I', X, F), ('N', X, F)],
         [('T', Y, F), ('G', Y, F), ('U', X, F), ('R', X, F), ('I', X, F), ('N', X, F)],
         [('G', B, F), ('T', X, F), ('U', X, F), ('R', X, F), ('I', X, F), ('N', X, F)],
         [('G', B, F), ('T', X, F), ('U', X, F), ('R', X, F), ('I', Y, F), ('N', Y, F)],
         [('G', B, F), ('T', X, F), ('U', X, F), ('R', X, F), ('I', X, F), ('N', X, F)],
         [('G', B, F), ('T', X, F), ('U', X, F), ('R', Y, F), ('I', Y, F), ('N', X, F)],
         [('G', B, F), ('T', X, F), ('U', X, F), ('I', X, F), ('R', X, F), ('N', X, F)],
         [('G', B, F), ('T', X, F), ('U', Y, F), ('I', Y, F), ('R', X, F), ('N', X, F)],
         [('G', B, F), ('T', X, F), ('I', X, F), ('U', X, F), ('R', X, F), ('N', X, F)],
         [('G', B, F), ('T', Y, F), ('I', Y, F), ('U', X, F), ('R', X, F), ('N', X, F)],
         [('G', B, F), ('I', B, F), ('T', X, F), ('U', X, F), ('R', X, F), ('N', X, F)],
         [('G', B, F), ('I', B, F), ('T', X, F), ('U', X, F), ('R', Y, F), ('N', Y, F)],
         [('G', B, F), ('I', B, F), ('T', X, F), ('U', X, F), ('N', X, F), ('R', X, F)],
         [('G', B, F), ('I', B, F), ('T', X, F), ('U', Y, F), ('N', Y, F), ('R', X, F)],
         [('G', B, F), ('I', B, F), ('T', X, F), ('N', X, F), ('U', X, F), ('R', X, F)],
         [('G', B, F), ('I', B, F), ('T', Y, F), ('N', Y, F), ('U', X, F), ('R', X, F)],
         [('G', B, F), ('I', B, F), ('N', B, F), ('T', X, F), ('U', X, F), ('R', X, F)],
         [('G', B, F), ('I', B, F), ('N', B, F), ('T', X, F), ('U', Y, F), ('R', Y, F)],
         [('G', B, F), ('I', B, F), ('N', B, F), ('T', X, F), ('R', X, F), ('U', X, F)],
         [('G', B, F), ('I', B, F), ('N', B, F), ('T', Y, F), ('R', Y, F), ('U', X, F)],
         [('G', B, F), ('I', B, F), ('N', B, F), ('R', B, F), ('T', X, F), ('U', X, F)],
         [('G', B, F), ('I', B, F), ('N', B, F), ('R', B, F), ('T', Y, F), ('U', Y, F)],
         [('G', B, F), ('I', B, F), ('N', B, F), ('R', B, F), ('T', B, F), ('U', X, F)],
         [('G', B, F), ('I', B, F), ('N', B, F), ('R', B, F), ('T', B, F), ('U', B, F)],
         ]
    tex = '\\begin{overprint}\n'
    for i, a in enumerate(A):
        tex += '\onslide<%d|handout:%d>\n' %(i + 1, i + 1)
        tex += '\\begin{center}\n'
        tex += slideutils.trace(6, None, a)
        tex += '\end{center}\n'
    tex += '\end{overprint}\n'
    return tex

def trace2():
    B, Y, X = 'grape300', 'banana300', ''
    T, F = True, False
    CODE = """    public static void sort(Comparable[] a) {
        int n = a.length;
        for (int i = 0; i < n; i++) {
            for (int j = n - 1; j > i; j--) {
                if (less(a[j], a[j - 1])) {
                    exchange(a, j, j - 1);
                }
            }
        }
    }"""
    VARS = [('i', 1), ('j', 1), ('a', 6)]
    A = [[[], (' ', X, F), (' ', X, F), ('T', X, F), ('U', X, F), ('R', X, F), ('I', X, F), ('N', X, F), ('G', X, F)],
         [[(1, 1)], (' ', X, F), (' ', X, F), ('T', X, F), ('U', X, F), ('R', X, F), ('I', X, F), ('N', X, F), ('G', X, F)],
         [[(2, 2)], (' ', X, F), (' ', X, F), ('T', X, F), ('U', X, F), ('R', X, F), ('I', X, F), ('N', X, F), ('G', X, F)],
         [[(3, 3)], ('0', X, F), (' ', X, F), ('T', X, F), ('U', X, F), ('R', X, F), ('I', X, F), ('N', X, F), ('G', X, F)],
         [[(4, 4)], ('0', X, F), ('5', X, F), ('T', X, F), ('U', X, F), ('R', X, F), ('I', X, F), ('N', X, F), ('G', X, F)],
         [[(5, 5)], ('0', X, F), ('5', X, F), ('T', X, F), ('U', X, F), ('R', X, F), ('I', X, F), ('N', Y, F), ('G', Y, F)],
         [[(6, 6)], ('0', X, F), ('5', X, F), ('T', X, F), ('U', X, F), ('R', X, F), ('I', X, F), ('N', Y, F), ('G', Y, F)],
         [[(6, 6)], ('0', X, F), ('5', X, F), ('T', X, F), ('U', X, F), ('R', X, F), ('I', X, F), ('G', X, F), ('N', X, F)],
         [[(4, 4)], ('0', X, F), ('4', X, F), ('T', X, F), ('U', X, F), ('R', X, F), ('I', X, F), ('G', X, F), ('N', X, F)],
         [[(5, 5)], ('0', X, F), ('4', X, F), ('T', X, F), ('U', X, F), ('R', X, F), ('I', Y, F), ('G', Y, F), ('N', X, F)],
         [[(6, 6)], ('0', X, F), ('4', X, F), ('T', X, F), ('U', X, F), ('R', X, F), ('I', Y, F), ('G', Y, F), ('N', X, F)],
         [[(6, 6)], ('0', X, F), ('4', X, F), ('T', X, F), ('U', X, F), ('R', X, F), ('G', X, F), ('I', X, F), ('N', X, F)],
         [[(4, 4)], ('0', X, F), ('3', X, F), ('T', X, F), ('U', X, F), ('R', X, F), ('G', X, F), ('I', X, F), ('N', X, F)],
         [[(5, 5)], ('0', X, F), ('3', X, F), ('T', X, F), ('U', X, F), ('R', Y, F), ('G', Y, F), ('I', X, F), ('N', X, F)],
         [[(6, 6)], ('0', X, F), ('3', X, F), ('T', X, F), ('U', X, F), ('R', Y, F), ('G', Y, F), ('I', X, F), ('N', X, F)],
         [[(6, 6)], ('0', X, F), ('3', X, F), ('T', X, F), ('U', X, F), ('G', X, F), ('R', X, F), ('I', X, F), ('N', X, F)],
         [[(4, 4)], ('0', X, F), ('2', X, F), ('T', X, F), ('U', X, F), ('G', X, F), ('R', X, F), ('I', X, F), ('N', X, F)],
         [[(5, 5)], ('0', X, F), ('2', X, F), ('T', X, F), ('U', Y, F), ('G', Y, F), ('R', X, F), ('I', X, F), ('N', X, F)],
         [[(6, 6)], ('0', X, F), ('2', X, F), ('T', X, F), ('U', Y, F), ('G', Y, F), ('R', X, F), ('I', X, F), ('N', X, F)],
         [[(6, 6)], ('0', X, F), ('2', X, F), ('T', X, F), ('G', X, F), ('U', X, F), ('R', X, F), ('I', X, F), ('N', X, F)],
         [[(4, 4)], ('0', X, F), ('1', X, F), ('T', X, F), ('G', X, F), ('U', X, F), ('R', X, F), ('I', X, F), ('N', X, F)],
         [[(5, 5)], ('0', X, F), ('1', X, F), ('T', Y, F), ('G', Y, F), ('U', X, F), ('R', X, F), ('I', X, F), ('N', X, F)],
         [[(6, 6)], ('0', X, F), ('1', X, F), ('T', Y, F), ('G', Y, F), ('U', X, F), ('R', X, F), ('I', X, F), ('N', X, F)],
         [[(6, 6)], ('0', X, F), ('1', X, F), ('G', B, F), ('T', X, F), ('U', X, F), ('R', X, F), ('I', X, F), ('N', X, F)],
         [[(4, 4)], ('0', X, F), ('0', X, F), ('G', B, F), ('T', X, F), ('U', X, F), ('R', X, F), ('I', X, F), ('N', X, F)],
         [[(3, 3)], ('1', X, F), (' ', X, F), ('G', B, F), ('T', X, F), ('U', X, F), ('R', X, F), ('I', X, F), ('N', X, F)],
         [[(4, 4)], ('1', X, F), ('5', X, F), ('G', B, F), ('T', X, F), ('U', X, F), ('R', X, F), ('I', X, F), ('N', X, F)],
         [[(5, 5)], ('1', X, F), ('5', X, F), ('G', B, F), ('T', X, F), ('U', X, F), ('R', X, F), ('I', Y, F), ('N', Y, F)],
         [[(4, 4)], ('1', X, F), ('4', X, F), ('G', B, F), ('T', X, F), ('U', X, F), ('R', X, F), ('I', X, F), ('N', X, F)],
         [[(5, 5)], ('1', X, F), ('4', X, F), ('G', B, F), ('T', X, F), ('U', X, F), ('R', Y, F), ('I', Y, F), ('N', X, F)],
         [[(6, 6)], ('1', X, F), ('4', X, F), ('G', B, F), ('T', X, F), ('U', X, F), ('R', Y, F), ('I', Y, F), ('N', X, F)],
         [[(6, 6)], ('1', X, F), ('4', X, F), ('G', B, F), ('T', X, F), ('U', X, F), ('I', X, F), ('R', X, F), ('N', X, F)],
         [[(4, 4)], ('1', X, F), ('3', X, F), ('G', B, F), ('T', X, F), ('U', X, F), ('I', X, F), ('R', X, F), ('N', X, F)],
         [[(5, 5)], ('1', X, F), ('3', X, F), ('G', B, F), ('T', X, F), ('U', Y, F), ('I', Y, F), ('R', X, F), ('N', X, F)],
         [[(6, 6)], ('1', X, F), ('3', X, F), ('G', B, F), ('T', X, F), ('U', Y, F), ('I', Y, F), ('R', X, F), ('N', X, F)],
         [[(6, 6)], ('1', X, F), ('3', X, F), ('G', B, F), ('T', X, F), ('I', X, F), ('U', X, F), ('R', X, F), ('N', X, F)],
         [[(4, 4)], ('1', X, F), ('2', X, F), ('G', B, F), ('T', X, F), ('I', X, F), ('U', X, F), ('R', X, F), ('N', X, F)],
         
         ]
    tex = '\\begin{overprint}\n'
    for i, row in enumerate(A):
        highlight = row[0]
        a = row[1:]
        tex += '\onslide<%d|handout:%d>\n' %(i + 1, i + 1)
        tex += '\\begin{center}\n'
        tex += slideutils.code_highlight('java', CODE, highlight, fullsize = False)
        tex += '\end{center}\n'
        tex += '\\begin{center}\n'
        tex += slideutils.trace(8, VARS, a)
        tex += '\end{center}\n'
    tex += '\end{overprint}\n'
    return tex

def main(args):
    # print(trace1())
    print(trace2())

if __name__ == '__main__':
    main(sys.argv[1:])
    
