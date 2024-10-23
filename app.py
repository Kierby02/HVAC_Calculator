from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    total_load = None
    tips = []

    if request.method == "POST":
        building_size = float(request.form["building_size"])
        insulation_r_value = float(request.form["insulation_r_value"])
        climate_zone_factor = float(request.form["climate_zone_factor"])
        num_occupants = int(request.form["num_occupants"])

        total_load = (building_size * climate_zone_factor) / insulation_r_value + (num_occupants * 100)

        if total_load > 30000:
            tips.append("Improve insulation.")
            tips.append("Use energy-efficient windows.")
        elif total_load > 20000:
            tips.append("Seal air leaks to reduce HVAC load.")
        else:
            tips.append("Your HVAC load is optimal! Keep maintaining your system.")

    return render_template("index.html", total_load=total_load, tips=tips)

if __name__ == "__main__":
    app.run(debug=True)