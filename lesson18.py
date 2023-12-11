from flask import Flask, Response, request, render_template, redirect, url_for
from sqlalchemy import exc
from crud import get_note, create_note, get_all_notes
from models import create_tables, drop_tables

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/",
)

drop_tables()
create_tables()


@app.route('/publish', methods=["GET"])
def get_publish_view():
    return render_template("publish_form.html")


@app.route('/publish', methods=["POST"])
def publish_note_view():
    note_data = request.form
    note = create_note(
        title=note_data["title"],
        content=note_data["content"]
    )
    return redirect(url_for("notes_view", note_uuid=note.uuid))


@app.route('/<note_uuid>', methods=["GET"])
def notes_view(note_uuid: str):
    try:
        note = get_note(note_uuid)
    except exc.NoResultFound:
        return Response("Идентификатор не найден!", status=404)
    return render_template(
        "note.html",
        note_uuid=note.uuid,
        title=note.title,
        content=note.content,
        created_at=note.created_at
    )


@app.route("/", methods=["GET"])
def home_page_view():
    all_notes = get_all_notes()
    return render_template("home.html", notes=all_notes)
