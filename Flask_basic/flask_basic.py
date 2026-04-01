from flask import Flask, request
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

    for task in todo_list.tasks:
        status = "✔" if task["done"] else "❌"
        output += f"""<li>
        <form action='/update-task' method='post'>
            {task['text']} | {status}
            <button type="submit">{'Undo' if task['done'] else 'Done'}</button>
        </li></form>"""

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
