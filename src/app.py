import os, sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from flask import Flask
from src import views

app = Flask(__name__)


# url routes
app.add_url_rule("/", view_func=views.root, methods=["GET"])
app.add_url_rule("/create_file", view_func=views.create_file, methods=["POST"])
app.add_url_rule("/delete_file/<audioFileType>/<audioFileID>", view_func=views.delete_file, methods=["DELETE"])
app.add_url_rule("/update_file/<audioFileType>/<audioFileID>", view_func=views.update_file, methods=["PUT"])
app.add_url_rule("/get_file/<audioFileType>/<audioFileID>", view_func=views.get_file, methods=["GET"])
app.add_url_rule("/get_file/<audioFileType>", view_func=views.get_file, methods=["GET"], defaults={"audioFileID": None})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)