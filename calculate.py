
import circle
import square
import triangle

figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {
    "area-circle": 1,
    "perimeter-circle": 1,
    "area-square": 1,
    "perimeter-square": 1,
    "area-triangle": 3,
    "perimeter-triangle": 3,
}

def calc(fig, func, size):
    if fig not in figs:
        raise ValueError(f"Invalid figure: {fig}. Allowed figures are: {figs}")
    if func not in funcs:
        raise ValueError(f"Invalid function: {func}. Allowed functions are: {funcs}")
    if len(size) != sizes[f"{func}-{fig}"]:
        raise ValueError(
            f"Invalid number of dimensions for {func} of {fig}. "
            f"Expected {sizes[f'{func}-{fig}']}, got {len(size)}."
        )
    module = globals()[fig]
    function = getattr(module, func)
    return function(*size)

if __name__ == "__main__":
    fig = ''
    func = ''
    size = []

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")
    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")
    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(float, input(f"Enter dimensions for {fig}, separated by spaces:\n").split()))
    result = calc(fig, func, size)
    print(f'{func.capitalize()} of {fig} is {result}')
