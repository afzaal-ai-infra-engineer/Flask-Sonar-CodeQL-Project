from flask import Flask, render_teimplate_string

app = Flask(__name__)n

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Afzaal DevOps & Ai infra Engineer - Flask Project</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background: #f4f6f9;
            }
            header {
                background: #222;
                color: white;
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 15px 40px;
            }
            header img {
                height: 50px;
            }
            nav {
                background: #444;
                padding: 10px;
                text-align: center;
            }
            nav a {
                color: white;
                margin: 0 15px;
                text-decoration: none;
                font-weight: bold;
            }
            nav a:hover {
                color: #ff9800;
            }
            .container {
                padding: 40px;
                text-align: center;
            }
            h1 {
                font-size: 2.5rem;
                margin-bottom: 20px;
                color: #333;
            }
            p {
                font-size: 1.2rem;
                color: #555;
                line-height: 1.6;
                max-width: 800px;
                margin: 0 auto;
            }
        </style>
    </head>
    <body>
        <header>
            <img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg" alt="Flask Logo">
            <h2>Afzaal DevOps</h2>
            <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Devops-toolchain.svg" alt="DevOps Logo">
        </header>

        <nav>
            <a href="#">Home</a>
            <a href="#">Projects</a>
            <a href="#">Blog</a>
            <a href="#">Contact</a>
        </nav>

        <div class="container">
            <h1>Afzaal DevOps & Ai infra Engineer</h1>
            <p>
                Today I explored Flask, a lightweight but powerful Python framework.
                I learned how its structure works, what libraries developers commonly use, 
                and how it powers web and mobile projects. From a DevOps perspective, 
                I understood my role in setting up environments, pipelines, containerization, 
                and monitoring. This deep learning session gave me the confidence to contribute 
                effectively to real-world Flask projects.
            </p>
        </div>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
