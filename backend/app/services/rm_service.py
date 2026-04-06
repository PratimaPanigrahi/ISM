def calculate_rm_from_ssim(grid):
    print("rm_service.py is being executed")

    """
    Convert SSIM grid (with headers) to:
    - Binary Reachability Matrix
    - Driving Power
    - Dependence Power
    """

    n = len(grid) - 1  # exclude header row & column

    # Initialize RM
    rm = [[0 for _ in range(n)] for _ in range(n)]

    # Diagonal = 1
    for i in range(n):
        rm[i][i] = 1

    # Process upper triangle only
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            val = grid[i][j].strip().upper()

            if val == "V":
                rm[i - 1][j - 1] = 1
                rm[j - 1][i - 1] = 0

            elif val == "A":
                rm[i - 1][j - 1] = 0
                rm[j - 1][i - 1] = 1

            elif val == "X":
                rm[i - 1][j - 1] = 1
                rm[j - 1][i - 1] = 1

            else:  # O or -
                rm[i - 1][j - 1] = 0
                rm[j - 1][i - 1] = 0

    # Driving & Dependence Power
    driving_power = [sum(row) for row in rm]
    dependence_power = [
        sum(rm[i][j] for i in range(n)) for j in range(n)
    ]

    return rm, driving_power, dependence_power
