from flask import Flask, request, jsonify
import tools
import database

app = Flask(__name__)

# Initialize DB
database.init_db()

@app.route("/mcp", methods=["POST"])
def handle_request():
    data = request.json
    query = data.get("query").lower()

    if "weather" in query:
        city = query.split()[-1]
        result = tools.get_weather(city)

    elif any(op in query for op in ["+", "-", "*", "/"]):
        result = tools.calculate(query)

    elif "employee" in query:
        try:
            emp_id = int(query.split()[-1])
            result = tools.get_employee(emp_id)
        except:
            result = "Invalid employee ID"

    else:
        result = "No tool matched"

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(port=5000)