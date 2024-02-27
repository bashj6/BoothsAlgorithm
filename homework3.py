"""
Kaylyn Boice
Ryan Petschauer
Professor Kennth Riddle
CSC20252H1

Implements Booth's Algorithm

"""

Multiplication = [4," "," "," "," "]

# prints the array
def print_list():
    for i in range(0,4):
        print("%4s" % Multiplication[i], end="")
    print("\t%s\n" % Multiplication[4])
    Multiplication[4] = " "
#Comparing the last bit to q
def concatenate(LB, q):
    LB = str(LB)[-1]
    q = str(q)
    num = LB + q
    return num

def clear_bit(bit):
    bit = null
    return bit
#converts and takes off the first two characters
def binary_conversion(val):
    binary = bin(int(val))[2:]
    return binary

# need this since m is found this way.
def twos_comp(val, bits):
    """compute the 2's complement of int value val"""
    val = int(val)
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    val = str(val)
    return val
# fills zeros for the initial input
def add_zeros(val):
    total_digits = 4
    result = str(val).zfill(total_digits)
    return result


def main():
    #global variable
    global Multiplication
    #getting the input for the multiplication
    M = int(input("Type a number:  "))
    Q = int(input("Type another number:  "))

    # setting up the variables for the problem
    # N is the number of bits and is set at 4
    N = Multiplication[0]
    # q starts at zero as it gets ready to compare to Q
    q = str(0)
    Multiplication[3] = q
    # M is the muliplier which we take the 2's complement of
    M = str(binary_conversion(M))
    A = str(twos_comp(M, 4))
    print(A)
    Multiplication[1] = A
    # Q gets assigned and converted here
    Q = str(binary_conversion(Q))
    M = add_zeros(M)
    Q = add_zeros(Q)
    # Assignning Q to the 3 position on the array
    Multiplication[2] = Q
    
    # starting the Multiplication
    Multiplication[4] = "Initialization"
    print("N    A    Q    q    Action")
    print(35 * '-')
    print_list()
    #while loop runs til the condition of N is met
    while(N != 0):

        CB = concatenate(Q, q)
        if CB == "10":
            A = bin(int(A, 2) - int(M, 2))[2:].zfill(4)
            Multiplication[4] = " A = A - M "
            print_list()

        elif CB =="01":
            A = bin(int(A, 2) + int(M, 2))[2:].zfill(4)
            Multiplication[4] = " A = A + M "
            print_list()
        elif CB == "00" or CB == "11":
            print_list()


        Temp_Q = Q
        Temp_mem = Q + Temp_Q[-1]

        Q = Q[0:2] #shifts Q right
        print(Q)

        q = Q[-1] #assign q the new least significant bit of Q
        Q = Temp_mem + Q
        print(Q)
        Multiplication[3] = q
        Multiplication[2] = Q
        Multiplication[4] = " Shift "
        print_list()

        Multiplication[1] = A
        N = N - 1
        Multiplication[0] = N
        print_list()

    print(f'{A} {Q}')

if __name__ == "__main__":
    main()
