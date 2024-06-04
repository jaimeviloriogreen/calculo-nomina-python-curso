from prettytable import PrettyTable
from os import system
from helpers import question_menu, insert_employee, set_employee_discount


system("clear" or "cls")

print(
"""
========== GESTIÓN DE NÓMINA ==========
"""
)

employees_db = []
table = PrettyTable()

table.field_names = ["Nombre", "Apellido", "Sueldo", "SFS", "AFP", "Salario Neto Imponible", "ISR", "Salario Neto"]


while True:
    
    opts = question_menu()
    
    if opts == "1":
        system("clear" or "cls")
        employees = insert_employee()
        system("clear" or "cls")
        
        print("\n¡Empleado agregado!\n")
        
        employees_db.append(employees)
         
    if opts == "2":
        system("clear" or "cls")
     
        employees = [*map(set_employee_discount, employees_db)]

        table.add_rows(employees)
        print(table, "\n")
        
        table.clear_rows()
    elif opts == "3":
        system("clear" or "cls")
        print("\n¡Fin del programa!\n")
        break
        
    
    
    
    




