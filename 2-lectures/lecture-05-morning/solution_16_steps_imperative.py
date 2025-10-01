from matplotlib import pyplot as plt

def count_steps(n):
    """
    >>> count_steps(1)
    1
    >>> count_steps(2)
    2
    >>> count_steps(3)
    3
    >>> count_steps(4)
    5
    >>> count_steps(10)
    89
    """

    assert isinstance(n, int) and n > 0

    steps = [1, 2]

    for i in range(3, n + 1):
        steps.append(steps[-1] + steps[-2])

    return steps[n - 1]


def plot_complexity(n=20):

    x_range = list(range(1, n + 1))
    linear_complexity = [2 * i for i in x_range]
    exponential_complexity = [1] + [count_steps(i - 1) for i in x_range[1:]]
    
    plt.plot(x_range, linear_complexity, label="imperative (linear)")
    plt.plot(x_range, exponential_complexity, label="naive recursive (exponential)")
    plt.legend()
    plt.title("Complexity of counting steps")
    plt.show()


def compare_complexity(n=int(1e3)):

    assert isinstance(n, int) and n > 0

    linear = 2 * n
    exponential = count_steps(n - 1)

    print(f"Complexity for n = {n:d}")
    print(f"Imperative (linear) takes {linear:.1g} operations")
    print(f"Recursive (exponential) takes {exponential:.1g} operations")
    print(f"Imperative is {exponential / linear:.1g}x times faster")


compare_complexity()
plot_complexity()
