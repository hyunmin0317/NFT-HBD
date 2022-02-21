years = [1,2,3,4,5,6,7,8,9,10,11,12]
days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for year in years:
    for day in range(1, days[year-1]+1):
        hbd = "%02d.%02d"%(year, day)
        print(hbd)