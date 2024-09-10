def fun(n):
  if n>10:
    return
  print(n)
  fun(1+n)

fun(1)