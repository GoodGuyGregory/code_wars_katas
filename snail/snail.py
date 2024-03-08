# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python
def snail(snail_map):
    pass

def main():
    # test case for nxn
    array = [[1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]]

    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    result = "pass" if snail(array) is expected else "fail"

    print( result)


main()

