# Operadores en Python

## Ejercicio 1

**Expresión:**

`5 + 3 * 2`

**Resolución manual:**

En Python, primero se resuelven las multiplicaciones y luego las sumas (jerarquía de operadores).

3 * 2 = 6
5 + 6 = 11

**Resultado manual:**
`11`

**Comprobación en Python:**

```python
print(5 + 3 * 2)
```

**Resultado en Python:**

`11`


## Ejercicio 2

**Expresión:**

`8 / 2 + 4 * 3`

**Resolución manual:**

Primero se resuelven la división y la multiplicación (de izquierda a derecha):

8 / 2 = 4
4 * 3 = 12

Luego se realiza la suma:

4 + 12 = 16

**Resultado manual:**
`16.0`

**¿Por qué?**
Porque en Python la división (`/`) siempre devuelve un número decimal (float), y se respeta la jerarquía de operadores: primero división y multiplicación, luego suma.

**Comprobación en Python:**

```python
print(8 / 2 + 4 * 3)
```

**Resultado en Python:**

`16.0`
## Ejercicio 3

**Expresión:**

`(7 + 3) * 2 - 5`

**Resolución manual:**

Primero se resuelven los paréntesis:

7 + 3 = 10

Luego la multiplicación:

10 * 2 = 20

Finalmente la resta:

20 - 5 = 15

**Resultado manual:**
`15`

**¿Por qué?**
Porque en Python se sigue la jerarquía de operadores: primero paréntesis, luego multiplicación y finalmente resta.

**Comprobación en Python:**

```python
print((7 + 3) * 2 - 5)
```

**Resultado en Python:**

`15`

## Ejercicio 4

**Expresión:**

`10 - 4 + 2 * 3`

**Resolución manual:**

Primero se resuelve la multiplicación:

2 * 3 = 6

Luego las operaciones de izquierda a derecha:

10 - 4 = 6
6 + 6 = 12

**Resultado manual:**
`12`

**¿Por qué?**
Porque en Python se respeta la jerarquía de operadores: primero la multiplicación y luego la suma y resta de izquierda a derecha.

**Comprobación en Python:**

```python
print(10 - 4 + 2 * 3)
```

**Resultado en Python:**

`12`

## Ejercicio 5

**Expresión:**

`(10 / 2) * (3 + 2) - 4`

**Resolución manual:**

Primero se resuelven los paréntesis:

10 / 2 = 5.0
3 + 2 = 5

Luego la multiplicación:

5.0 * 5 = 25.0

Finalmente la resta:

25.0 - 4 = 21.0

**Resultado manual:**
`21.0`

**¿Por qué?**
Porque en Python primero se resuelven los paréntesis, luego la multiplicación y finalmente la resta. Además, la división (`/`) devuelve un número decimal (float), por eso el resultado final es `21.0`.

**Comprobación en Python:**

```python id="k3n9qp"
print((10 / 2) * (3 + 2) - 4)
```

**Resultado en Python:**

`21.0`

## Ejercicio 6

**Expresión:**

`2 + 3 * (4 - 1)`

**Resolución manual:**

Primero se resuelven los paréntesis:

4 - 1 = 3

Luego la multiplicación:

3 * 3 = 9

Finalmente la suma:

2 + 9 = 11

**Resultado manual:**
`11`

**¿Por qué?**
Porque en Python se sigue la jerarquía de operadores: primero paréntesis, luego multiplicación y finalmente suma.

**Comprobación en Python:**

```python id="p7k2mz"
print(2 + 3 * (4 - 1))
```

**Resultado en Python:**

`11`

## Ejercicio 7

**Expresión:**

`5 * 2 ** 3`

**Resolución manual:**

Primero se resuelve la potencia:

2 ** 3 = 8

Luego la multiplicación:

5 * 8 = 40

**Resultado manual:**
`40`

**¿Por qué?**
Porque en Python la potenciación (`**`) tiene mayor prioridad que la multiplicación (`*`), por eso se resuelve primero.

**Comprobación en Python:**

```python id="t4x9qn"
print(5 * 2 ** 3)
```

**Resultado en Python:**

`40`

## Ejercicio 8

**Expresión:**

`6 + 4 / 2 ** 2`

**Resolución manual:**

Primero se resuelve la potencia:

2 ** 2 = 4

Luego la división:

4 / 4 = 1.0

Finalmente la suma:

6 + 1.0 = 7.0

**Resultado manual:**
`7.0`

**¿Por qué?**
Porque en Python primero se resuelve la potenciación (`**`), luego la división (`/`) y finalmente la suma (`+`). Además, la división devuelve un número decimal (float).

**Comprobación en Python:**

```python id="u9m3rk"
print(6 + 4 / 2 ** 2)
```

**Resultado en Python:**

`7.0`

