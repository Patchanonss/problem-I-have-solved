width = int(input())  # the number of cells on the X axis
height = int(input())
node = []
ans = []
x_index = 0
y_index = 0
for i in range(height):
    line = list(input())
    node.append(line)
while y_index < height:
    cond_x = True
    cond_y = True
    if node[y_index][x_index] == '0':
        has_node = '{} {}'.format(x_index, y_index)
        for x in range(x_index + 1, width):
            if node[y_index][x] == '0':
                has_node += ' {} {}'.format(x, y_index)
                cond_x = False
                break
        if x_index == width - 1:
            has_node += ' -1 -1'
        elif cond_x:
            has_node += ' -1 -1'
        for y in range(1 + y_index, height):
            if node[y][x_index] == '0':
                has_node += ' {} {}'.format(x_index, y)
                cond_y = False
                break
        if y_index == height - 1:
            has_node += ' -1 -1'
        elif cond_y:
            has_node += ' -1 -1'
        ans.append(has_node)
    x_index += 1
    if x_index == width:
        x_index = 0
        y_index += 1
for a in ans:
    print(a)


