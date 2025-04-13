#Ahmed Raza
#Set Operations
colors = {"red", "green", "blue"}
print("Original set:", colors)

# Adding elements
colors.add("yellow")
print("After add('yellow'):", colors)

# Updating with multiple elements
colors.update(["orange", "purple"])
print("After update(['orange', 'purple']):", colors)

# Removing elements
colors.remove("green")
print("After remove('green'):", colors)

# Discard (no error if missing)
colors.discard("pink")
print("After discard('pink'):", colors)

# Pop random element
popped = colors.pop()
print(f"After pop(): {popped} removed, remaining:", colors)

# Set Operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("\nSet Operations:")
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))

# Set Comparisons
print("\nSet Comparisons:")
print("Is subset:", {1, 2}.issubset(set1))
print("Is superset:", set1.issuperset({1, 2}))
print("Is disjoint:", set1.isdisjoint({5, 6}))

# Clearing set
set1.clear()
print("\nAfter clear():", set1)


print("\n=== Frozensets ===")

# Frozenset creation
fset = frozenset(["a", "b", "c"])
print("Original frozenset:", fset)

# Frozenset operations (immutable but supports queries)
fset2 = frozenset(["b", "c", "d"])

print("\nFrozenset Operations:")
print("Union:", fset.union(fset2))
print("Intersection:", fset.intersection(fset2))
print("Difference:", fset.difference(fset2))
print("Symmetric Difference:", fset.symmetric_difference(fset2))

import gc

gc.collect()
print(gc.get_count())