## Ejercicio 9

**Expresión:**

`10 % 3 + 2 * 5`

**Resolución manual:**

Primero se resuelven el módulo y la multiplicación:

10 % 3 = 1
2 * 5 = 10

Luego la suma:

1 + 10 = 11

**Resultado manual:**
`11`

**¿Por qué?**
Porque en Python el módulo (`%`) y la multiplicación (`*`) tienen mayor prioridad que la suma (`+`), por lo que se resuelven primero.

**Comprobación en Python:**

```python id="x8n2qp"
print(10 % 3 + 2 * 5)
```

**Resultado en Python:**

`11`

## Ejercicio 10

**Expresión:**

`(8 + 2) * 3 ** 2`

**Resolución manual:**

Primero se resuelven los paréntesis:

8 + 2 = 10

Luego la potencia:

3 ** 2 = 9

Finalmente la multiplicación:

10 * 9 = 90

**Resultado manual:**
`90`

**¿Por qué?**
Porque en Python primero se resuelven los paréntesis, luego la potenciación (`**`) y finalmente la multiplicación (`*`).

**Comprobación en Python:**

```python id="q7n4zp"
print((8 + 2) * 3 ** 2)
```

**Resultado en Python:**

`90`

## Ejercicio 11

**Expresión:**

`7 + 2 * (3 + 5) / 4`

**Resolución manual:**

Primero se resuelven los paréntesis:

3 + 5 = 8

Luego la multiplicación:

2 * 8 = 16

Después la división:

16 / 4 = 4.0

Finalmente la suma:

7 + 4.0 = 11.0

**Resultado manual:**
`11.0`

**¿Por qué?**
Porque en Python se respeta la jerarquía de operadores: primero paréntesis, luego multiplicación y división, y finalmente la suma. Además, la división (`/`) devuelve un número decimal (float).

**Comprobación en Python:**

```python id="w3k8mz"
print(7 + 2 * (3 + 5) / 4)
```

**Resultado en Python:**

`11.0`

## Ejercicio 12

**Expresión:**

`2 ** 3 * 4 / 2`

**Resolución manual:**

Primero se resuelve la potencia:

2 ** 3 = 8

Luego la multiplicación:

8 * 4 = 32

Después la división:

32 / 2 = 16.0

**Resultado manual:**
`16.0`

**¿Por qué?**
Porque en Python la potenciación (`**`) tiene mayor prioridad, luego se realizan multiplicación y división de izquierda a derecha. Además, la división (`/`) devuelve un número decimal (float).

**Comprobación en Python:**

```python id="z9x2qp"
print(2 ** 3 * 4 / 2)
```

**Resultado en Python:**

`16.0`


## Ejercicio 13

**Expresión:**

`9 - 6 + 3 ** 2`

**Resolución manual:**

Primero se resuelve la potencia:

3 ** 2 = 9

Luego las operaciones de izquierda a derecha:

9 - 6 = 3
3 + 9 = 12

**Resultado manual:**
`12`

**¿Por qué?**
Porque en Python la potenciación (`**`) tiene mayor prioridad que la suma y la resta, y estas se resuelven de izquierda a derecha.

**Comprobación en Python:**

```python id="n4k7mz"
print(9 - 6 + 3 ** 2)
```

**Resultado en Python:**

`12`


## Ejercicio 14

**Expresión:**

`(7 - 2) * 5 + 3 ** 2`

**Resolución manual:**

Primero se resuelven los paréntesis:

7 - 2 = 5

Luego la multiplicación:

5 * 5 = 25

Después la potencia:

3 ** 2 = 9

Finalmente la suma:

25 + 9 = 34

**Resultado manual:**
`34`

**¿Por qué?**
Porque en Python se respeta la jerarquía de operadores: primero paréntesis, luego potenciación (`**`), después multiplicación (`*`) y finalmente suma (`+`).

**Comprobación en Python:**

```python id="y6m2qp"
print((7 - 2) * 5 + 3 ** 2)
```

**Resultado en Python:**

`34`

## Ejercicio 15

**Expresión:**

`4 * 2 ** 3 / 8 + 1`

**Resolución manual:**

Primero se resuelve la potencia:

2 ** 3 = 8

Luego multiplicación y división de izquierda a derecha:

4 * 8 = 32
32 / 8 = 4.0

Finalmente la suma:

4.0 + 1 = 5.0

**Resultado manual:**
`5.0`

**¿Por qué?**
Porque en Python la potenciación (`**`) tiene mayor prioridad, luego se realizan multiplicación y división de izquierda a derecha, y finalmente la suma. Además, la división (`/`) devuelve un número decimal (float).

**Comprobación en Python:**

```python id="k8m3zp"
print(4 * 2 ** 3 / 8 + 1)
```

**Resultado en Python:**

`5.0`
