import sys
# we write the orbit.params for each loop in a new job folder.
def generate_orbit_params(beta, phi, output_dir):
        output_file = f'{output_dir}/sample.params'
        with open(output_file, "w") as file:
                file.write("# tde setup file\n")
                file.write("beta =      {:.3f}    ! beta\n".format(beta))
                file.write("phi =         {:.3f}    ! phi\n".format(phi))
        print("Finished generating a new sample.params file with beta and phi as ",beta,phi)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python generate_orbit_params.py <beta> <phi>")
        sys.exit(1)

    beta = float(sys.argv[1])
    phi = float(sys.argv[2])
    output_file = sys.argv[3]
    print(output_file,"output_file")
    print(beta,"beta in python script")
    print(phi,"phi in python script")
    generate_orbit_params(beta, phi, output_file)
