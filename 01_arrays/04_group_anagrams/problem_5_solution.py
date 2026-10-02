def group_orders(orders):
    groups = {}

    for order in orders:
        key = tuple(sorted(order))

        if key not in groups:
            groups[key] = []

        groups[key].append(order)

    return list(groups.values())
