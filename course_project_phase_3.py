def get_data(filename):
    while True:
        date = input('Enter the "from date" in mm/dd/yyyy format or "all": ')
        try:
            date_attributes = list(map(int,date.split('/')))
            if 1 <= date_attributes[0] <= 12 and 1 <= date_attributes[1] <= 31:
                break
            else:
                print('Enter the date in mm/dd/yyyy format or "all".')
        except: 
            if date.lower() == 'all':
                break
            else:
                print('Enter the date in mm/dd/yyyy format or "all".')

    data_dict = {
        'total_employee': 0,
        'total_hours' : 0,
        'total_tax' : 0,
        'total_net_pay' : 0
        }

    with open(filename) as file:
        data = file.readlines()

    print('{:<15} {:<15} {:<25} {:<15} {:<12} {:<8} {:<15} {:<12} {:<15}' .format(
            'From Date',
            'To Date',
            'Employee Name',
            'Hours Worked',
            'Gross Pay',
            'Income Tax Rate',
            'Income Taxes',
            'Net Pay'))
    for line in data:
        line = line.split('|')
        from_date = line[0]
        from_date_attributes = list(map(int,date.split('/')))

        try:
            if from_date_attributes[2] >= date_attributes[2]:
                if from_date_attributes[1] >= date_attributes[1]:
                    if from_date_attributes[0] >= date_attributes[0]:
                        pass
                    else:
                        continue
                else:
                    continue
            else:
                continue
        except:
            pass

        to_date = line[1]
        employee_name = line[2]
        hours_worked = float(line[3])
        pay_rate = float(line[4])
        income_tax_rate = float(line[5])
        gross_pay = hours_worked * pay_rate
        income_taxes = gross_pay * (income_tax_rate/100)
        net_pay = gross_pay - income_taxes

        data_dict['total_employee'] += 1
        data_dict['total_hours'] += hours_worked
        data_dict['total_tax'] += income_taxes
        data_dict['total_net_pay'] += net_pay

        print('{<15} {:<15} {:<25} {:<15} {:<12} {:<8} {:<15} {:<12} {:<15}' .format(
            from_date,
            to_date,
            employee_name,
            hours_worked,
            pay_rate,
            gross_pay,
            income_tax_rate,
            income_taxes,
            net_pay))

        print('{:<30} {:<15} {:<20} {:<20}'.format(
                'Total Numbers of Employees',
                'Total Hours',
                'Total Tax',
                'Total Net Pay'))

        print('{:<30} {:<15} {:<20} {:<20}'.format(
                data_dict['total_employee'],
                data_dict['total_hours'],
                data_dict['total_tax'],
                data_dict['total_net_pay']))

data_list = []

while True:
    print('Enter the following details: ')
    from_date = input('Enter the from date: ')
    to_date = input('Enter the to date: ')
    employee_name = input('Enter the employee name: ')
    hours_worked = input('Enter the hours worked: ')
    pay_rate = input('Enter the pay rate: ')
    income_tax_rate = input('Enter the income tax rate: ')

data_list.append(from_date+'|'+to_date+'|'+employee_name+'|'+hours_worked+'|'+pay_rate+'|'+income_tax_rate+'\n')

choice = input('Enter "Q" to quit or any key to continue adding more employees: ').lower()
if choice == 'q':
    print()

file_name = 'data.text'

with open(file_name, 'a') as file:
    file.writelines(data_list)

get_data(file_name)
  



