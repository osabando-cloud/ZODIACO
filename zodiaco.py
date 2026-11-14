from datetime import datetime
import sys

SIGNOS = {
    "Capricornio": ((12, 22), (1, 19)),
    "Acuario": ((1, 20), (2, 18)),
    "Piscis": ((2, 19), (3, 20)),
    "Aries": ((3, 21), (4, 19)),
    "Tauro": ((4, 20), (5, 20)),
    "Géminis": ((5, 21), (6, 20)),
    "Cáncer": ((6, 21), (7, 22)),
    "Leo": ((7, 23), (8, 22)),
    "Virgo": ((8, 23), (9, 22)),
    "Libra": ((9, 23), (10, 22)),
    "Escorpio": ((10, 23), (11, 21)),
    "Sagitario": ((11, 22), (12, 21)),
}

MENSAJES = {
    "Capricornio": "Eres disciplinado, responsable y muy enfocado en tus metas.",
    "Acuario": "Eres original, independiente y siempre piensas diferente.",
    "Piscis": "Eres sensible, creativo y muy intuitivo con las personas.",
    "Aries": "Eres valiente, enérgico y siempre vas adelante con pasión.",
    "Tauro": "Eres estable, perseverante y muy sensible a la belleza.",
    "Géminis": "Eres curioso, sociable y siempre lleno de ideas nuevas.",
    "Cáncer": "Eres emocional, protector y muy ligado a tu hogar.",
    "Leo": "Eres carismático, fuerte y naturalmente líder.",
    "Virgo": "Eres práctico, observador y muy detallista.",
    "Libra": "Eres equilibrado, amable y buscas siempre la armonía.",
    "Escorpio": "Eres intenso, profundo y muy apasionado en todo.",
    "Sagitario": "Eres optimista, aventurero y con una gran libertad interior.",
}


def parse_date(value: str):
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y"):
        try:
            return datetime.strptime(value.strip(), fmt).date()
        except ValueError:
            pass
    raise ValueError("La fecha debe tener el formato YYYY-MM-DD, DD/MM/YYYY o DD-MM-YYYY.")


def obtener_signo(fecha):
    mes = fecha.month
    dia = fecha.day

    if (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        return "Capricornio"
    if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Acuario"
    if (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return "Piscis"
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Aries"
    if (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Tauro"
    if (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Géminis"
    if (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Cáncer"
    if (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leo"
    if (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgo"
    if (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    if (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpio"
    if (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitario"

    raise ValueError("No se pudo determinar el signo zodiacal.")


def main():
    if len(sys.argv) > 1:
        fecha_input = sys.argv[1]
    else:
        fecha_input = input("Ingresa tu fecha de nacimiento (YYYY-MM-DD): ")

    try:
        fecha = parse_date(fecha_input)
        signo = obtener_signo(fecha)
        print(f"Tu signo zodiacal es: {signo}")
        print(f"Mensaje: {MENSAJES[signo]}")
    except ValueError as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
