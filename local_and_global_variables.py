#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in October 2022
# A program that uses local and global variables

variable_x = 10


def local_variables():
    # Uses local variables

    variable_x = 20
    variable_y = 50
    variable_z = variable_x + variable_y
    print(
        "variable_x, variable_y, variable_z | {0} + {1} = {2}".format(
            variable_x, variable_y, variable_z
        )
    )


def global_variables():
    # Uses global variables

    global variable_x
    variable_x = variable_x + 5
    variable_y = 50
    variable_z = variable_x + variable_y
    print(
        "variable_x, variable_y, variable_z | {0} + {1} = {2}".format(
            variable_x, variable_y, variable_z
        )
    )


def main():
    # Calls functions that use local and global variables

    local_variables()
    global_variables()

    print("\nDone.")


if __name__ == "__main__":
    main()
