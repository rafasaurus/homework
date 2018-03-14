import numpy as np
n = 4
arr = np.array([2, 1, 3, 4,
                3, 4, 1, 1,
                1, 2, 3, 4,
                1, 2, 4, 3])
arr_ = arr.copy()
expert_points = np.array([1, 0, 1, 1,
                          0, 1, 1, 1,
                          1, 1, 1, 0,
                          1, 0, 0, 1])
expert_point = expert_points.reshape((n, n))
arr = arr.reshape((n, n))   
r0 = np.sum(arr, axis=1)
print(arr)
print(r0)
min__ = np.argmin(r0)
print(min__)

r0_sum = np.sum(r0)
r0_sum_mean = np.mean(r0)
print(r0_sum_mean)
s = np.sum(pow(r0-r0_sum_mean, 2))

print(s)
w = (12 * s) / (n**2 * (n**3-n))
print(w)
if w >= 0 and w <= 0.1:
    print("they don't agree with each other")
elif w > 0.1 and w <= 0.3:
    print("շատ թույլ համաձայնություն")
elif w > 0.3 and w <= 0.5:
    print("թույլ")
elif w > 0.5 and w <= 0.7:
    print("չափավոր")
elif w > 0.7 and w <= 0.9:
    print("բարձր")
elif w > 0.9 and w <= 1:
    print("very nice")
print("-----------------------\n-----------------------\nանմիջական գնահատականների մեթոդ")
expert_points_column_sum = np.sum(expert_points, axis=0)
print(expert_points)
print(expert_points_column_sum)
expert_points = expert_points/expert_points_column_sum 
print(expert_points)
w = np.sum(arr_, axis=0)
print("w==", w)
print(arr_/w)
print(arr_/w)
arr_ = arr_.reshape((n, n))
print(w)
print(w.shape)
arr_ = arr_/w
print("arr_ = \n")
print(arr_)

W = np.sum(arr_, axis=0)/n
print("W=\n", W)
print("-----------------------\n-----------------------\nզույգ առ զույգ համեմատման մեթոդ")

