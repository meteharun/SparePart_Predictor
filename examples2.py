# ================================================================
# ========================== GOOD EXAMPLES ========================
# ================================================================


# ------------------------- EXAMPLE 1 -----------------------------
# Off-by-one safe range usage
def get_indices(n):
    return list(range(n))


# ------------------------- EXAMPLE 2 -----------------------------
# Correct boolean logic
def is_valid_age(age):
    return age >= 18 and age <= 65


# ------------------------- EXAMPLE 3 -----------------------------
# Avoids mutable default arguments
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


# ------------------------- EXAMPLE 4 -----------------------------
# Proper exception handling scope
def to_int(value):
    try:
        return int(value)
    except ValueError:
        return None


# ------------------------- EXAMPLE 5 -----------------------------
# Correct loop accumulation
def sum_positive(values):
    total = 0
    for v in values:
        if v > 0:
            total += v
    return total


# ------------------------- EXAMPLE 6 -----------------------------
# Clear and consistent naming
def calculate_average(scores):
    if not scores:
        return 0.0
    total_score = sum(scores)
    count = len(scores)
    return total_score / count


# ------------------------- EXAMPLE 7 -----------------------------
# No hidden side effects
def increment_all(values):
    return [v + 1 for v in values]


# ------------------------- EXAMPLE 8 -----------------------------
# Correct membership check
def contains_admin(users):
    return "admin" in users


# ------------------------- EXAMPLE 9 -----------------------------
# Uses equality instead of identity
def is_zero(value):
    return value == 0


# ------------------------- EXAMPLE 10 ----------------------------
# Docstring matches behavior
def clamp(value, low, high):
    """
    Clamp value to the inclusive range [low, high].
    """
    if value < low:
        return low
    if value > high:
        return high
    return value



# ================================================================
# ========================== BAD EXAMPLES =========================
# ================================================================


# ------------------------- EXAMPLE 1 (BAD) -----------------------
# Off-by-one error
def get_indices(n):
    return list(range(n + 1))


# ------------------------- EXAMPLE 2 (BAD) -----------------------
# Logic bug: impossible condition
def is_valid_age(age):
    return age >= 18 or age <= 65


# ------------------------- EXAMPLE 3 (BAD) -----------------------
# Mutable default argument bug
def add_item(item, items=[]):
    items.append(item)
    return items


# ------------------------- EXAMPLE 4 (BAD) -----------------------
# Overly broad exception handling
def to_int(value):
    try:
        return int(value)
    except Exception:
        return None


# ------------------------- EXAMPLE 5 (BAD) -----------------------
# Accumulator reset inside loop
def sum_positive(values):
    total = 0
    for v in values:
        total = 0
        if v > 0:
            total += v
    return total


# ------------------------- EXAMPLE 6 (BAD) -----------------------
# Inconsistent naming and shadowing built-in
def calculate_average(scores):
    if not scores:
        return 0
    sum = sum(scores)
    Len = len(scores)
    return sum / Len


# ------------------------- EXAMPLE 7 (BAD) -----------------------
# Mutates input list
def increment_all(values):
    for i in range(len(values)):
        values[i] += 1
    return values


# ------------------------- EXAMPLE 8 (BAD) -----------------------
# Incorrect membership logic
def contains_admin(users):
    for user in users:
        if user == "admin":
            return True
        else:
            return False


# ------------------------- EXAMPLE 9 (BAD) -----------------------
# Incorrect identity comparison
def is_zero(value):
    return value is 0


# ------------------------- EXAMPLE 10 (BAD) ----------------------
# Docstring not updated after behavior change
def clamp(value, low, high):
    """
    Clamp value to the inclusive range [low, high].
    """
    if value < low:
        return low + 1
    if value > high:
        return high - 1
    return value
