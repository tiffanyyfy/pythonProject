import asyncio


# 定义异步函数
async def fetch_data(api_name, delay):
    print(f"Fetching data from {api_name}...")
    await asyncio.sleep(delay)  # 模拟不同的延迟
    print(f"Data fetched from {api_name}!")
    return f"{api_name} data"


# 定义主异步函数，使用 asyncio.gather 并发运行
async def main():
    # 创建多个异步任务
    tasks = [
        fetch_data("API 1", 2),
        fetch_data("API 2", 3),
        fetch_data("API 3", 1)
    ]
    # 并发执行所有任务并等待它们完成
    results = await asyncio.gather(*tasks)

    # 输出结果
    for result in results:
        print(result)


# 运行主异步函数
asyncio.run(main())