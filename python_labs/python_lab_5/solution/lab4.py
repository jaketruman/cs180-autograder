import argparse
import numpy

def main(number: int) -> int:
    # Write the code to sum up cubed numbers here.
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.
    total = 0
    i = 0
    while i <= number:
        output = i*i*i
        if output < 10:
            if output % 2 == 0:
                total = total + output
                i += 1
            else:
                i += 1
        else:
            other_output = output
            while output > 9:
                output = output // 10
            if output % 2 == 0:
                total = total + other_output
                i += 1
            else:
                i += 1
    print("cube (" + str(number) + ") = " + str(total))



    return "cube("   + str(number) + ") = " + str(total)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Cube Counter")
    parser.add_argument("--n", type=int, required=True, help="Input a number to sum the cube counts")
    arguments = parser.parse_args()
    main(arguments.n)