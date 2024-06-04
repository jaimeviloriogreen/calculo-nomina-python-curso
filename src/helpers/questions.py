import inquirer

def question_menu():
    questions = [
        inquirer.List(
            "menu",
            message="Elige la opción que prefieras...",
            choices=[
                ("1. Ingresar empleado", "1"),
                ("2. Mostrar nómina", "2"),
              
                ("3. Salir", "3")
            ],
            carousel=True
        )
    ]
    choice = inquirer.prompt(questions)
    return choice['menu']

def insert_employee():
    question = [
        inquirer.Text("fname", message="Ingresa el nombre del empleado"),
        inquirer.Text("lname", message="Ingresa el apellido del empleado"),
        inquirer.Text("salary", message="Indica el salario mensual del empleado")
    ]
    return inquirer.prompt(question)
