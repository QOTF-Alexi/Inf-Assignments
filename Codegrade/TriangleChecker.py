def check_triangle(side_a, side_b, side_c):
    if side_a >= (side_b + side_c) or side_b >= (side_c + side_a) or side_c >= (side_a + side_b):
        print("Impossible triangle")
        return False
    else:
        print("Possible triangle")
        return True


if __name__ == "__main__":
    side_a = int(input("Side A: "))
    side_b = int(input("Side B: "))
    side_c = int(input("Side C: "))
    check_triangle(side_a, side_b, side_c)