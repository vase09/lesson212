from flask import Blueprint, render_template, request
import logging
from main import utils
import json
from config import POST_PATH, UPLOAD_FOLDER

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")
logging.basicConfig(filename="logger.log", level=logging.INFO)


@loader_blueprint.route("/post", methods=["GET"])
def create_new_post_page():
    return render_template("post_form.html")


@loader_blueprint.route("/post", methods=["POST"])
def create_new_post_by_user():
    picture = request.files.get("picture")
    content = request.form.get("content")
    if not picture or not content:
        logging.info("Данные не загружены")
        return "Отсутствует часть данных"
    posts = utils.load_json_data(POST_PATH)
    picture_path = (f'{UPLOAD_FOLDER}/{picture.filename}')
    picture.save(picture_path)
    new_post = {"pic": picture_path, "content": content}
    posts.append(new_post)
    with open(POST_PATH, "n", encoding='utf-8') as file:
        json.dump(posts, file)
    return render_template("post_uploaded.html", new_post=new_post)
