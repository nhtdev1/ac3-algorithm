'''Nguyễn Hoàng Thịnh - 17110372'''
from csp import *

# Định nghĩa thuật toán AC3
def AC_3(csp):
	queueArcs = queue.Queue()
	for arc in csp.C:
		queueArcs.put(arc)


	while not queueArcs.empty():
		(Xi,Xj) = queueArcs.get()

		# Nếu domain của Xi có sự thay đổi
		if REVISE(csp,Xi,Xj):
			# Nếu thay đổi làm domain của Xi rỗng điều đó có nghĩa là
			# không có giá trị nào trong Xj mà thỏa mãn ràng buộc giữa Xi và Xj
			# ta trả về False, không tìm thấy Solution
			if len(csp.D[Xi]) == 0:
				return False

			# Với các phần tử ràng buộc với Xi mà khác Xj, ta tiếp tục thêm
			# vào hàng đợi để xét
			for Xk in csp.neighbors[Xi]:
				if Xk != Xj:
					queueArcs.put((Xk,Xi))
	return True

# Hàm xem xét sự ràng buộc giữa Xi và Xj
def REVISE(csp,Xi,Xj):
	revised = False
	Di = set(csp.D[Xi])

	for x in Di:
		if not inconsistent(csp,x,Xi,Xj): 
			csp.D[Xi] = csp.D[Xi].replace(x,'') # Xóa giá trị x trong X[i]
			revised = True
	return revised

def inconsistent(csp,x,Xi,Xj):
	Dj = csp.D[Xj]
	for y in Dj:
		# Xj in csp.neighbors[Xi]: nghĩa là Xj nằm trong mảng phần tử ràng buộc với Xi
		# Và nếu giá trị y trong Xj khác với x thì return True
		if Xj in csp.neighbors[Xi] and y != x:
			return True
	return False

def getResults(input):
	start = time.time()
	sudoku = CSP(input)
	solved = AC_3(sudoku)
	if solved == True:
		return printSolution(sudoku.D), time.time() - start

if __name__ == "__main__":

	# Đọc dữ liệu từ file txt
	# Sudoku được biểu diễn dưới file txt, trong đó tất cả các phần tử
	# được ghi trên 1 dòng từ trái qua phải, từ trên xuống dưới. Ô nào trống
	# ta sẽ điền vào số 0

	array = []
	with open('input1.txt','r') as ins:
		for line in ins:
			array.append(line)

	print("Input:")
	printArray(array[0])

	# Chạy thuật toán giải quyết đầu vào
	start = time.time()
	sudoku = CSP(array[0])
	solved = AC_3(sudoku)
	if solved == True:
		print("Output:")
		printSolution(sudoku.D)
		print("Time excute:",time.time() - start)



