from bayarea_relief import create_app


def main():
    app = create_app()
    app.run(host="0.0.0.0", port=8080)

