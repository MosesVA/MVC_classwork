class TimeTableView:
    def __init__(self, controller):
        self.controller = controller

    def print_default_action(self):
        print(self.controller.default_action())

    def print_courses_list(self):
        print(self.controller.only_courses_list())

    def print_dates_list(self):
        print(self.controller.only_dates_list())

    def print_courses_dates(self):
        print(self.controller.courses_dates())

    def add_date(self, course, date, filename, validation='user'):
        # if validation in ['is_superuser', 'is_stuff']:
        #     self.controller.add_date(course, date, filename)
        #     print('Дата успешно добавлена!')
        # else:
        #     print('Нет доступа!')
        print(self.controller.add_date(course, date, filename, validation))
