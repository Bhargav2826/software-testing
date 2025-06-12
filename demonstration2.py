from datetime import datetime

versions = {}
log = []

def update(name, ver):
    action = "Added" if name not in versions else f"Updated {versions[name]} -> {ver}"
    versions[name] = ver
    log.append((datetime.now().strftime("%Y-%m-%d %H:%M:%S"), name, action))

def show():
    print("Versions:", versions)
    print("Log:")
    for time, name, action in log:
        print(f"[{time}] {name}: {action}")

# Example
update("Python", "3.10")
update("NodeJS", "16")
update("Python", "3.11")
show()
