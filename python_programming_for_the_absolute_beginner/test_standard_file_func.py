original_text = """Practical experience shows that consultation with
IT professionals require us to analyze key components
planned upgrade? Dear friends, consultation with
IT professionals can evaluate the value of new offers? So
Thus, the new organizational model directly depends on
positions taken by participants in relation to the tasks assigned?
"""
additional_text = """
On the other hand, the implementation of the 
planned development plan contributes to the preparation and implementation 
of impact forms? A diverse and rich experience, the innovative path chosen 
by us plays an important role in the formation of a personnel training system 
that meets urgent needs! Higher-order considerations, as well as 
socio-economic development, allow us to appreciate the importance of 
comprehensively balanced innovations. Dear friends, the constant information 
and technical support of our activities entails the process of introducing 
and modernizing the directions of progressive development.
"""

def read_file(file_name):
    try:
        f = open(file_name, 'r')
        print(f.read())
    except FileNotFoundError:
        print('File not found!\n')
    else:
        f.close()

def change_file(file_name, text, mode = 'w'):
    try:
        f = open(file_name, mode)
        f.write(str(text))
    except FileNotFoundError:
        print('File not found!\n')
    finally:
        f.close()


change_file('test.txt', original_text)
print('Text before change:')
read_file('test.txt')

change_file('test.txt', additional_text, 'a')
print('Text after change:')
read_file('test.txt')