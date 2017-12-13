# def my_abs(x):
# 	if not isinstance(x,(int,float)):
# 		raise TypeError('bad operand type')
# 	if x >= 0 :
# 		return x
# 	else:
# 		return -x
import math

# def move(x,y,step,angle=0):
# 	nx = x + step * math.cos(angle)
# 	ny = y - step * math.sin(angle)
# 	return nx,ny

#返回一个二元一次方程的两个解
# def quadratic(a,b,c):
# 	x1 = (-b + math.sqrt(b*b - 4*a*c))/2*a
# 	x2 = (-b - math.sqrt(b*b - 4*a*c))/2*a
# 	return x1,x2
# import pdb
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
def quadratic(a,b,c):
	det = math.sqrt(pow(b,2)-4*a*c)
	# pdb.set_trace()
	if det > 0:
		return (-b + det) / (2*a) , (-b - det) / (2*a)
	elif det == 0:
		return (-b + det) / (2*a)
	else:
		return None
print('quadratic(2,3,1) = ',quadratic(2,3,1))
print('quadratic(1,3,-4) = ',quadratic(1,3,-4))
if quadratic(2,3,1) != (-0.5,-1.0):
    print("测试失败！")
elif quadratic(1,3,-4) != (1.0,-4.0):
	print("测试失败")
else:
	print("测试成功！")


