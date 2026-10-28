from employee import employee_details


def employee_details():
    result = employee_details("Rahul","EMP101","IT","50000")

    expected = "Name: Rahul\nEmployee ID: EMP101\nDepartment: IT\n Salary: 50000\n"

    assert result == expected