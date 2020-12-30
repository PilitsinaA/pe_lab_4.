import csv
import pickle

class Practic_2_4:
    def __init__(self):
        self.stlist = [[None for x in range(4)] for y in range(9)]

    def students(self):
        with open('C:/Users/Systema/Desktop/мага/программнаяинженерия/students.csv', encoding='UTF-8') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print('Загаловок был прочитан')
                    line_count += 1
                else:
                    for i in range(4):
                        self.stlist[line_count-1][i] = row[i]
                    print('Значения записаны в строку')
                    line_count += 1
            print(self.stlist)


    def sort_by_name(self):
        self.stlist.sort(key=lambda student: student[1])
        print('Сортировка по имени:\n', self.stlist)


    def sort_by_age_22(self):
        age_22 = []
        for student in self.stlist:
            if int(student[2])>22:
                age_22.append(student)
        print('Возраст>22:\n', age_22)

    def write_to_file_csv(self, filename='practic_2_3'):
        name = filename + '.csv'
        with open (name, 'w') as f:
            thewriter = csv.writer(f, delimiter=';', lineterminator = '\n')
            thewriter.writerow(['#', 'ФИО', 'Возраст', 'Группа'])
            thewriter.writerows(self.stlist)
        f.close()

    def save_to_pickle_file(self):
        with open('test.pickle', 'wb') as p:
            pickle.dump(self.stlist, p)
            print('saved in pickle file')
        p.close()

    def read_from_pickle_file(self):
        with open('test.pickle', 'rb') as r:
            stlist = pickle.load(r)
            print('read from pickle file')
            print(stlist)
        r.close()

obj1 = Practic_2_4()
obj1.students()

obj1.sort_by_name()

obj1.sort_by_age_22()

#obj1.write_to_file_csv()
#print('Файл записан ".csv" file')

obj1.stlist.append(['78', 'Пупкин Александр Олеговия', '221', 'БО-202322'])
obj1.write_to_file_csv('practic_4_2_3')
print('ещё один студент добавлен в файл')

obj1.save_to_pickle_file()
obj1.read_from_pickle_file()

    

