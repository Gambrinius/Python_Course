box1 = sorted([int(input()) for _ in range(3)])
box2 = sorted([int(input()) for _ in range(3)])

if all(side1 == side2 for side1, side2 in zip(box1, box2)):
    print("Boxes are equal")
elif all(side1 <= side2 for side1, side2 in zip(box1, box2)):
    print("The first box is smaller than the second one")
elif all(side1 >= side2 for side1, side2 in zip(box1, box2)):
    print("The first box is larger than the second one")
else:
    print("Boxes are incomparable")
