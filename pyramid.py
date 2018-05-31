height = int(input("How high do you want your pyramid my Pharaoh?"))


def build_pyramid(height_count):
    if height_count <= 0:
        return 0
    return height_count + build_pyramid(height_count - 1)


print("You will need {} bricks to build this pyramid my Pharaoh".format(build_pyramid(height)))
