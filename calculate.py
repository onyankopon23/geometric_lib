import importlib

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
        raise ValueError(
            f"Invalid figure: {fig}. Allowed figures are: {figs}"
        )
    if func not in funcs:
        raise ValueError(
            f"Invalid function: {func}. Allowed functions are: {funcs}"
        )
    if len(size) != sizes[f"{func}-{fig}"]:
        raise ValueError(
            f"Expected {sizes[f'{func}-{fig}']} dimensions, "
            f"got {len(size)}."
        )
    module = importlib.import_module(fig)
    operation = getattr(module, func)
    return operation(*size)


def get_input(prompt):
    return list(map(float, input(prompt).split()))


if __name__ == "__main__":
    fig = input(f"Choose a figure ({', '.join(figs)}):\n")
    while fig not in figs:
        fig = input(f"Invalid figure. Choose from ({', '.join(figs)}):\n")

    func = input(f"Choose a function ({', '.join(funcs)}):\n")
    while func not in funcs:
        func = input(f"Invalid function. Choose from ({', '.join(funcs)}):\n")

    expected_size = sizes[f"{func}-{fig}"]
    size = get_input(
        f"Enter {expected_size} dimension(s) separated by spaces:\n"
    )
    while len(size) != expected_size:
        size = get_input(
            f"Invalid number of dimensions. Enter {expected_size}:\n"
        )

    result = calc(fig, func, size)
    print(f"{func.capitalize()} of {fig} is {result}")
