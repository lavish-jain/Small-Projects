from pythagorean_triples import Triples

def main():

    while 1:
        side_a = input("Enter the length of first side: ")
        side_b = input("Enter the length of second side: ")
        side_c = input("Enter the length of third side: ")

        triplets = Triples(side_a, side_b, side_c)
        if triplets.checkTriples():
            print("The sides are Pythagorean Triplets")
        else:
            print("The sides are not Pythagorean Triplets")

        choice = input("Do you want to continue? (Y/N)")
        if choice == 'y' or choice == 'Y':
            continue 
        else:
            break

main()