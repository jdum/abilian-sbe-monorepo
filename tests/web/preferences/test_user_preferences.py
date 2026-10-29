# Copyright (c) 2012-2024, Abilian SAS

""""""

from __future__ import annotations

from io import BytesIO
from pathlib import Path

from flask import request, url_for
from flask_login import login_user
from PIL import Image

from abilian.core.models.subjects import create_root_user
from abilian.web.preferences.user import UserPreferencesForm

AVATAR_COLORMAP = Path(__file__).parent / "avatar-colormap.png"


def test_form_photo(app, db) -> None:
    user = create_root_user()
    url = url_for("preferences.user")
    uploads = app.extensions["uploads"]
    with AVATAR_COLORMAP.open("rb") as f:
        handle = uploads.add_file(user, f, filename="avatar.png", mimetype="image/png")

    kwargs = {"method": "POST", "data": {"photo": handle}}

    with app.test_request_context(url, **kwargs):
        login_user(user)
        form = UserPreferencesForm(request.form)
        form.validate()
        assert form.photo.data is not None

        img_data = form.photo.data
        with Image.open(BytesIO(img_data)) as img:
            img_type = (img.format or "").lower()
        # ???: should be 'png' but is 'jpeg' on Python 2
        assert img_type in ("png", "jpeg")
