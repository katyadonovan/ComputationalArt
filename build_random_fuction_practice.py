import random
variables = [["x"],["y"]]
functions = ["sin_pi", "cos_pi","square_root","square","avg","prod"]

def build_random_function(min_depth, max_depth):
    if min_depth == 0:
        for_variables = random.randint(0,1)
        start_var = variables[for_variables]
        print(start_var)
        return [start_var]
    else:
        for_functions = random.randint(0,5)
        start_function = functions[for_functions]
        if start_function > 4:
            print(start_function)
            return [start_function, build_random_function(min_depth-1,max_depth-1), build_random_function(min_depth-1,max_depth-1)]
        else:
            print(start_function)
            return [start_function, build_random_function(min_depth-1,max_depth-1)]

print(build_random_function(7,9))
