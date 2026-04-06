def generate_conical_and_reduced(frm, elements):
    """
    Generate Proper Conical and Reduced Conical Matrix
    Based strictly on Level Partition ordering
    """

    # 1️⃣ Group elements by level
    level_dict = {}
    for e in elements:
        level = e["level"]
        if level not in level_dict:
            level_dict[level] = []
        level_dict[level].append(e["element"])

    # 2️⃣ Sort levels ascending
    ordered_variables = []
    for level in sorted(level_dict.keys()):
        ordered_variables.extend(level_dict[level])

    # 3️⃣ Map original variable index
    original_vars = [e["element"] for e in elements]
    index_map = {var: i for i, var in enumerate(original_vars)}

    order = [index_map[var] for var in ordered_variables]

    # 4️⃣ Generate Conical
    conical = [
        [frm[i][j] for j in order]
        for i in order
    ]

    # 5️⃣ Proper Transitive Reduction
       # Proper Transitive Reduction (Hasse Diagram)
    n = len(conical)
    reduced = [row[:] for row in conical]

    for i in range(n):
        for j in range(n):
            if i != j and reduced[i][j] == 1:

                # Temporarily remove edge
                reduced[i][j] = 0

                # Check if alternate path exists
                stack = [i]
                visited = set()

                found = False

                while stack:
                    node = stack.pop()
                    if node == j:
                        found = True
                        break

                    for k in range(n):
                        if reduced[node][k] == 1 and k not in visited:
                            visited.add(k)
                            stack.append(k)

                # If no alternate path, restore edge
                if not found:
                    reduced[i][j] = 1

    return conical, reduced, ordered_variables