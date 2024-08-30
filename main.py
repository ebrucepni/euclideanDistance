def main():
    points = [(3, 4), (1, 9), (13, 5), (100, 200)]
    distances = []
    euclidean_distance(points, distances)

    min_distance = distances[0]
    for value in distances:
        if min_distance > value:
            min_distance = value
    print("Minimum distance is", min(distances))


def euclidean_distance(my_list, new_list):
    length_list = len(my_list)
    for i in range(length_list - 1):
        for j in range(length_list - 1, i, -1):
            x1 = my_list[i][0]
            y1 = my_list[i][1]
            x2 = my_list[j][0]
            y2 = my_list[j][1]
            difference_square = ((x2 ** 2 - x1 ** 2) + (y2 ** 2 - y1 ** 2))
            points_distance = difference_square ** 0.5                          # square root calculation
            new_list.append(points_distance)
            print("Distance between point", i, "and", j, "=", points_distance)
            j += 1
        i += 1

main()
