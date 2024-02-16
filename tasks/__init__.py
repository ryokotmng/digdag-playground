import digdag

class MyWorkflow(object):
    def my_task(self, arg: str, nested: str):
        print('Running my_task')
        print(arg)
        print("nested: "+nested)
        digdag.env.store({'my_task': arg})

    def my_second_task(self, my_task):
        print('Running my_second_task')
        print(my_task)
        print(digdag.env.params['my_task'])
