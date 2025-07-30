def solve(haab_date: str) -> str:
    haab_months = [
        "pop", "no", "zip", "zotz", "tzec", 
        "xul", "yoxkin", "mol", "chen", "yax", 
        "zac", "ceh", "mac", "kankin", "muan", 
        "pax", "koyab", "cumhu"
    ]

    tzolkin_days = [
        "imix", "ik", "akbal", "kan", "chicchan", 
        "cimi", "manik", "lamat", "muluk", "ok", 
        "chuen", "eb", "ben", "ix", "mem", 
        "cib", "caban", "eznab", "canac", "ahau"
    ]

    day, month, year = haab_date.split()
    day, year = int(day.strip('.')), int(year)

    mo = haab_months.index(month)
    tmp = year*365 + (mo*20) + day
    
    tz_num = (tmp%13) + 1
    tz_name = tzolkin_days[tmp%20]
    tz_year = tmp//260

    return f"{tz_num} {tz_name} {tz_year}"


print(solve("10. zac 0"))
print(solve("0. pop 0"))
print(solve("10. zac 1995"))
