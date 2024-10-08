import streamlit as st
import pandas as pd

# Datos de electronegatividades en formato tabla periódica
tabla_periodica = [
    ["H", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, "He"],
    ["Li", "Be", None, None, None, None, None, None, None, None, None, None, "B", "C", "N", "O", "F", "Ne"],
    ["Na", "Mg", None, None, None, None, None, None, None, None, None, None, "Al", "Si", "P", "S", "Cl", "Ar"],
    ["K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr"],
    ["Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe"],
    ["Cs", "Ba", "La", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn"],
    ["Fr", "Ra", "Ac", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", None, None, None, None, None, None, None, None, None]
]

# Diccionario de electronegatividades
electronegatividades = {
    "H": 2.20, "He": 0.00, "Li": 0.98, "Be": 1.57, "B": 2.04, "C": 2.55, "N": 3.04, "O": 3.44, "F": 3.98, "Ne": 0.00,
    "Na": 0.93, "Mg": 1.31, "Al": 1.61, "Si": 1.90, "P": 2.19, "S": 2.58, "Cl": 3.16, "Ar": 0.00, "K": 0.82, "Ca": 1.00,
    "Sc": 1.36, "Ti": 1.54, "V": 1.63, "Cr": 1.66, "Mn": 1.55, "Fe": 1.83, "Co": 1.88, "Ni": 1.91, "Cu": 1.90, "Zn": 1.65,
    "Ga": 1.81, "Ge": 2.01, "As": 2.18, "Se": 2.55, "Br": 2.96, "Kr": 3.00, "Rb": 0.82, "Sr": 0.95, "Y": 1.22, "Zr": 1.33,
    "Nb": 1.60, "Mo": 2.16, "Tc": 1.90, "Ru": 2.20, "Rh": 2.28, "Pd": 2.20, "Ag": 1.93, "Cd": 1.69, "In": 1.78, "Sn": 1.96,
    "Sb": 2.05, "Te": 2.10, "I": 2.66, "Xe": 2.60, "Cs": 0.79, "Ba": 0.89, "La": 1.10, "Ce": 1.12, "Pr": 1.13, "Nd": 1.14,
    "Pm": 1.13, "Sm": 1.17, "Eu": 1.00, "Gd": 1.20, "Tb": 1.10, "Dy": 1.22, "Ho": 1.23, "Er": 1.24, "Tm": 1.25, "Yb": 1.10,
    "Lu": 1.27, "Hf": 1.30, "Ta": 1.50, "W": 2.36, "Re": 1.90, "Os": 2.20, "Ir": 2.20, "Pt": 2.28, "Au": 2.54, "Hg": 2.00,
    "Tl": 1.62, "Pb": 2.33, "Bi": 2.02, "Po": 2.00, "At": 2.20, "Rn": 2.20, "Fr": 0.70, "Ra": 0.90
}

# Función para generar la tabla periódica con electronegatividades
def generar_tabla_periodica():
    tabla_html = "<table style='border-collapse: collapse; width: 100%;'>"
    for fila in tabla_periodica:
        tabla_html += "<tr>"
        for elemento in fila:
            if elemento is None:
                tabla_html += "<td style='border: 1px solid black; padding: 10px;'></td>"
            else:
                valor = electronegatividades.get(elemento, "N/A")
                tabla_html += f"<td style='border: 1px solid black; padding: 10px; text-align: center;'>{elemento}<br><small>{valor}</small></td>"
        tabla_html += "</tr>"
    tabla_html += "</table>"
    return tabla_html

# Función para calcular el tipo de enlace
def tipo_enlace(diferencia):
    if diferencia > 1.7:
        return "Iónico"
    elif 0.4 < diferencia <= 1.7:
        return "Covalente polar"
    else:
        return "Covalente apolar"

# Crear la app
st.title("Calculadora de Electronegatividad")

st.write("### Tabla periódica con electronegatividades")
st.markdown(generar_tabla_periodica(), unsafe_allow_html=True)

# Selección de los elementos
elemento1 = st.selectbox("Selecciona el primer elemento", list(electronegatividades.keys()))
elemento2 = st.selectbox("Selecciona el segundo elemento", list(electronegatividades.keys()))

# Calcular la diferencia de electronegatividad
if elemento1 and elemento2:
    electroneg1 = electronegatividades[elemento1]
    electroneg2 = electronegatividades[elemento2]
    diferencia = abs(electroneg1 - electroneg2)

    st.write(f"Electronegatividad de {elemento1}: {electroneg1}")
    st.write(f"Electronegatividad de {elemento2}: {electroneg2}")
    st.write(f"**Diferencia de electronegatividad:** {diferencia}")

    # Determinar el tipo de enlace
    enlace = tipo_enlace(diferencia)
    st.write(f"**Tipo de enlace:** {enlace}")
