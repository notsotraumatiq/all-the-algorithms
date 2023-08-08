def booked_rooms(booked_rooms):

    count = 0
    current_room = ""
    for i in range(len(booked_rooms)):
        if booked_rooms[i][0] == "-":
            count -= 1
        elif booked_rooms[i][0] == "+":
            if current_room == "":
                current_room = booked_rooms[i][1:]
                count = 1
            elif current_room == booked_rooms[i][1:]:
                count += 1
            else:
                count -= 1
        if count == 0:
            current_room = booked_rooms[i][1:]
            count = 1


    return current_room



print(booked_rooms(["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"]))



