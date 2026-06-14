# Bug Report

**Date:** 15 June 2026

---

## Bug 1

### Description
Detailed Project Information section displayed only 20 projects.

### Cause
The code used:

```python
filtered_df.head(20)
```

### Resolution
Replaced with:

```python
filtered_df.iterrows()
```

### Status
Resolved

---

## Bug 2

### Description
Location names appeared inconsistent.

### Examples
- NE
- Northeast
- India, India

### Resolution
Implemented location normalization rules.

### Status
Partially Resolved

---

## Bug 3

### Description
Project explorer section appeared empty during testing.

### Cause
Filtered dataset returned no records under certain filter combinations.

### Resolution
Added validation and empty dataset handling.

### Status
Resolved

---

## Critical Bugs

No critical bugs found.

---

## Final Assessment

The application is functioning correctly and all major modules operate as expected.