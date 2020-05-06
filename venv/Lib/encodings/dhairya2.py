# # def per(name,*dtat):
# #     print(name)
# #     print(dtat)
# #
# # per('navin',28,'mumbai',222222)
# #
# # lst = [20,34,56,23,66,44,22]
# # even = []
# # odd = []
# # for i in lst:
# #     if i % 2 == 0 :
# #         even.append(i)
# #     else:
# #         odd.append(i)
# # print(even)
# # print(odd)
#
#
# def fib(n):
#     a = 0
#     b=1
#     print(a)
#     print(b)
#
#     for i in range(1,n):
#         c = a + b
#         a = b
#         b = c
#         print(c)
#
# fib(10)
#
#
# # fib(10)
#
#

# def fac(n):
#     d = 1
#     for f in range(1,n+1):
#         d = d * f
#         print(d)
# fac(5)
#
f = lambda a,b : a*b

print(f(5,6))
