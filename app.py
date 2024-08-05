from flask import Flask, request, render_template

from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"


@app.route('/')
def ask_questions():
    """Send to form page"""

    prompts = story.prompts

    return render_template('questions.html', prompts = prompts)


@app.route('/story')
def generate_story():
    """replace prompt with user input for story"""

    text = story.generate(request.args)

    return render_template('story.html', text = text)




