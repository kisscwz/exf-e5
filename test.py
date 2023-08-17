import time

# 设置循环次数
total_iterations = 10
# 设置循环间隔时间（秒）
interval = 1

# 循环计次
for i in range(total_iterations):
    # 执行你想要循环执行的代码
    print("Iteration:", i+1)

    # 等待一段时间
    time.sleep(interval)
