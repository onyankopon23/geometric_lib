
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# General description
Калькулятор позволяет вычислять площадь или периметр различных фигур.

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# Функции

### Circle
**area(r)**: Рассчитывает площадь круга с радиусом 'r'.
Пример: 'area(4)' вернет '50.24'.

**perimeter(r)**: Рассчитывает периметр круга (длину окружности) с радиусом `r`.
Пример: `perimeter(5)` вернёт `31.4`.

### Square
**area(a)**: Рассчитывает площадь квадрата со стороной длиной `a`.
Пример: `area(5)` вернёт `25`.

**perimeter(a)**: Рассчитывает периметр квадрата со стороной длиной `a`.
Пример: `perimeter(5)` вернёт `20`.

### Triangle
**area(a, b, c)**: Рассчитывает площадь треугольника с длинами сторон 'a', 'b' и 'c'.
Пример: `area(3, 4, 5)` вернёт `6`.

**perimeter(a, b, c)**: Рассчитывает периметр треугольника, суммируя длины его сторон.
Пример: `perimeter(3, 4, 5)` вернёт `12`.

# Commit history
Commit '1a6c3abc34dc0a0dfd21753c817b09a189428ad6' - Added documentation








