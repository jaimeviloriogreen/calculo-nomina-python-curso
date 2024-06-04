
tabla_isr = [
    {"id":1, "lim_inf": 0.00, "lim_sup":416220.00, "agr": 0, "tasa": 0},
    {"id":2, "lim_inf": 416220.01, "lim_sup":624329.00, "agr": 0, "tasa": 0.15},
    {"id":3, "lim_inf": 624329.01, "lim_sup":867123.00, "agr": 31216.00, "tasa": 0.20},
    {"id":4, "lim_inf": 867123.01, "lim_sup": 999999999.00, "agr": 79776, "tasa": 0.25}, 
]

tss = {
    "sfs":0.0304,
    "afp":0.0287
}

def set_employee_discount(emp: dict) -> list:
    fname = emp["fname"]
    lname = emp["lname"]
    salary = float(emp["salary"])
    sfs = tss["sfs"] * salary
    afp = tss["afp"] * salary

    salario_neto_imponible = salary - (sfs + afp)
   
    ISR = set_isr(salario_neto_imponible)

    salario_neto = salary - (sfs + afp) - ISR

    return [
        fname, 
        lname, 
        f"RD${salary:,.2f}",
        f"RD${sfs:,.2f}",
        f"RD${afp:,.2f}",
        f"RD${salario_neto_imponible:,.2f}",
        f"RD${ISR:,.2f}",
        f"RD${salario_neto:,.2f}"
    ]

def set_isr(sni:float)-> float:
    resultado = 0
    for isr in tabla_isr:
        sueldo_anual = sni * 12
    
        if sueldo_anual >= isr["lim_inf"] and sueldo_anual <= isr["lim_sup"]:
            excedente = sueldo_anual - isr["lim_inf"]
            resultado = ((excedente * isr["tasa"]) + isr["agr"]) / 12
            
                
                
    return resultado

