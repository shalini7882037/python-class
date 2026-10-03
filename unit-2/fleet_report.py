def battery_band(pct):
    """Classifying battery percentage into a band."""
    if pct < 15:
        return "CRITICAL"
    elif pct < 30:
        return "LOW"
    return "OK"
 
print("Alpha:", battery_band(45))
print("Beta :", battery_band(3))
print("Gamma:", battery_band(25))
