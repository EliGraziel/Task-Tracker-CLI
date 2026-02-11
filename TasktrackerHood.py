from datetime import datetime
import json
import shelve
import os

# Read the json
def read_json():
    with open(file='task.json', mode='r', encoding='utf-8') as j:
        after_read = json.load(j)
        return after_read
        
# Add a task to existing task list[Dictionary]   
def Updatelist(new_task):
    saved_tasks = read_json()
    saved_tasks.append(new_task)
    return saved_tasks

# Write the json 
def write_json(_task_):
    with open(file="task.json", mode='w', encoding= 'utf-8') as t:
        json.dump(_task_,t,indent=4)

# Assignment of task_ids, never repeat an id. 
def assign_id():
    with shelve.open('_id_') as db:
        _id = db.get('_id_',-1)
        _id += 1
        db['_id_'] = _id
        return _id 

    """ To restart the memory, just delete the file
    what happpens:
        starts from -2: Hence the generated id starts from 0.
    """
    
variable_id = assign_id()
    
# To access any task,  provide id then return the task dictionary
# Reasons to access the task ---> update description, delete task, task details such as done, not started plus in progress.
# Return the index of the task dictionary needed, given the task id.

# its a list of lists
def return_index(id_input):
    saved_tasks = read_json()
    for index,dict in enumerate(saved_tasks):
        id_found = next(iter(dict))
        if id_found == id_input:
            return index

# Global variables
time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Object for Task 
class Task:
    def __init__(self,task_placeholder,_id_= variable_id,status = 'Not started', 
         time_of_creation = time_now, time_of_update = None):
        self.task_id = _id_
        self.task_description = task_placeholder
        self.status = status
        self.createdAt = time_of_creation
        self.updatedAt = time_of_update
        
# Methods
    #Converts the object's attributes to a list
    def construct_task(self):
        return [
            {
                self.task_id:{
                    "task description":self.task_description,
                    "status":self.status,
                    "create time": self.createdAt,
                    "update time": self.updatedAt
                }
            }
        ]
    # Add a task to the list of task dictioanries.
    def Add_task(self):
        added_task = self.construct_task()      
        if not os.path.exists('task.json'):
            write_json(_task_=added_task)
        else:
            entire_list = Updatelist(new_task=added_task)
            write_json(_task_= entire_list)
        print(added_task)
        print(f"TASK SUCCESSFULLY SAVED AS ID:{self.task_id}")
        
    # Update task description of specific task in the list of task dictionaries.
def update_task_description(task_id,updated_description):
    saved_tasks = read_json()
    _ID_= next(iter(saved_tasks[return_index(id_input=task_id)]))
    nested_dictionary = saved_tasks[return_index(id_input=task_id)].get(_ID_)
    #short_description = nested_dictionary['task description']
    short_description = updated_description
    status_of_task = nested_dictionary['status']
    creatitontime_of_task = nested_dictionary['create time']
    # updatetime_of_task = nested_dictionary['update time']
    Updated_task = Task(_id_=_ID_,task_placeholder=short_description,status=status_of_task,
                        time_of_creation=creatitontime_of_task,time_of_update= time_now).construct_task()
    saved_tasks[return_index(id_input=task_id)] = Updated_task
    write_json(_task_=saved_tasks)
    print(Updated_task)

    
def delete_task(number):
    pass
    
def Update_status(task_status):
    pass
    
def list_done():
    pass
    
def list_in_progress():
    pass
    
def list_not_started():
    pass

