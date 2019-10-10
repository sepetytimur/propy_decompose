from aplications.salary import calculate_salary
from aplications.people import get_employees
from datetime import datetime, date, time
def main():
    z = datetime.today()
    a = calculate_salary()

    b = get_employees()
    print(z)

if __name__=='__main__':
    main()