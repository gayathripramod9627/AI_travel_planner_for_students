from flask import Flask, request, render_template_string

app = Flask(__name__)

# ---------------- AI Travel Planner Logic ---------------- #
def generate_itinerary(destination, days, budget):
    daily_budget = budget // days

    activities_list = [
        "Visit local heritage sites",
        "Explore famous markets",
        "Relax in city parks",
        "Visit museums and cultural centers",
        "Street food exploration"
    ]

    plan = []
    for day in range(1, days + 1):
        plan.append({
            "day": day,
            "activity": activities_list[day % len(activities_list)],
            "food": "Affordable local eateries",
            "transport": "Public transport / Walking",
            "cost": daily_budget
        })

    return plan, daily_budget

# ---------------- Home Page ---------------- #
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        destination = request.form["destination"]
        days = int(request.form["days"])
        budget = int(request.form["budget"])

        plan, daily_budget = generate_itinerary(destination, days, budget)

        return render_template_string(RESULT_HTML,
                                      destination=destination,
                                      days=days,
                                      budget=budget,
                                      daily_budget=daily_budget,
                                      plan=plan)

    return render_template_string(HOME_HTML)

# ---------------- HTML Templates ---------------- #
HOME_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Travel Planner for Students</title>
    <style>
        body { font-family: Arial; background: #f2f4f8; text-align: center; }
        form { background: white; padding: 20px; width: 300px; margin: auto; border-radius: 10px; }
        input, button { width: 90%; padding: 8px; margin: 8px; }
        button { background: #007bff; color: white; border: none; cursor: pointer; }
    </style>
</head>
<body>
    <h1>AI Travel Planner for Students</h1>
    <form method="post">
        <input type="text" name="destination" placeholder="Destination" required>
        <input type="number" name="days" placeholder="Number of Days" required>
        <input type="number" name="budget" placeholder="Total Budget (₹)" required>
        <button type="submit">Generate Plan</button>
    </form>
</body>
</html>
"""

RESULT_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Travel Itinerary</title>
    <style>
        body { font-family: Arial; background: #eef1f5; text-align: center; }
        .card { background: white; margin: 10px auto; padding: 15px; width: 60%; border-radius: 8px; }
        a { text-decoration: none; color: #007bff; }
    </style>
</head>
<body>
    <h2>Trip Plan for {{ destination }}</h2>
    <p><b>Total Budget:</b> ₹{{ budget }}</p>
    <p><b>Daily Budget:</b> ₹{{ daily_budget }}</p>

    {% for day in plan %}
        <div class="card">
            <h3>Day {{ day.day }}</h3>
            <p><b>Activity:</b> {{ day.activity }}</p>
            <p><b>Food:</b> {{ day.food }}</p>
            <p><b>Transport:</b> {{ day.transport }}</p>
            <p><b>Estimated Cost:</b> ₹{{ day.cost }}</p>
        </div>
    {% endfor %}

    <a href="/">Plan Another Trip</a>
</body>
</html>
"""

# ---------------- Run App ---------------- #
if __name__ == "__main__":
    app.run(debug=True)
