def add_time(start, duration, days_of_week=''):
  new_time = ''
  # get hour out of start time
  start_time = start.split(" ")[0]
  hour = start_time.split(":")

  # if start time is pm, transfer hour to 24h format
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

  # new time's minutes
  new_time_mins = mins + duration_mins
  if new_time_mins >= 60:
    new_time_mins = new_time_mins - 60
    new_time_hour_24 = new_time_hour_24 + 1

  # if minutes is in single digit, add "0" before 
  if len(str(new_time_mins)) == 1:
    str_new_time_mins = "0" + str(new_time_mins)
  else:
    str_new_time_mins = str(new_time_mins)

  # add 'next day' if pass midnight
  new_time_in_12 = new_time_hour_24 - 12
  if new_time_in_12 >= 12:
    time_of_day = "AM"
    new_time_in_12 = new_time_in_12 - 12
    new_time = str(
        new_time_in_12
    ) + ":" + str_new_time_mins + " " + time_of_day + " " + "(next day)"
  if new_time_in_12 == 0:
      new_time_in_12 = 12

  new_time = str(
      new_time_in_12) + ":" + str_new_time_mins + " " + time_of_day

  # if days of week is inputted
  if days_of_week != '':
    new_time = new_time + "," + " " + days_of_week

  return new_time


print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))
