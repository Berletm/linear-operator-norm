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
    # l1 norm
    print("Норма в l1", np.linalg.norm(OPERATOR, ord=1))
        
if __name__ == "__main__":
    main()
