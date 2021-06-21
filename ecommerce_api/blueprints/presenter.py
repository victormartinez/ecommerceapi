from typing import Optional, Dict

from flask import jsonify, make_response


def create_response(
    status, code: str = None, message: str = None, data: Optional[Dict] = None
):
    return make_response(
        jsonify(
            {
                "success": 200 <= status < 300,
                "code": code,
                "message": None if not message else f"{message}",
                "data": data,
            }
        ),
        status,
    )


def exc_to_str(exc):
    try:
        return exc.args[0]
    except IndexError:
        return str(exc)
