import asyncio


class Async():

    async def task(self, taskName :str):
        print(f"enter into task,task-name:{taskName}")
        print(f"{taskName} end.")
        return f'我执行的task是：{taskName}'

    async def runningArsynMth(self):
        tasks = [self.task('task3'), self.task('task2'), self.task('task1')]
        results = await asyncio.gather(*tasks)
        for res in results:
            print(f"调度的服务有:{res}")




#其他项目引用时此处代码不会执行
if __name__ == "__main__":
    async_obj = Async()
    asyncio.run(async_obj.runningArsynMth())