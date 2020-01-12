'''
3+2*{1+2*[-4/(8-6)+7]}
25
'''
def eval_postfix(s):
	stack = []
	for i in s:
		if i.isnumeric():
			stack.append(i)
		else:
			# a = 0
			# b = 0
			# if stack[-1].isnumeric():
			# 	a = int(stack.pop())
			#
			#
			# if stack[-1].isnumeric():
			# 	b = int(stack.pop())

			a = int(stack.pop())
			b = int(stack.pop())
			# print(a,b)
			if i == '+':
				stack.append(a+b)
			if i == '-':
				stack.append(b-a)

			if i == '*':
				stack.append(a*b)
			if i == '/':
				stack.append(b/a)
			if i =='^':
				stack.append(b^a)
	if not stack:
		return -1
	return stack.pop()


def infix2postfix(s):
	stack = []
	ans = ''

	for i in s:

		if i.isnumeric() or i.isalpha():
			ans+=i
		if i in '({[':
			stack.append('(')
		if i in '+-*/^':
			d = {'+':1,'-':1,'*':2,'/':2,'^':3,'(':0}

			while stack and d[stack[-1]] >= d[i]:
				ans+=stack.pop()

			stack.append(i)

		if i in ')]}':

			while stack and stack[-1] != '(':

				ans += stack.pop()

			if stack and stack[-1] != '(':
					return -1
			stack.pop()

	while stack:
		ans+=stack.pop()
		# if stack[-1] == '(':
		# 	stack.pop()
		# else:
		# 	ans+=stack.pop()
	return ans

def func(s):
	for i in s:
		pass

def right(str):
	# str = input()
	str = str.replace("{", "(")
	str = str.replace("}", ")")
	str = str.replace("[", "(")
	str = str.replace("]", ")")
	print('right ans:%g' % (eval(str)))
'''
while True:
	try:

		str = input()
		str = str.replace("{", "(")
		str = str.replace("}", ")")
		str = str.replace("[", "(")
		str = str.replace("]", ")")
		print('%g'%(eval(str)))

	except:
		break
'''
s = '3+2*{0-1+2*[4/(8-6)+7]}'
# s = '3-2+4'
# s = '4+3*2'
# s = '3-(2+4)'
# s = "a+b*(c^d-e)^(f+g*h)-i"
# 'abcd^e-fgh*+^*+i-'
print(infix2postfix(s))
ans = infix2postfix(s)
print('my ans: ',eval_postfix(ans))
right(s)