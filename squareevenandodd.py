def square_filter(start, end):
    even_squares = []
    odd_squares = []

    for n in range(start, end + 1):
        sq = n * n
        if sq % 2 == 0:
            even_squares.append(sq)
        else:
            odd_squares.append(sq)

    print("Even square values:", even_squares)
    print("Odd square values:", odd_squares)
square_filter(2, 7)