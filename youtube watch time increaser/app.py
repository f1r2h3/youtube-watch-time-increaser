from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('youtube_watch_time_increaser.html')

# You can add more routes as needed

if __name__ == "__main__":
    app.run(debug=True)
