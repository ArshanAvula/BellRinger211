from datetime import datetime
both = datetime.now()
current = both.hour*60 + both.minute
end = 14*60 + 19
print("There are " + str(end - current) + " minutes left.")
