# Kata: https://www.codewars.com/kata/5a25ac6ac5e284cfbe000111/train/python

def triangle(row):
    if len(row) > 1:
        downRow = []
        for index in range(len(row)-1):
            if index < (len(row)-1):
                # if the two colors are the same. keep them the same
                if row[index] == row[index+1]:
                    downRow += row[index]
                else:
                    # case where they're B G -> R or R G ->  B  or B R -> G
                    if row[index] == 'B' and row[index + 1] == 'G' or row[index] == 'G' and row[index+1 ] == 'B':
                        downRow += 'R'
                    if row[index] == 'R' and row[index + 1] == 'G' or row[index] == 'G' and row[index+1 ] == 'R':
                        downRow += 'B'
                    if row[index] == 'B' and row[index + 1] == 'R' or row[index] == 'R' and row[index+1 ] == 'B':
                        downRow += 'G'

            # print(downRow)
        return triangle(downRow)
    else:
        # base case
        return row[0]


def main():
    print(triangle("RRGBRGBB"))


main()