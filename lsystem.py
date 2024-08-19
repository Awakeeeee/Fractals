import matplotlib.pyplot as mp
from fracpen import Fracpen

SET = {
	'F' : 'move forward and draw',
	'f' : 'move forward without drawing',
	'+' : 'turn left',
	'-' : 'turn right',
	'[' : 'save state to stack',
	']' : 'read state from stack',
}

#LS: 文法系统
#A: 起点
#L: 步长
#n: 迭代次数
def LSystem(LS, A, L, n):
	angle = LS['angle']
	axiom = LS['axiom']
	rule = LS['rules']

	#构造文法字符串
	loop = 0
	s = axiom
	while loop < n:
		
		replaced = [] #原始s中每个字符的匹配结果分别作为一个元素存入这个列表
		
		for char in s:
			match = 0
			for entry in rule:
				check, mod = entry.split('->')
				if char == check:
					if mod:
						replaced.append(mod)
						match = 1
						#TODO char已经找到了匹配,为什么不能在这里break
			if match == 0: #如何没有匹配,意思就是照抄这个字符
				replaced.append(char)

		s = ''.join(replaced)
		print("{} : {}".format(loop, s))
		loop = loop + 1

	
	#绘制图形
	fp = Fracpen(A)
	memory = [] #用于分支结构的回溯
	for char in s:
		if char not in SET: #没有对应绘制含义的字符
			continue

		if char == 'F':
			fp.Forward(L)
		elif char == 'f':
			fp.ForwardVoid(L)
		elif char == '+':
			fp.Left(angle)
		elif char == '-':
			fp.Right(angle)
		elif char == '[':
			p = fp.CurrentPoint()
			memory.append(p)
		elif char == ']':
			q = memory[-1]
			del memory[-1]
			fp.ResetTo(q)


# 具体图形的设定集
koch = {
	'angle' : 60,
	'axiom' : 'F',
	'rules' : ['F->F+F--F+F']
}

tree1 = {
	'angle' : 22.5,
	'axiom' : 'X',
	'rules' : ['X->F-[[X]+X]+F[+FX]-X']
}


if __name__ == '__main__':
	
	print("starting l-system")

	mp.rcParams['figure.facecolor'] = 'green'

	A = (0, 0, 90)
	L = 20
	n = 5

	LSystem(tree1, A, L, n)

	mp.axis('equal')
	#mp.axis('off')
	mp.show()

