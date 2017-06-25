import jellybean
import easy_cereal
import time
import urllib

while True:
    try:
        info = jellybean.bart_info()
    except urllib.error.URLError:
        print('handling error')
        continue
    display = easy_cereal.Display()
    for station in info:
        display.print(station)
        display.new_line()
        for train in info[station][1]:
            if (train[0].lower() == 'leaving'):
                display.print("%s. L%s" % (train))
            else:
                display.print("%s min. L%s" % (train))
            display.new_line()
    time.sleep(5)
