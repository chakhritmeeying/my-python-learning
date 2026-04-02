from flask import Flask, request, redirect
from app import TodoList


app = Flask(__name__)

todo_list = TodoList()
todo_list.load_tasks()


@app.route("/")
def home():
    return """
    <title>To Do List</title>
    <h1>----To Do List Program----</h1>
    <p><a href="/veiwtasks" target="_blank">Veiw Tasks.</a></p>
    """


@app.route("/veiwtasks")
def show_tasks():
    output = ""

    for idx, task in enumerate(todo_list.tasks):
        status = "✔" if task["done"] else "❌"
        output += f"""<li>
        
        <form action='/update-task' method='post'>
            {task['text']} | {status}
            <input type='hidden' name='update_index' value="{idx}">
            <button type='submit'>{'Undo' if task['done'] else 'Done'}</button>
            
        </form>
        <form action='/delete-task' method='post'>
            <input type='hidden' name='delete_index' value="{idx}">
            <button type='submit'>Delete</button>
        </form>
        </li>"""

    return f"""
    <h1>My To Do Lists.</h1>
    <ul>{output}</ul>
    <br>
    <h2>Add new task</h2>
    <form action="/add" method="post">
        <input type="text" name="task" placeholder="Enter task">
        <button type="submit">Add</button>
    </form>
"""


@app.route("/delete-task", methods=['POST'])
def delete_task():
    index = request.form.get("delete_index")
    if index is not None:
        index = int(index)
        delete_task = todo_list.delete_task(index)
        todo_list.save_tasks()

    return f"""
    <title>Delete Complete</title>
    <p>{delete_task['text']} has been deleted.</p>
    <p><a href="/veiwtasks">Back to list</a></p>
    """


@app.route("/update-task", methods=['POST'])
def update_task():
    index = request.form.get("update_index")
    if index is not None:
        index = int(index)
        todo_list.update_task(index)

    return redirect("/veiwtasks")


@app.route("/add", methods=['POST'])
def add_task():
    new_task = request.form.get("task")

    if new_task:
        todo_list.add_task(new_task)
        todo_list.save_tasks()

    return """
    <title>Add tasks</title>
    <p>Task Added.</p>
    <p><a href="/veiwtasks">Back to list</a></p>
    """


@app.errorhandler(404)
def not_found(e):
    return f"""
    <title>Page not found</title>
    Page not found 😢
    """, 404


if __name__ == "__main__":
    app.run(debug=True)
