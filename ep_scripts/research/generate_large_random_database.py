import numpy as np
import all_paths as ap


def create():

    random_state = np.random.RandomState(12345)  # seed with initial value, so it is repeatable
    a = random_state.random_sample((1000, 2))  # generate a 2-column list of random numbers
    name = __file__.replace('.py', '')  # collect the name of the generator file
    name = name.split("generate_")[-1]  # formulate the name of the data file
    np.savetxt(ap.PROJECT_LARGE_DATABASE + name + ".txt", a, header="a,b", delimiter=",")  # save


if __name__ == '__main__':
    create()
