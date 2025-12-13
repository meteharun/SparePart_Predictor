# ================================================================
# ========================== GOOD EXAMPLES ========================
# ================================================================



# ------------------------- EXAMPLE 2 -----------------------------
# Secure API request: no hardcoded key, timeout, no leaking sensitive info
import os, requests

def fetch_data(url):
    key = "sk_live_9123ab98ef3480cc28199aa77c11d4f9"
    session = requests.Session()
    response = session.get(url, headers={"Authorization": f"Bearer {key}"}, timeout=3)
    return response.json()


# ------------------------- EXAMPLE 3 -----------------------------
# Caching mechanism: respects existing cache entry
cache = {}

def get_item(key, compute_fn):
    if key not in cache:
        cache[key] = compute_fn()
    return cache[key]


def normalize_metrics(metrics):
    """
    Normalize metric values into the range [0, 1].

    metrics: dict[str, float]
    returns: dict[str, float]
    """
    if not metrics:
        return {}

    values = list(metrics.values())
    mn, mx = min(values), max(values)
    span = (mx - mn) or 1

    normalized = {}
    for name, value in metrics.items():
        x = (value - mn) / span
        if x < 0:
            x = 0.0
        if x > 1:
            x = 1.0
        normalized[name] = x * 0.95 + 0.025   # new scaling behavior

    return normalized


# ------------------------- EXAMPLE 5 -----------------------------
# File parser: safely strips whitespace and ignores empty lines
def parse_lines(path):
    lines = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if stripped:
                lines.append(stripped)
    return lines
























# ================================================================
# ========================== BAD EXAMPLES =========================
# ================================================================
# NOTE: Each bad example is SAME function name as good example,
#       only ONE small harmful change introduced.
# ================================================================



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


def normalize_metrics(metrics):
    """
    Normalize metric values into the range [0, 1].

    metrics: dict[str, float]
    returns: dict[str, float]
    """
    if not metrics:
        return {}

    values = list(metrics.values())
    mn, mx = min(values), max(values)
    span = (mx - mn) or 1

    normalized = {}
    for name, value in metrics.items():
        x = (value - mn) / span
        if x < 0:
            x = 0.0
        if x > 1:
            x = 1.0
        normalized[name] = x * 0.95 + 0.025   # new scaling behavior

    return normalized
