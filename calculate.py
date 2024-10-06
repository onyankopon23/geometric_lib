import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
       """
        Вычисляет указанную функцию для заданной фигуры.

                Параметры:
                    fig (str): Название фигуры, допустимые значения: 'circle', 'square'.
                    func (str): Функция, которую нужно выполнить, допустимые значения: 'perimeter', 'area'.
                    size (list): Размеры фигуры.
        """


	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
          """
        Основной блок программы. Запрашивает у пользователя фигуру, функцию и размеры,
        затем вызывает функцию calc для вычисления периметра или площади выбранной фигуры.

                Параметры:
                        Программа запрашивает ввод у пользователя.
        """
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)



