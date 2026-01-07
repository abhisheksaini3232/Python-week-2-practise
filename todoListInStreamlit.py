import streamlit as st
import pymongo

# Connection
@st.cache_resource
def init_connection():
    connectionString = ""
    return pymongo.MongoClient(connectionString)

client = init_connection()
db = client['projects']
todos = db['todoList']

class TodoList:
    def __init__(self):
        self.todos = db['todoList']

    def add_task(self, task_name):
        """Add new task to todoTask array"""
        self.todos.update_one({}, {'$push': {'todoTask': task_name}}, upsert=True)
        st.success(f"Added: '{task_name}'")

    def list_tasks(self):
        """Show all tasks with numbers"""
        tasks = self.get_all_tasks()
        if not tasks:
            st.warning("No tasks!")
            return
        st.subheader("Your Tasks:")
        for i, task in enumerate(tasks):
            st.write(f"{i+1}. {task}")

    def get_all_tasks(self):
        """Get raw task list"""
        doc = self.todos.find_one({}, {'todoTask': 1})
        return doc['todoTask'] if doc and 'todoTask' in doc else []

    def update_task(self):
        """Update task by number"""
        tasks = self.get_all_tasks()
        if not tasks:
            st.warning("No tasks to update!")
            return
        
        self.list_tasks()
        task_num = st.number_input("Enter task number to update:", min_value=1, max_value=len(tasks))
        index = int(task_num) - 1
        new_task = st.text_input("Enter new task name:", key="update_input")
        
        if st.button("Update Task") and new_task:
            self.todos.update_one({}, {'$set': {f'todoTask.{index}': new_task}})
            st.success("Task updated!")
            st.rerun()

    def delete_task(self):
        """Delete task by number"""
        tasks = self.get_all_tasks()
        if not tasks:
            st.warning("No tasks to delete!")
            return
        
        self.list_tasks()
        task_num = st.number_input("Enter task number to delete:", min_value=1, max_value=len(tasks))
        index = int(task_num) - 1
        task_name = tasks[index]
        
        if st.button("Delete Task"):
            self.todos.update_one({}, {'$pull': {'todoTask': task_name}})
            st.success("Task deleted!")
            st.rerun()

    def clear_all(self):
        """Delete all tasks"""
        self.todos.update_one({}, {'$set': {'todoTask': []}})
        st.success("All tasks cleared!")

st.title(" TODO APP")

todoList1 = TodoList()
optionSelected = st.selectbox("Choose option:", ["1. Add task", "2. List tasks", "3. Update task", "4. Delete task", "5. Clear all", "0. Exit"])

if optionSelected == "1. Add task":
    with st.form("add_form", clear_on_submit=True):
        task = st.text_input("Enter task:")
        if st.form_submit_button("Add"):
            todoList1.add_task(task)

elif optionSelected == "2. List tasks":
    todoList1.list_tasks()

elif optionSelected == "3. Update task":
    todoList1.update_task()

elif optionSelected == "4. Delete task":
    todoList1.delete_task()

elif optionSelected == "5. Clear all":
    if st.button("Clear All Tasks", type="primary"):
        todoList1.clear_all()

elif optionSelected == "0. Exit":
    st.stop()
