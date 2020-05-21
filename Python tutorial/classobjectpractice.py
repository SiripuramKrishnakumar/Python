class employee:
    def __init__(self):
        self.name = 'fdsdsf'
        self.Age = 45
        self.phn = 8768767673
        self.depart = self.Department()

    class Department:
        Name = 'dgjydfygids'

        def __init__(self):
            self.Name = 'API'
            self.Code = 'AA'
            self.Manager = 'sdfhsdiguh'


employee1 = employee()

dep1 = employee1.Department()
print(employee1.name)
print(employee1.Department.Name)
print(dep1.Name,dep1.Manager)

dep2 = employee.Department()
