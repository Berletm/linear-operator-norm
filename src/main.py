import numpy as np

# var 2
OPERATOR = np.array([
    [  333/11,   288/11,   18/11,  270/11],
    [  819/22,  1305/22, -315/11,  324/11],
    [-1257/44, -1773/44,  453/22, -315/11],
    [  -81/44,  -549/44,  351/22,  108/11]
])


def main() -> None:
    # l1 norm
    print("Норма в l1", np.linalg.norm(OPERATOR, ord=1))
    
if __name__ == "__main__":
    main()
