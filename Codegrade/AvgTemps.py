temperatures = (
    ('1995', '3', ['47.3', '40.0', '38.3', '36.3', '37.4', '40.3', '41.1', '40.5', '41.6', '43.2', '46.2', '45.8',
                   '44.9', '39.4', '40.5', '42.0', '46.5', '46.2', '43.3', '41.7', '40.7', '39.6', '44.2', '47.8',
                   '45.9', '47.3', '39.8', '35.2', '38.5', '40.5', '47.0']),
    ('2010', '3', ['39.2', '36.7', '35.5', '35.2', '35.8', '33.8', '30.7', '33.2', '32.3', '33.3', '37.3', '39.9',
                   '40.8', '42.9', '42.7', '42.6', '44.8', '50.3', '52.2', '55.2', '47.2', '45.0', '48.6', '55.0',
                   '57.4', '50.9', '48.6', '46.2', '49.6', '50.1', '43.6']),
    ('2020', '3', ['43.2', '41.1', '40.0', '43.6', '42.6', '44.0', '44.0', '47.9', '46.6', '50.5', '51.5', '47.7',
                   '44.7', '44.0', '48.9', '45.3', '46.6', '49.7', '47.2', '44.8', '41.8', '40.9', '41.0', '42.7',
                   '43.4', '44.0', '46.4', '45.5', '40.7', '39.5', '40.6'])
)


def findEqual9510():
    temps_float_95 = [float(temp) for temp in (temperatures[0])[2]]
    temps_float_10 = [float(temp) for temp in (temperatures[1])[2]]
    print(len(set(temps_float_95).intersection(set(temps_float_10))))


def findEqual9520():
    temps_float_95 = [float(temp) for temp in (temperatures[0])[2]]
    temps_float_20 = [float(temp) for temp in (temperatures[2])[2]]
    print(len(set(temps_float_95).intersection(set(temps_float_20))))


def findHighestTemp():
    year = 0
    maxTemps = []
    while year <= 2:
        maxTemps.append(max((temperatures[year])[2]))
        year += 1
        maxTemp = max(maxTemps)
        warmestDay = maxTemps.index(maxTemp)
    print((temperatures[warmestDay])[0])


def findWarmestMarch():
    year = 0
    averageTemps = []
    while year <= 2:
        sumTemps = 0
        for element in ((temperatures[year])[2]):
            sumTemps += float(element)
        year += 1
        averageTemps.append(round((sumTemps / (len((temperatures[0])[2]))), 2))
        maxAvg = max(averageTemps)
        warmestMarch = averageTemps.index(maxAvg)
    print(temperatures[warmestMarch])


if __name__ == "__main__":
    findEqual9510()
    findEqual9520()
    findHighestTemp()
    findWarmestMarch()