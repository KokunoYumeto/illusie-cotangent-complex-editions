"""Finite type/map check for the correction of I (1.2.2.1), pp. 7–8.

The printed shuffle uses positions 1,...,p+q, whereas I (1.1.1)
indexes codegeneracies from zero. Function composition is right to left.
This checks the two monotone surjections only, not the shuffle sign or
chain-map/homotopy theorem. Run explicitly with Python 3.
"""
from itertools import combinations


def compose_codegeneracies(degree, execution_indices):
    values = list(range(degree + 1))
    for index in execution_indices:
        if not 0 <= index < degree:
            return {"valid": False, "degree_before": degree, "bad_index": index}
        values = [value if value <= index else value - 1 for value in values]
        degree -= 1
    return {"valid": True, "degree_after": degree, "values": values}


def main():
    print("Printed p=0,q=1:", compose_codegeneracies(1, [1]))
    print("Shifted but unreversed p=0,q=2:", compose_codegeneracies(2, [0, 1]))
    print("Shifted and reversed p=0,q=2:", compose_codegeneracies(2, [1, 0]))
    count = 0
    for p in range(5):
        for q in range(5):
            degree = p + q
            for mu in combinations(range(1, degree + 1), p):
                nu = tuple(k for k in range(1, degree + 1) if k not in mu)
                for collapsed, remaining, target in [(nu, mu, p), (mu, nu, q)]:
                    result = compose_codegeneracies(
                        degree, [k - 1 for k in reversed(collapsed)]
                    )
                    expected = [
                        sum(k <= t for k in remaining) for t in range(degree + 1)
                    ]
                    assert result["valid"]
                    assert result["degree_after"] == target
                    assert result["values"] == expected
                count += 1
    print(f"PASS: both factors for all {count} shuffles with 0<=p,q<=4.")


if __name__ == "__main__":
    main()
