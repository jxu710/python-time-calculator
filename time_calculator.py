def add_time(start, duration, days_of_week=''):
  new_time = ''


  # Days of the week list
  days_of_week_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  
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

  # calculate how many days later based on total hour in 24h floor divided 24 
  days_later = new_time_hour_24  // 24
  # if minutes is in single digit, add "0" before
  if len(str(new_time_mins)) == 1:
    str_new_time_mins = "0" + str(new_time_mins)
  else:
    str_new_time_mins = str(new_time_mins)

  # convert the hour in 24h format back to 12h format
  if new_time_hour_24 >= 24:
      new_time_hour_24 %= 24  

  if new_time_hour_24 == 0:
      str_new_time_hour_12 = "12:" + str_new_time_mins + " AM"
  elif new_time_hour_24 > 12:
      str_new_time_hour_12 = str(new_time_hour_24 - 12) + ":" + str_new_time_mins + " PM"
  elif new_time_hour_24 == 12:
      str_new_time_hour_12 = str(new_time_hour_24) + ":" + str_new_time_mins + " PM"
  else:
    str_new_time_hour_12 = str(new_time_hour_24) + ":" + str_new_time_mins + " AM"


  
  if days_later == 1:
    new_time += str_new_time_hour_12 + " (next day)"
  elif days_later > 1:
    new_time += str_new_time_hour_12 + f" ({days_later} days later)"
  else:
    new_time += str_new_time_hour_12

  # if days of the week is not empty, add the day of the week to the new time
  if days_of_week:
  
    index = days_of_week_list.index(days_of_week.lower().capitalize())

    # Update the day_of_week based on days_later
    new_index = (index + days_later) % 7
    new_day_of_week = days_of_week_list[new_index]

    new_time = f"{str_new_time_hour_12}, {new_day_of_week} ({days_later} days later)"

    if days_later == 1:
      return f"{str_new_time_hour_12}, {new_day_of_week} (next day)"
    elif days_later == 0:
      return f"{str_new_time_hour_12}, {days_of_week}"
  return new_time


print(add_time("2:59 AM", "24:00", "saturDay"))
print(add_time("3:00 PM", "3:10")) 
print(add_time("11:30 AM", "2:32", "Monday")) 
print(add_time("11:43 AM", "00:20")) 
print(add_time("10:10 PM", "3:30")) 
print(add_time("11:43 PM", "24:20", "tueSday")) 
print(add_time("6:30 PM", "205:12"))
print(add_time("3:30 PM", "2:12", "Monday"))