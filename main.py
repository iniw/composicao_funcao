import cexprtk


def unknown_symbol_callback(symbol):
  print(f"simbolo invalido '{symbol}' - a única variável permitida é x.")
  exit(1)


if __name__ == "__main__":
  while (input_f := input("f(x) = ")).strip() == "":
    print("f(x) não pode estar vazio!")

  while (input_g := input("g(x) = ")).strip() == "":
    print("g(x) não pode estar vazio!")

  exprs = [
      ("g ° f", input_g.replace("x", f"({input_f})")),
      ("g ° g", input_g.replace("x", f"({input_g})")),
      ("f ° g", input_f.replace("x", f"({input_g})")),
      ("f ° f", input_f.replace("x", f"({input_f})")),
  ]

  while True:
    try:
      x = float(input("defina o valor de x: "))
      break
    except ValueError:
      print("valor inválido!")
      continue

  st = cexprtk.Symbol_Table({})
  st.variables['x'] = x

  while True:
    print("escolha a operacao")
    for (i, expr) in enumerate(exprs):
      print(f"{i} -> {expr[0]} = {expr[1]}")

    print(f">= {len(exprs)} -> sair")

    while True:
      try:
        funcao = int(input())
        break
      except ValueError:
        print("valor inválido!")
        continue

    if funcao >= len(exprs):
      break

    expr = exprs[funcao][1]
    value = cexprtk.Expression(expr, st, unknown_symbol_callback).value()
    result = f"({expr})({x}) = {value}"
    print(f"{result}\n{'-' * len(result)}")
