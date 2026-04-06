def calculate_frm(rm):
    """
    Warshall algorithm for transitive closure.
    Also calculates Driving Power & Dependence Power.
    """

    n = len(rm)
    frm = [row[:] for row in rm]  # deep copy

    # Warshall Transitive Closure
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if frm[i][j] == 1 or (frm[i][k] == 1 and frm[k][j] == 1):
                    frm[i][j] = 1

    # Driving Power (row sum)
    driving_power = [sum(row) for row in frm]

    # Dependence Power (column sum)
    dependence_power = [
        sum(frm[i][j] for i in range(n)) for j in range(n)
    ]

    return frm, driving_power, dependence_power