def probar_streamlit(st):
    """ Ponga aqui todos los controles de prueba para que entienda como funciona"""
    st.write("Seleccione su fecha de nacimiento ")
    st.button("Soy un boton")
    st.date_input("Fecha")
    st.write("Defina la alarma que le recuerde el horario de clase")
    st.time_input("Hora")

    st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

    with st.expander("See explanation"):
        st.write("""
             The chart above shows some numbers I picked for you.
             I rolled actual dice for these, so they're *guaranteed* to
             be random.
         """)