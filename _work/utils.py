class format:
  def dates(date:str):
    date = date.split('-')
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    if month == 1:
      month = 'Jan'
    elif month == 2:
      month = 'Feb'
    elif month == 3:
      month = 'Mar'
    elif month == 4:
      month = 'Apr'
    elif month == 5:
      month = 'May'
    elif month == 6:
      month = 'Jun'
    elif month == 7:
      month = 'Jul'
    elif month == 8:
      month = 'Aug'
    elif month == 9:
      month = 'Sep'
    elif month == 10:
      month = 'Oct'
    elif month == 11:
      month = 'Nov'
    elif month == 12:
      month = 'Dec'
    return f'{month}. {day}, {year}'

class calculate:
  def dates(start, end):
    if start != end:
      start = start.split('-')
      start_year = int(start[0])
      start_month = int(start[1])
      start_day = int(start[2])
      end = end.split('-')
      end_year = int(end[0])
      end_month = int(end[1])
      end_day = int(end[2])
      years = end_year - start_year
      months = (12 - end_month) + (12 - start_month)
      if months > 12:
        years += 1
        months -= 12
      return (years, months, 0)
    return (0, 0, 0)

class generate:
  def element_id(element):
    from .models import Entry, Position, Duty
    if element == 'entry':
      count = Entry.objects.count()
      count += 1
      return f'E{count}'
    elif element == 'position':
      count = Position.objects.count()
      count += 1
      return f'P{count}'
    elif element == 'duty':
      count = Duty.objects.count()
      count += 1
      return f'D{count}'
