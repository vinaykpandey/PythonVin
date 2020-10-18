import datetime
def file_write(text_str):
    """
    @file_write_task:
    @argument: str
    """
    # print("file_write_task called in tasks.py")
    f = open('celery.log','a+')
    mydate = datetime.datetime.now()
    datetime_str = datetime.datetime.strftime(mydate, '%Y-%m-%d %H:%M:%S')
    f.write(str(datetime_str))
    f.write(' ')
    f.write(text_str)
    f.write(str('\n'))
    f.close()
