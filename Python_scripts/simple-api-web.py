from flask import Flask, redirect, render_template_string, request, url_for

app = Flask(__name__)

# A simple in-memory database to store tasks
tasks = [
    {"id": 1, "title": "Learn Python Flask", "done": False},
    {"id": 2, "title": "Build a web interface", "done": True},
]

# Simple HTML template embedded right inside the file for easy testing
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple Todo App</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 500px; margin: 40px auto; padding: 20px; background: #f4f4f9; }
        h1 { color: #333; text-align: center; }
        form { display: flex; gap: 10px; margin-bottom: 20px; }
        input[type="text"] { flex: 1; padding: 10px; font-size: 16px; border: 1px solid #ccc; border-radius: 4px; }
        button { padding: 10px 20px; background: #28a745; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; }
        button:hover { background: #218838; }
        ul { list-style-type: none; padding: 0; }
        li { background: white; padding: 12px; margin-bottom: 8px; border: 1px solid #ddd; border-radius: 4px; display: flex; justify-content: space-between; align-items: center; }
        .done { text-decoration: line-through; color: gray; }
        a { text-decoration: none; padding: 4px 8px; background: #007bff; color: white; border-radius: 3px; font-size: 12px; }
        a:hover { background: #0056b3; }
    </style>
</head>
<body>
    <h1>My Todo List</h1>
    
    <!-- Form to add a new task (Sends a POST request) -->
    <form action="/add" method="POST">
        <input type="text" name="title" placeholder="Enter a new task..." required>
        <button type="submit">Add Task</button>
    </form>

    <!-- List of existing tasks -->
    <ul>
        {% for task in tasks %}
            <li>
                <span class="{% if task.done %}done{% endif %}">{{ task.title }}</span>
                <a href="/toggle/{{ task.id }}">
                    {% if task.done %}Undo{% else %}Complete{% endif %}
                </a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
"""


# 1. Route to display the web page
@app.route("/")
def index():
  return render_template_string(HTML_PAGE, tasks=tasks)


# 2. Route to handle adding a new task from the web form (POST request)
@app.route("/add", methods=["POST"])
def add_task():
  title = request.form.get("title")  # Grabs data typed into the form input field
  if title:
    new_id = len(tasks) + 1
    tasks.append({"id": new_id, "title": title, "done": False})
  return redirect(url_for("index"))  # Send user back to the home page


# 3. Route to toggle a task's status between done and undone
@app.route("/toggle/<int:task_id>")
def toggle_task(task_id):
  for task in tasks:
    if task["id"] == task_id:
      task["done"] = not task["done"]  # Flips True to False, or False to True
      break
  return redirect(url_for("index"))


if __name__ == "__main__":
  app.run(debug=True)