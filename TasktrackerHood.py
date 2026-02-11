from datetime import datetime
import json
import shelve
import os


# Global variables
time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Assign of task_ids to each task, never repeat an id. 
def assign_id():
    with shelve.open('_id_') as db:
        _id = db.get('_id_',-1)
        _id += 1
        db['_id_'] = _id
        return _id 

    """ To restart the memory, just delete the file
    what happpens:
        starts from -1: Hence the generated id starts from 0.
    """

# Read the json file, Load Data to Variable to contain the list of tasks (in form of dictionaries). 
def read_json():
    with open(file='task.json', mode='r', encoding='utf-8') as L:
        read_jsonData = json.load(L)
        return read_jsonData
        
# Add new task to the latest version of the list of tasks (in form of dictionaries).
def Add_to_list(new_task):
    nes = read_json()
    nes.extend(new_task)
    return nes

# Write the latest version of the list of tasks (in form of dictionaries) to a json file.
def write_json(latest_list):
    with open(file="task.json", mode='w', encoding= 'utf-8') as t:
        json.dump(latest_list,t,indent=4)

# Provide the index of the task dictionary required for other functions
def return_index(id_provided):
    for index, task_dict in enumerate(read_json()):
        id_found = next(iter(task_dict))
        if id_found == id_provided:
            return index
    return 'Bro, the ID you provided was not found! :('

# Object for Task 
class Task:
    def __init__(self,
                 task_placeholder,
                 _id_=assign_id(),
                 status = 'Not started',
                 time_of_creation = time_now,
                 time_of_update = None ):
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
        if not os.path.exists('task.json'):
            write_json(self.construct_task())
        else:
            write_json(Add_to_list(self.construct_task()))
        print(self.construct_task())
        print(f"TASK SUCCESSFULLY SAVED AS ID:{self.task_id}")
    
    
# Update task description of specific task in the list of task dictionaries.
def update_task_description(task_id,updated_description):
    _ID_= next(iter(read_json()[return_index(task_id)]))
    nested_dictionary = read_json()[return_index(task_id)].get(_ID_)
    _taskObject = Task(_id_=_ID_,
                        task_placeholder=updated_description,
                        status=nested_dictionary['status'],
                        time_of_creation=nested_dictionary['create time'],
                        time_of_update= time_now)
    updated_task = _taskObject.construct_task()
    task_history = read_json()
    task_history[return_index(task_id)] = updated_task
    write_json(task_history)
    print(updated_task)

    
    '''updatetime_of_task = nested_dictionary['update time']
       short_description = nested_dictionary['task description']'''
    
    
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

