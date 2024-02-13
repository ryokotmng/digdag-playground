import digdag

class MyWorkflow(object):
    def my_task(self, arg: str) -> str:
        print('Running my_task')
        print(arg)
        digdag.env.store({'my_task': arg})

    def my_second_task(self) -> str:
        print('Running my_second_task')
        # print(my_task)
        # digdag.env.params['my_task']