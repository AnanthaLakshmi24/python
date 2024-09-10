def fun(table,start,stop):
  if start>stop:
    return
  print(table,"X",start,"=",table*start)
  fun(table,start+1,stop)

fun(3,1,10)