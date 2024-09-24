def percetable_greater_than(rider, competitor, seconds):

    rider.sort(key=lambda x: x[0])
    competitor.sort(key=lambda x: x[0])
    last_rider_time = 0
    last_competitor_time = 0
    better_than = False
    result_interval = 0
    for rider_interval, competitor_interval in zip(rider, competitor):
        rider_time, rider_watt = rider_interval
        competitor_time, competitor_watt = competitor_interval

        if rider_watt > competitor_watt:
            result_interval += rider_time - last_competitor_time
        else:
            last_competitor_time = competitor_time
            last_rider_time = rider_time

    if last_rider_time != seconds and rider[-1][1] > competitor[-1][1]:
        result_interval += seconds - rider[-1][0]


    return result_interval

print(percetable_greater_than([(10,70),(200,80),(250,90)], [(10,75), (50,84),(200,100)], 300))
