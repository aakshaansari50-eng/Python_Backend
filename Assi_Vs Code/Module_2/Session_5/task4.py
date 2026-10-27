team = {
    "CSK": {"captain": "Dhoni", "players": 18},
    "MI": {"captain": "Rohit", "players": 17}
}

team["GT"] = {"captain": "Hardik", "players": 16}

for name, details in team.items():
    print(name, "-", details["captain"])