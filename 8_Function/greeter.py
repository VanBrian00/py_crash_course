def greet_user(nama):
    """Display a simple greeting."""
    print(f"Hello, {nama.title()}!")
    
greet_user('Jovan')

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

#perulangan tak terbatas
flag = True
while flag:
    print("\nPlease tell me your name (enter 'q' if u want quit):")
    f_name = input('First name: ')
    if f_name == 'q':
        break

    m_name = ''
    ask_middle_name = input('Have a middle name? yes or no ')
    if ask_middle_name.lower() == 'yes' : 
        m_name = input('Middle name: ')
    if m_name == 'q':
        break

    l_name = input('Last name: ')
    if l_name == 'q':
        break

    if m_name:
        formatted_name = get_formatted_name(f_name, l_name, m_name)
    else:
        formatted_name = get_formatted_name(f_name, l_name)

    print(f'Hello, {formatted_name}!')