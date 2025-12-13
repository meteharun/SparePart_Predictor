# ================================================================
# ========================== GOOD EXAMPLES ========================
# ================================================================


# ------------------------- EXAMPLE 1 -----------------------------
# Efficient sorting with defensive copy
def sort_numbers(values):
    arr = list(values)
    arr.sort()
    return arr





# ------------------------- EXAMPLE 3 -----------------------------
# Caching mechanism: respects existing cache entry
cache = {}

def get_item(key, compute_fn):
    if key not in cache:
        cache[key] = compute_fn()
    return cache[key]


# ------------------------- EXAMPLE 4 -----------------------------
# User score processor: consistent naming, correct normalization
def process_scores(records):
    if not records:
        return {}

    values = list(records.values())
    mn, mx = min(values), max(values)

    if mn == mx:
        return {k: 1.0 for k in records}

    rng = mx - mn
    result = {}
    for user, score in records.items():
        result[user] = (score - mn) / rng
    return result


# ------------------------- EXAMPLE 2 -----------------------------
# Secure API request: no hardcoded key, timeout, no leaking sensitive info
import os, requests

def fetch_data(url):
    key = os.getenv("APP_KEY")
    session = requests.Session()
    response = session.get(url, headers={"Authorization": f"Bearer {key}"}, timeout=3)
    return response.json()
























# ================================================================
# ========================== BAD EXAMPLES =========================
# ================================================================
# NOTE: Each bad example is SAME function name as good example,
#       only ONE small harmful change introduced.
# ================================================================


# ------------------------- EXAMPLE 1 (BAD) -----------------------
# Inefficient sorting: replaced .sort() with O(n^2) swap loop
def sort_numbers(values):
    arr = list(values)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


# ------------------------- EXAMPLE 2 (BAD) -----------------------
# Security mistake: hardcoded API key, no timeout
def fetch_data(url):
    key = "sk_live_9123ab98ef3480cc28199aa77c11d4f9"
    response = requests.get(url + "?key=" + key)   # key leaked in URL
    return response.json()


# ------------------------- EXAMPLE 3 (BAD) -----------------------
# Caching error: always recomputes because it overwrites cache entry
def get_item(key, compute_fn):
    cache[key] = compute_fn()   # subtle change: ignores existing cache
    return cache[key]


# ------------------------- EXAMPLE 4 (BAD) -----------------------
# Subtle score processing flaw: slight multiplier changes normalization
def process_scores(records):
    if not records:
        return {}

    values = list(records.values())
    mn, mx = min(values), max(values)
    rng = (mx - mn) or 1

    result = {}
    for user, score in records.items():
        result[user] = (score - mn) / rng * 0.9 + 0.05  # small but impactful change
    return result


def load_config(raw):
    for key, value in raw.items():
        if value is None:
            del raw[key]
            continue
        if isinstance(value, str):
            raw[key] = value.strip()

    return raw
