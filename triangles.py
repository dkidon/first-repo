from math import sqrt

print('This is a program that does the pythagorean theorem for you.')
print('Assume the sides are a, b, c, c being the hypotenuse.')
formula = input('Which side (a, b, c) do you wish to calculate? side> ')

if formula == 'c':
	side_a = int(input('Input the length of side a: '))
	side_b = int(input('Input the length of side b: '))

	side_c = sqrt(side_a * side_a + side_b * side_b)
	
	print('The length of side c is: ' )
	print(side_c)

elif formula == 'a':
    side_b = int(input('Input the length of side b: '))
    side_c = int(input('Input the length of side c: '))
    
    side_a = sqrt((side_c * side_c) - (side_b * side_b))
    
    print('The length of side a is' )
    print(side_a)

elif formula == 'b':
    side_a = int(input('Input the length of side a: '))
    side_b = int(input('Input the length of side c: '))
        
    side_c = sqrt(side_c * side_c - side_a * side_a)
    
    print('The length of side b is')
    print(side_c)

else:
	print('Please select a side- a, b, or c')
  
