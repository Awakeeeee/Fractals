import matplotlib.pyplot as mp
import math

#基于matplotlib编写自己的turtle-like画笔
class Fracpen:

	def __init__(self, P):
		self.x = P[0]
		self.y = P[1]
		self.h = P[2] #h for heading
		self.c = 'red'

	def CurrentPoint(self):
		return (self.x, self.y, self.h)

	def ResetTo(self, P):
		self.x = P[0]
		self.y = P[1]
		self.h = P[2]

	#以当前状态为起点,绘制一条长为L的线段,状态前进到线段终点
	def Forward(self, L):
		endx = self.x + L * math.cos(self.h * math.pi / 180)
		endy = self.y + L * math.sin(self.h * math.pi / 180)
		A = [self.x, endx]
		B = [self.y, endy]
		mp.plot(A, B, c = self.c, alpha = 1)
		self.x = endx
		self.y = endy

	#向前移动,但只改变画笔状态,不绘制
	def ForwardVoid(self, L):
		endx = self.x + L * math.cos(self.h * math.pi / 180)
		endy = self.y + L * math.sin(self.h * math.pi / 180)
		self.x = endx
		self.y = endy

	def Left(self, angle):
		self.h = self.h + angle

	def Right(self, angle):
		self.h = self.h - angle

	def SetColor(self, col):
		self.c = col