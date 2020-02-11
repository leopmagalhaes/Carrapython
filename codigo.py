in_file = "dados2.txt"
out_file = "saida.txt"
 
search_for = "12"
line_num = 0
lines_found = 0

with open(out_file, 'w') as out_f:
    with open(in_file, "r") as in_f:
        for line in in_f:
            line_num += 1
            if search_for in line:
                lines_found += 1
                print("Found '{}' in line {}...".format(search_for, line_num))
                out_f.write(line)
 
        print("Found {} lines...".format(lines_found))

arquivo = open('saida.txt', 'r')
df = arquivo.read()
arquivo.close()

print(df)


