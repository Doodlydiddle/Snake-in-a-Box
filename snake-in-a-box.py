from timeit import timeit

def hypercube_gen(n):
    return [x for x in range(0, 2**n)]

def hamming_distance(num1, num2):
    return bin(num1 ^ num2).count('1')

def adjacent(num1, num2):
    return True if hamming_distance(num1, num2) == 1 else False

def snake(snake_stack, rem_nodes, removals):
    rem_nodes = [node for node in rem_nodes if node not in removals]
    head = snake_stack[-1]
    adj_nodes = [node for node in rem_nodes if adjacent(head, node)]
    if not adj_nodes:
        return len(snake_stack) - 1
    else:
        return max([snake(snake_stack + [node], rem_nodes, adj_nodes) for node in adj_nodes])



def main():
    n = int(input("Enter dimension:   "))
    hypercube = hypercube_gen(n)
    return snake([0], hypercube[1:], [])

def time_test():
    n = int(input("Enter dimension:   "))
    hypercube = hypercube_gen(n)
    return timeit(lambda: snake([0], hypercube[1:], []), number=1)

print(main())
print(time_test())

