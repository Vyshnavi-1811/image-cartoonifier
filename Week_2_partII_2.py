
def compute_gradient_descent(x_train, y_train, w_init, b_init, alpha, num_iters):
    w = w_init
    b = b_init

    for i in range(num_iters):
        cost = compute_cost(x_train, y_train, w, b)
        dw, db = compute_gradient(x_train, y_train, w, b)

        w -= alpha * dw
        b -= alpha * db

        if (i + 1) % 1000 == 0:
            print(f'Iteration {i+1}, Cost: {cost}')

    return w, b