def add_time(start, duration):
  new_time = ""

  # get hour out of start time
  start_time = start.split(" ")[0]
  hour = start_time.split(":")

  time_of_day = start.split(" ")[1]
  if time_of_day == "PM":
    hour[0] = str(int(hour[0]) + 12)

  # get minutes out of start time
  mins = int(hour[1])

  # get the duration time and add to start time
  duration_time = duration.split(":")
  duratiom_hour = int(duration_time[0])
  duration_mins = int(duration_time[1])

  # new time's hour digit
  new_time_hour_24 = int(hour[0]) + duratiom_hour
  new_time_in_12 = new_time_hour_24 - 12

  # new time's minutes
  new_time_mins = mins + duration_mins
  if new_time_mins >= 60:
    new_time_mins = new_time_mins - 60
    new_time_hour_24 + 1

  print(duration_mins)


  
  return new_time


print(add_time("3:00 PM", "3:10"))
