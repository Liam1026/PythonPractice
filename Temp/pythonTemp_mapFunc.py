# 迭代器
# https://mp.weixin.qq.com/s?__biz=MzU0OTg3NzU2NA==&mid=2247483827&idx=1&sn=6a661c78b3f0db2e4c94cee1ddc3b036&chksm=fba863e0ccdfeaf628a112bcfe9401b3933fe5b359e17ff4345d6fcfddf7103c4460cd3d1c5d&scene=21#wechat_redirect

# b = map(lambda x:x*x, [1, 2, 3])
# print(i for i in b)
# print(i for i in b)
def yield_test(n):
    for i in range(n):
        yield call(i)

def call(i):
    return i*2

x = yield_test(5)
print([i for i in x])
print([i for i in x])


