from TimeTableModel import TimeTableModel
from View import TimeTableView
from Controller import TimeTableController


model = TimeTableModel()
controller = TimeTableController(model)
view = TimeTableView(controller)

view.print_default_action()
view.print_courses_list()
view.print_dates_list()
view.print_courses_dates()
view.add_date('HTML', 'Dec 01', 'dates_file.json', 'is_stuff')
view.add_date('CSS', 'Jun 08', 'dates_file.json', 'is_stuff')
view.add_date('JavaScript', 'Feb 03', 'dates_file.json', 'is_stuff')
view.add_date('Python', 'Apr 22', 'dates_file.json')
view.print_default_action()
view.print_courses_list()
view.print_dates_list()
view.print_courses_dates()
