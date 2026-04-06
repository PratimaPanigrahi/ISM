def calculate_level_partition(frm, variables):
    n = len(frm)

    elements_data = []
    remaining = set(range(n))
    level_number = 1

    matrix = [row[:] for row in frm]

    while remaining:
        current_level = []

        for i in remaining:
            # Only consider remaining elements
            reachability = {j for j in remaining if matrix[i][j] == 1}
            antecedent = {j for j in remaining if matrix[j][i] == 1}

            intersection = reachability & antecedent

            if reachability == intersection:
                current_level.append(i)

        # Safety check (prevents infinite loop)
        if not current_level:
            break

        for i in current_level:
            reachability = [variables[j] for j in remaining if matrix[i][j] == 1]
            antecedent = [variables[j] for j in remaining if matrix[j][i] == 1]
            intersection = list(set(reachability) & set(antecedent))

            elements_data.append({
                "element": variables[i],
                "reachability": reachability,
                "antecedent": antecedent,
                "intersection": intersection,
                "level": level_number
            })

        # Remove identified level elements
        remaining -= set(current_level)

        level_number += 1

    return elements_data