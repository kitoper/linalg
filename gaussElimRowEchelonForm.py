def gauss(given):
    """ Performs the Gaussian Elimination algorithm on an mxn matrix """

    rownum, colnum = len(given), len(given[0])
    h, k = 0, 0

    while h < rownum and k < colnum:
        #find the kth pivot
        kthcol = [abs(given[i][k]) for i in range(0, rownum)]
        imax = kthcol.index(max(kthcol))
        if kthcol[imax] == 0:
            #no pivots in the kth column, go to next column
            k += 1
        else:
            #swap the rows
            given[imax],given[h] = given[h],given[imax]
            for i in range(h+1, rownum):
                f = given[i][k] / given[h][k]
                #fill column entries below pivot as zero
                given[i][k] = 0
                #subtract multiplied pivot row
                for j in range(k+1, colnum):
                    given[i][j] = given[i][j] - f*given[h][j]
            #go to next pivot row and column
            h += 1
            k += 1

    return given

if __name__ == '__main__':
    a = [[-9, 4, 20], [-7, 16, 80]]
    print "before: ", a
    print "after: ", gauss(a)
