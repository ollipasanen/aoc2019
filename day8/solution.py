def solution():
    with open("input", "r") as f:
        inp = f.read()

    w = 25
    h = 6
    n_layers = len(inp) // (w * h)
    layers = []

    p = 0
    for i in range(n_layers):
        layer = []
        for y in range(h):
            row = []
            for x in range(w):
                row.append(inp[p])
                p += 1
            layer.append(row)
        layers.append(layer)

    def cnt_on_layer(layer, val):
        cnt = 0
        for y in range(h):
            for x in range(w):
                cnt += (layers[layer][y][x] == val)
        return cnt

    # Day 1

    best_layer = -1
    num_zeros = 1e9

    for layer in range(n_layers):
        zero_cnt = cnt_on_layer(layer, "0")
        if zero_cnt < num_zeros:
            num_zeros = zero_cnt
            best_layer = layer

    print(cnt_on_layer(best_layer, "1") * cnt_on_layer(best_layer, "2"))

    # Day 2

    for y in range(h):
        row = []
        for x in range(w):
            col = 2
            for l in range(n_layers):
                c = layers[l][y][x]
                if c == "0":
                    col = "#"
                    break
                if c == "1":
                    col = " "
                    break
            row.append(col)
        print("".join(str(x) for x in row))

if __name__ == '__main__':
    solution()