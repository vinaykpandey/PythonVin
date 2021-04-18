from workers.math_cal import welcome, add, multiply

if __name__ == "__main__":
    welcome.apply_async()
    add_task_id = add.delay(4, 4)
    # it will return task id not result
    print("Add result task id: ", add_task_id)
    task_id_m = multiply.delay(5, 7)
    print("Multiplication result is: ", task_id_m)
