# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python
def snail(snail_map):
    collectedDigits = []
    visited = []
    N = len(snail_map[0])
    # init starting location
    start = [0, 0]
    while len(visited) < N**2:
        # first go right
        for right in range(N):
            # check for edge:
            if start[1] < N:
                # move right
                # check visited
                location = (start[0], right)
                if location not in visited:
                    collectedDigits.append(snail_map[start[0]][right])
                    visited.append(location)
                start[1] += 1
                right += 1

        # next go down perimeter of the map
        if start[0] < N:
            start[0] += 1
        down = start[0]
        for down in range(down, N):
            # collect all numbers below if not visited.
            location = (down, start[1]-1)
            # check visited
            if location not in visited:
                collectedDigits.append(snail_map[down][N-1])
                visited.append(location)
            start[0] += 1
            down += 1

        #next go left perimeter until 0 boundary is reached
        if start[1] > 0:
            start[0] -= 1
            start[1] -= 1
        left = start[1]-1
        for left in range(left, -1, -1):

            location = (start[0], left)
            # go left
            if location not in visited:
                collectedDigits.append(snail_map[start[0]][left])
                visited.append(location)
            start[1] = left







    # done traveling
    return collectedDigits


def main():
    # test case for nxn
    array = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

    expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]

    result = "pass" if snail(array) is expected else "fail"

    print(result)


main()

