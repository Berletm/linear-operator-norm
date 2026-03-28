import numpy as np
import matplotlib.pyplot as plt


# var 2
OPERATOR = np.array([
    [  333/11,   288/11,   18/11,  270/11],
    [  819/22,  1305/22, -315/11,  324/11],
    [-1257/44, -1773/44,  453/22, -315/11],
    [  -81/44,  -549/44,  351/22,  108/11]
])

def draw_operator() -> None:
    A = np.array([[  3,    0.5],
                  [  5,      7]])
    theta = np.linspace(0, 2 * np.pi, 200)
    x_circle = np.cos(theta)
    y_circle = np.sin(theta)

    points_orig = np.vstack((x_circle, y_circle))

    points_trans = A @ points_orig 

    n_vectors = 32
    angles = np.linspace(0, 2 * np.pi, n_vectors, endpoint=False)
    vx_orig = np.cos(angles)
    vy_orig = np.sin(angles)
    vecs_orig = np.vstack((vx_orig, vy_orig))

    vecs_trans = A @ vecs_orig

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.grid(True, linestyle='--', alpha=0.5)

    ax1.plot(x_circle, y_circle, 'b-', alpha=0.3)

    for i in range(n_vectors):
        ax1.arrow(0, 0, vx_orig[i], vy_orig[i], 
                head_width=0.03, head_length=0.03, fc='blue', ec='blue')

    ax2.grid(True, linestyle='--', alpha=0.5)

    ax2.plot(points_trans[0, :], points_trans[1, :], 'r-', alpha=0.5)

    for i in range(n_vectors):
        ax2.arrow(0, 0, vecs_trans[0, i], vecs_trans[1, i], 
                head_width=0.02 * np.max(np.abs(A)),
                head_length=0.02 * np.max(np.abs(A)), 
                fc='red', ec='red')

    plt.tight_layout()
    plt.show()


def main() -> None:
    G = OPERATOR.T @ OPERATOR
    G_inv = np.linalg.inv(G)
    
    b = np.array([1/2, 1/3, 1/4, 1/5])
    x = np.array([1, 1, 1, 1])
    iters = 10
    
    print(x_ := np.linalg.solve(np.eye(4) - G_inv, b))
    print()
    residuals = []
    solutions = []
    solutions.append(x)
    residuals.append(b - (np.eye(4) - G_inv) @ x)
    for _ in range(iters):
        x = b + G_inv @ x
        solutions.append(x)
        residuals.append(b - (np.eye(4) - G_inv) @ x)
    
    res_len = [np.linalg.norm(res, ord=2) for res in residuals]
    errors_ = [x_ - sol for sol in solutions]
    errors_len = [np.linalg.norm(res, ord=2) for res in errors_]
    
    print(res_len)
    print(errors_len)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    # График невязок
    ax1.semilogy(res_len, marker='o')
    ax1.grid(True, which='both', alpha=0.3)
    ax1.set_title("Норма невязки ||b - Ax|| vs итерация")  # ← исправлено
    ax1.set_xlabel("Номер итерации")
    ax1.set_ylabel("Евклидова норма")

    # График погрешностей
    ax2.semilogy(errors_len, marker='o', color='orange')
    ax2.grid(True, which='both', alpha=0.3)
    ax2.set_title("Норма погрешности ||x* - x|| vs итерация")  # ← исправлено
    ax2.set_xlabel("Номер итерации")
    ax2.set_ylabel("Евклидова норма")
    
    plt.tight_layout()  # чтобы заголовки и подписи не наезжали
    plt.show()
        
if __name__ == "__main__":
    main()
