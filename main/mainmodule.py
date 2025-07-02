from decimal import Decimal
from Dao.reportgeneratorservice import ReportGenerator
from util.DBPropertyUtil import get_db_config
from util.DBConnUtil import get_connection
from Exception.employeenotfoundexception import EmployeeNotFoundException
from Exception.payrollgenerationexception import PayrollGenerationException
from Exception.taxcalculationexception import TaxCalculationException
from Exception.financialrecordexception import FinancialRecordException
from Exception.invalidinputexception import InvalidInputException
from Exception.databaseconnectionexception import DatabaseConnectionException
from Dao import EmployeeService, PayrollService, TaxService, FinancialRecordService
from Entity.employees import Employees
from Entity.payroll import payroll
from Entity.tax import tax
from Entity.financial_record import FinancialRecord
import datetime
from tabulate import tabulate

def main():
    try:
        config = get_db_config()
        conn = get_connection(config)
    except Exception:
        raise DatabaseConnectionException("Failed to connect to the database.")

    employee_service = EmployeeService(conn)
    payroll_service = PayrollService(conn)
    tax_service = TaxService(conn)
    financial_record_service = FinancialRecordService(conn)
    report_generator = ReportGenerator(conn)

    while True:
        print("\n--- PayXpert Payroll Management System ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Find Employee by ID")
        print("4. Remove Employee")
        print("5. Generate Payroll")
        print("6. View Payrolls for Employee")
        print("7. Record Tax")
        print("8. Record Financial Transaction")
        print("9. Generate Report (All Employees)")
        print("10. Calculate Tax by Employee ID")
        print("11. Update all Employee's Details")
        print("12. Update a Specific Employee's Details")
        print("13. View a specific Employee's Details")
        print("14. Generate Report for a Specific Employee")
        print("15. Salary Slip for a Specific Employee")
        print("16. Generate Tax Slip for a Specific Employee")
        print("17. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == '1':
                eid = input("ID: ")
                f_name = input("First Name: ")
                l_name = input("Last Name: ")
                dob = datetime.date.fromisoformat(input("DOB (YYYY-MM-DD): "))
                gender = input("Gender: ")
                email = input("Email: ")
                phone = input("Phone: ")
                address = input("Address: ")
                position = input("Position: ")
                join_date = datetime.date.fromisoformat(input("Joining Date (YYYY-MM-DD): "))

                emp = Employees(eid, f_name, l_name, dob, gender, email, phone, address, position, join_date)
                employee_service.add_employee(emp)
                print("Employee added successfully.")

            elif choice == '2':
                employees = employee_service.get_all_employees()
                if employees:
                    print(tabulate(employees, headers=["EmployeeID", "First Name", "Last Name", "DOB", "Gender", "Email", "Phone", "Address", "Position", "Join Date", "Termination Date"], tablefmt="grid"))
                else:
                    print("No employees found.")

            elif choice == '3':
                eid = input("Enter Employee ID: ")
                try:
                    emp = employee_service.get_employee_by_id(eid)
                    print(tabulate([emp], headers=["EmployeeID", "First Name", "Last Name", "DOB", "Gender", "Email", "Phone", "Address", "Position", "Join Date", "Termination Date"], tablefmt="grid"))
                except EmployeeNotFoundException as e:
                    print("Error:", e)

            elif choice == '4':
                eid = input("Enter Employee ID to remove: ")
                try:
                    employee_service.remove_employee(eid)
                    print("Employee removed.")
                except EmployeeNotFoundException as e:
                    print("Error:", e)

            elif choice == '5':
                pid = input("Payroll ID: ")
                eid = input("Employee ID: ")
                start_date = datetime.date.fromisoformat(input("Start Date (YYYY-MM-DD): "))
                end_date = datetime.date.fromisoformat(input("End Date (YYYY-MM-DD): "))
                basic = float(input("Basic Salary: "))
                overtime = float(input("Overtime Pay: "))
                deductions = float(input("Deductions: "))
                net = basic + overtime - deductions

                try:
                    if not eid.strip():
                        raise PayrollGenerationException("Employee ID cannot be empty.")
                    if basic < 0 or overtime < 0 or deductions < 0:
                        raise PayrollGenerationException("Salary values cannot be negative.")
                    if start_date > end_date:
                        raise PayrollGenerationException("Start date must be before end date.")

                    payroll_obj = payroll(pid, eid, start_date, end_date, basic, overtime, deductions, net)
                    payroll_service.generate_payroll(payroll_obj)
                    print("Payroll generated.")
                except PayrollGenerationException as e:
                    print("Error:", e)
                except Exception as e:
                    print("Unexpected error:", e)

            elif choice == '6':
                eid = input("Enter Employee ID: ")
                payrolls = payroll_service.get_payrolls_for_employee(eid)
                if payrolls:
                    print(tabulate(payrolls, headers=["Payroll ID", "Employee ID", "Start Date", "End Date", "Basic Salary", "Overtime Pay", "Deductions", "Net Salary"], tablefmt="grid"))
                else:
                    print("No payrolls found for this employee.")

            elif choice == '7':
                tid = input("Tax ID: ")
                eid = input("Employee ID: ")
                year = int(input("Tax Year: "))
                income = float(input("Taxable Income: "))
                amount = float(input("Tax Amount: "))

                try:
                    taxes = tax(tid, eid, year, income, amount)
                    tax_service.calculate_tax(taxes)
                    print("Tax record saved.")
                except Exception as e:
                    raise TaxCalculationException(str(e))

            elif choice == '8':
                rid = input("Record ID: ")
                eid = input("Employee ID: ")
                try:
                    record_date = datetime.date.fromisoformat(input("Record Date (YYYY-MM-DD): "))
                except ValueError:
                    print("Invalid date format.")
                    continue

                desc = input("Description: ")
                try:
                    amount = float(input("Amount: "))
                except ValueError:
                    print("Amount must be a number.")
                    continue

                rtype = input("Record Type (Income/Expense): ")

                try:
                    record = FinancialRecord(rid, eid, record_date, desc, amount, rtype)
                    financial_record_service.add_financial_record(record)
                    print(f"Financial record for {record_date.strftime('%Y-%m-%d')} added.")
                except FinancialRecordException as e:
                    print("Error:", e)
                except Exception as e:
                    print("Unexpected error:", e)

            elif choice == '9':
                try:
                    employees = employee_service.get_all_employees()
                    for emp in employees:
                        print("\n--- Report for", emp[1], emp[2], f"(ID: {emp[0]}) ---")

                        payrolls = payroll_service.get_payrolls_for_employee(emp[0])
                        if payrolls:
                            print("\nPayroll:")
                            print(tabulate(payrolls, headers=["Payroll ID", "Employee ID", "Start Date", "End Date", "Basic Salary", "Overtime", "Deductions", "Net Salary"], tablefmt="grid"))
                        else:
                            print("No payroll records.")

                        taxes = report_generator.generate_tax_report_by_employee(emp[0])
                        if taxes:
                            print("\nTaxes:")
                            print(tabulate(taxes, headers=["Employee ID", "First Name", "Last Name", "Tax Year", "Taxable Income", "Tax Amount"], tablefmt="grid"))
                        else:
                            print("No tax records.")

                        records = report_generator.generate_financial_record_by_employee(emp[0])
                        if records:
                            print("\nFinancial Records:")
                            print(tabulate(records, headers=["Employee ID", "First Name", "Last Name", "Record Date", "Description", "Amount", "Record Type"], tablefmt="grid"))
                        else:
                            print("No financial records.")

                except Exception as e:
                    print("Error generating report:", e)

            elif choice == '10':
                eid = input("Enter Employee ID to calculate tax: ")
                try:
                    payrolls = payroll_service.get_payrolls_for_employee(eid)
                    if not payrolls:
                        raise TaxCalculationException("No payrolls found for this employee.")

                    total_income = sum([row[4] + row[5] - row[6] for row in payrolls])
                    tax_amount = total_income * Decimal('0.20')
                    print("\nTax Summary:")
                    print(tabulate([[eid, total_income, round(tax_amount, 2)]], headers=["Employee ID", "Total Income", "Tax (20%)"], tablefmt="grid"))
                except TaxCalculationException as e:
                    print("Error:", e)
                except Exception as e:
                    print("Unexpected error:", e)

            elif choice == '11':
                eid = input("Enter Employee ID to update: ")
                try:
                    employee_service.get_employee_by_id(eid)
                    f_name = input("New First Name: ")
                    l_name = input("New Last Name: ")
                    dob = datetime.date.fromisoformat(input("New DOB (YYYY-MM-DD): "))
                    gender = input("New Gender: ")
                    email = input("New Email: ")
                    phone = input("New Phone: ")
                    address = input("New Address: ")
                    position = input("New Position: ")
                    join_date = datetime.date.fromisoformat(input("New Joining Date (YYYY-MM-DD): "))

                    updated_emp = Employees(eid, f_name, l_name, dob, gender, email, phone, address, position, join_date)
                    employee_service.update_employee(updated_emp)
                    print("Employee record updated successfully.")

                except EmployeeNotFoundException as e:
                    print("Error:", e)
                except Exception as e:
                    print("Unexpected error while updating employee:", e)

            elif choice == '12':
                eid = input("Enter Employee ID to update: ")
                try:
                    emp = employee_service.get_employee_by_id(eid)
                    print(tabulate([emp],
                                   headers=["EmployeeID", "First Name", "Last Name", "DOB", "Gender", "Email", "Phone",
                                            "Address", "Position", "Join Date", "Termination Date"], tablefmt="grid"))

                    print("Which attribute would you like to update?")
                    print("1. First Name")
                    print("2. Last Name")
                    print("3. Email")
                    print("4. Phone")
                    print("5. Address")
                    print("6. Position")
                    print("7. Gender")

                    attr_choice = input("Enter attribute number: ")
                    value = input("Enter new value: ")

                    updated = list(emp)
                    if attr_choice == '1':
                        updated[1] = value
                    elif attr_choice == '2':
                        updated[2] = value
                    elif attr_choice == '3':
                        updated[5] = value
                    elif attr_choice == '4':
                        updated[6] = value
                    elif attr_choice == '5':
                        updated[7] = value
                    elif attr_choice == '6':
                        updated[8] = value
                    elif attr_choice == '7':
                        updated[4] = value
                    else:
                        print("Invalid attribute selection.")
                        continue

                    updated_emp = Employees(
                        str(updated[0]),
                        str(updated[1]),
                        str(updated[2]),
                        datetime.date.fromisoformat(str(updated[3])) if isinstance(updated[3], str) else updated[3],
                        str(updated[4]),
                        str(updated[5]),
                        str(updated[6]),
                        str(updated[7]),
                        str(updated[8]),
                        datetime.date.fromisoformat(str(updated[9])) if isinstance(updated[9], str) else updated[9]
                    )
                    employee_service.update_employee(updated_emp)
                    print("Attribute updated successfully.")
                except EmployeeNotFoundException as e:
                    print("Error:", e)
                except Exception as e:
                    print("Unexpected error while updating attribute:", e)

            elif choice == '13':
                eid = input("Enter Employee ID: ")
                try:
                    emp = employee_service.get_employee_by_id(eid)
                    print("\nEmployee Details:")
                    print(tabulate([emp], headers=[
                        "EmployeeID", "First Name", "Last Name", "DOB", "Gender",
                        "Email", "Phone", "Address", "Position", "Join Date", "Termination Date"
                    ], tablefmt="grid"))
                except EmployeeNotFoundException as e:
                    print("Error:", e)
                except Exception as e:
                    print("Unexpected error:", e)

            elif choice == '14':
                eid = input("Enter Employee ID to generate full report: ")
                try:
                    emp = employee_service.get_employee_by_id(eid)
                    print("\n--- Employee Details ---")
                    print(tabulate([emp], headers=[
                        "EmployeeID", "First Name", "Last Name", "DOB", "Gender",
                        "Email", "Phone", "Address", "Position", "Join Date", "Termination Date"
                    ], tablefmt="grid"))

                    payrolls = payroll_service.get_payrolls_for_employee(eid)
                    print("\n--- Payroll Records ---")
                    if payrolls:
                        print(tabulate(payrolls, headers=[
                            "Payroll ID", "Employee ID", "Start Date", "End Date",
                            "Basic Salary", "Overtime", "Deductions", "Net Salary"
                        ], tablefmt="grid"))
                    else:
                        print("No payroll records found.")

                    records = report_generator.generate_financial_record_by_employee(eid)
                    print("\n--- Financial Records ---")
                    if records:
                        print(tabulate(records, headers=[
                            "Employee ID", "First Name", "Last Name",
                            "Record Date", "Description", "Amount", "Record Type"
                        ], tablefmt="grid"))
                    else:
                        print("No financial records found.")

                except EmployeeNotFoundException as e:
                    print("Error:", e)
                except Exception as e:
                    print("Error generating report:", e)

            elif choice == '15':
                eid = input("Enter Employee ID to generate salary slip: ")
                pid = input("Enter Payroll ID: ")
                try:
                    payroll_data = payroll_service.get_payroll_id(pid)
                    if not payroll_data:
                        print("No payroll found with that ID.")
                    elif str(payroll_data[1]) != str(eid):
                        print("Payroll ID does not belong to the given Employee ID.")
                    else:
                        print("\n--- Salary Slip ---")
                        headers = ["Field", "Value"]
                        slip = [
                            ["Payroll ID", payroll_data[0]],
                            ["Employee ID", payroll_data[1]],
                            ["Pay Period", str(payroll_data[2]) + " to " + str(payroll_data[3])],
                            ["Basic Salary", "₹" + str(payroll_data[4])],
                            ["Overtime Pay", "₹" + str(payroll_data[5])],
                            ["Deductions", "₹" + str(payroll_data[6])],
                            ["Net Salary", "₹" + str(payroll_data[7])]
                        ]
                        print(tabulate(slip, headers=headers, tablefmt="grid"))
                except Exception as e:
                    print("Error generating slip:", e)

            elif choice == '16':
                eid = input("Enter Employee ID to generate tax slip: ")
                tid = input("Enter Tax ID: ")
                try:
                    taxes = tax_service.get_tax_by_id(tid)
                    if not taxes:
                        print("No tax record found with that ID.")
                    elif str(taxes[1]) != str(eid):
                        print("Tax ID does not belong to the given Employee ID.")
                    else:
                        income = float(taxes[3])
                        tax_amount = float(taxes[4])
                        tax_rate = (tax_amount / income) * 100 if income != 0 else 0.0

                        print("\n--- Tax Slip ---")
                        headers = ["Field", "Value"]
                        slip = [
                            ["Tax ID", taxes[0]],
                            ["Employee ID", taxes[1]],
                            ["Tax Year", taxes[2]],
                            ["Taxable Income", "₹" + str(income)],
                            ["Tax Rate", str(round(tax_rate, 2)) + "%"],
                            ["Tax Calculation", "₹" + str(income) + " × " + str(round(tax_rate, 2)) + "%"],
                            ["Tax Amount", "₹" + str(tax_amount)]
                        ]
                        print(tabulate(slip, headers=headers, tablefmt="grid"))
                except Exception as e:
                    print("Error generating tax slip:", e)






            elif choice == '17':
                print("Exiting PayXpert. Goodbye!")
                break

            else:
                print("Invalid input. Try again.")

        except (ValueError, InvalidInputException) as ve:
            print("Invalid input:", ve)
        except (EmployeeNotFoundException, PayrollGenerationException, TaxCalculationException, FinancialRecordException, DatabaseConnectionException) as e:
            print("Error:", e)
        except Exception as e:
            print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()
