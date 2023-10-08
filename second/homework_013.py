def plus(a,b):
    return a+b

if __name__ == '__main__':
    print(plus(2,2))

# Topic 13
# Task 1
def count_local_var():
    var1 = 10
    var2 = "Hello"
    var3 = [1, 2, 3]

    print(locals())
    # num_var = locals
    # return len(num_var)
    local_variables = locals()
    a = len(local_variables)

# print(f"Number of local variables: {num_var}")

# Call the function
count_local_var()
