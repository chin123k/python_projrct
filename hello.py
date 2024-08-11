import streamlit as st

def username_checker(username):
    return username.lower() == "validuser"

def show_entries(selected_option):
    st.write(f"Selected Item: {selected_option}")
    if selected_option == 'Chemistry Cycle':
        GPA()

def GPA():
    weighted_sum = 0

    chem = get_chem()
    st.divider()
    python = get_python()
    st.divider()
    maths = get_maths()
    st.divider()
    epd = get_epd()
    st.divider()
    mechanics = get_mechanics()
    st.divider()

    total_credits = chem[1]+python[1]+maths[1]+epd[1]+mechanics[1]
    weighted_sum = chem[0]+python[0]+maths[0]+epd[0]+mechanics[0]
    sgpa = weighted_sum / total_credits
    if st.button("Submit"):
        st.info(f"Your GPA is {sgpa}")

def get_chem():
    st.header("Engineering Chemistry")
    st.divider()
    credits = st.number_input("Enter the credits in Chemistry course (8th digit of course code):", min_value=1, max_value=5)
    marksi1 = st.number_input("Marks obtained in Chemistry ISA1:", value=0, step=1, format="%d")
    marksi2 = st.number_input("Marks obtained in Chemistry ISA2:", value=0, step=1, format="%d")
    markse = st.number_input("Marks obtained in Chemistry ESA:", value=0, step=1, format="%d")
    misc = st.number_input("Marks obtained in Chemistry lab/assignment:", value=0, step=1, format="%d")
    total = (markse/2) + (marksi1/2) +(marksi2/2) + misc
    gp = grade_point(total)
    sums = gp*credits
    return sums, credits

def get_python():
    st.header("Python for Computational Problem Solving")
    st.divider()
    credits = st.number_input("Enter the credits in Python course (8th digit of course code):", min_value=1, max_value=5)
    marksi1 = st.number_input("Marks obtained in Python ISA1:", value=0, step=1, format="%d")
    marksi2 = st.number_input("Marks obtained in Python ISA2:", value=0, step=1, format="%d")
    markse = st.number_input("Marks obtained in Python ESA:", value=0, step=1, format="%d")
    misc = st.number_input("Marks obtained in Python project/assignment:", value=0, step=1, format="%d")
    total = (markse/2) + (marksi1/2) + (marksi2/2) + misc
    gp = grade_point(total)
    sums = gp*credits
    return sums, credits

def get_maths():
    st.header("Engineering Mathematics")
    st.divider()
    credits = st.number_input("Enter the credits in Maths course (8th digit of course code):", min_value=1, max_value=5)
    marksi1 = st.number_input("Marks obatained in Maths ISA1:", value=0, step=1, format="%d")
    marksi2 = st.number_input("Marks obtained in Maths ISA2:", value=0, step=1, format="%d")
    markse = st.number_input("Marks obtained in Maths ESA:", value=0, step=1, format="%d")
    misc = st.number_input("Marks obtained in Maths assignment:", value=0, step=1, format="%d")
    total = (markse/2) + (marksi1/2) + (marksi2/2) + misc
    gp = grade_point(total)
    sums = gp*credits
    return sums, credits

def get_epd():
    st.header("Electronic Principles and Devices")
    st.divider()
    credits = st.number_input("Enter the credits in EPD course (8th digit of course code):", min_value=1, max_value=5)
    marksi1 = st.number_input("Marks obatained in EPD ISA1:", value=0, step=1, format="%d")
    marksi2 = st.number_input("Marks obtained in EPD ISA2:", value=0, step=1, format="%d")
    markse = st.number_input("Marks obtained in EPD ESA:", value=0, step=1, format="%d")
    misc = st.number_input("Marks obtained in EPD assignment:", value=0, step=1, format="%d")
    total = (markse/2) + (marksi1/2) + (marksi2/2) + misc
    gp = grade_point(total)
    sums = gp*credits
    return sums, credits

def get_mechanics():
    st.header("Engineering Mechanics")
    st.divider()
    credits = st.number_input("Enter the credits in Mechanics course (8th digit of course code):", min_value=1, max_value=5)
    marksi1 = st.number_input("Marks obatained in Mechanics ISA1:", value=0, step=1, format="%d")
    marksi2 = st.number_input("Marks obtained in Mechanics ISA2:", value=0, step=1, format="%d")
    markse = st.number_input("Marks obtained in Mechanics ESA:", value=0, step=1, format="%d")
    misc = st.number_input("Marks obtained in Mechanics assignment:", value=0, step=1, format="%d")
    total = (markse/2) + (marksi1/2) + (marksi2/2) + misc
    gp = grade_point(total)
    sums = gp*credits
    return sums, credits

def grade_point(marks):
    if 90 <= marks <= 100:
        grade_point = 10
    elif 80 <= marks < 90:
        grade_point = 9        
    elif 70 <= marks < 80:
        grade_point = 8
    elif 60 <= marks < 70:
        grade_point = 7
    elif 50 <= marks < 60:
        grade_point = 6
    elif 40 <= marks < 50:
        grade_point = 5
    else:
        grade_point = 0
    return grade_point

st.title("PESU GPA Calculator")
st.title("Dropdown Example")
username = st.text_input("Enter your username:")
if username:
    if username_checker(username):
        st.success("Username is valid. You can proceed.")
        selected_option = st.selectbox("Select an option", ['Physics Cycle', 'Chemistry Cycle'], index=None)
        if selected_option != '':
            show_entries(selected_option)
    else:
        st.error("Invalid username. Access denied.")
