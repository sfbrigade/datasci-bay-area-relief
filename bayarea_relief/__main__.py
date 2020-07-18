from bayarea_relief import app
from bayarea_relief.settings import DEBUG


def main():
    app.run(host="0.0.0.0", port=8000, debug=DEBUG)


if __name__ == '__main__':
    main()
