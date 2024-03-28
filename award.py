swimming_event = int(input("Swimming time: "))
running_event = int(input("Running time: "))
cycle_event = int(input("Cycling time: "))
total_time = swimming_event + running_event + cycle_event
print(total_time, "minutes")

if total_time <= 100:
    print("Awarded: Provincial colours")
elif total_time <= 105:
    print("Awarded: Provincial half colours")
elif total_time <= 110:
    print("Awarded: Provincial scroll")

else: 
    print("No Award")
  