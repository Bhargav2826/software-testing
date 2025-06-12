# defect list
defects = [
    (101, "Login fails", "User cannot login with correct credentials", "Critical"),
    (102, "Alignment issue", "Button alignment is off in Firefox", "Minor"),
    (103, "Crash on upload", "App crashes while uploading file", "Critical"),
    (104, "Slow response", "Dashboard takes too long to load", "Major"),
    (105, "Typo in label", "Misspelling in the settings menu", "Minor"),
    (106, "Feature not saving", "Settings changes are not retained", "Major")
]
# defect categorize
categorized_defects = {
    "Critical": [],
    "Major": [],
    "Minor": []
}
# Categorize each defect based on severity
for defect in defects:
    id, title, description, severity = defect
    if severity in categorized_defects:
        categorized_defects[severity].append(defect)
    else:
        print(f"Unknown severity '{severity}' in defect ID {id}")
        
# Display categorized defects
print("Software Defect Categorization:\n")
for severity, defect_list in categorized_defects.items():
    print(f"{severity} Defects:")
    if defect_list:
        for d in defect_list:
            print(f"  ID: {d[0]}, Title: {d[1]}, Description: {d[2]}")
    else:
        print("  No defects in this category.")
    print("-" * 50)
