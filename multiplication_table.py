def multiplication_table(table, start, end):
    for i in range(start,end+1):
        print(f"{table} * {i} = {table*i}")

multiplication_table(5,0,12)
multiplication_table(6,1,10)
