class format:
  def dates(date):
    if date.month == 1:
      month = 'Jan'
    if date.month == 2:
      month = 'Feb'
    if date.month == 3:
      month = 'Mar'
    if date.month == 4:
      month = 'Apr'
    if date.month == 5:
      month = 'May'
    if date.month == 6:
      month = 'Jun'
    if date.month == 7:
      month = 'Jul'
    if date.month == 8:
      month = 'Aug'
    if date.month == 9:
      month = 'Sep'
    if date.month == 10:
      month = 'Oct'
    if date.month == 11:
      month = 'Nov'
    if date.month == 12:
      month = 'Dec'
    return f'{month}. {date.day}, {date.year}'

class calculate:
  def dates(start, end):
    if start != end:
      years = end.year - start.year
      months = (12 - end.month) + (12 - start.month)
      if months > 12:
        years += 1
        months -= 12
      thirty = [4, 6, 9, 11]
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
