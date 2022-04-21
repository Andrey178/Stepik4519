def multiply_table(param1, param2):
    table = []
    for mul1 in range(1, param2 + 1):
        table_row = []
        for mul2 in range(1, param1 + 1):
            table_row.append(mul1 * mul2)
        table.append(table_row)
    print("""<html><body><table>""")
    for row in table:
        print("<tr>")
        print("", end='')
        for elem in row:
            print(f"<td><a href=\"http://{elem}.ru\">{elem}</a></td>", end='')
        print("\n</tr>")
    print("""</table></body></html>""")


def task(name):
    multiply_table(10, 10)


if __name__ == '__main__':
    task('main')
