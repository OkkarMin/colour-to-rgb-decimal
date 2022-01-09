from chalice import Chalice
from chalice.app import AuthResponse, BadRequestError, NotFoundError
from chalicelib import db

app = Chalice(app_name="colour-to-rgb-decimal")
app.api.cors = True


@app.authorizer()
def bearer_auth(auth_request):
    token = auth_request.token.replace("Bearer ", "")
    if token == "allow":
        return AuthResponse(routes=["*"], principal_id="user")
    else:
        return AuthResponse(routes=[], principal_id="user")


@app.route(
    "/colours",
    methods=["PUT"],
    authorizer=bearer_auth,
)
def add_new_colour():
    request_body = app.current_request.json_body

    if not request_body:
        raise BadRequestError("Must provide a JSON body")

    colour = request_body.get("colour")
    rgb = request_body.get("rgb")

    db.put_item({"colour": colour, "rgb": rgb})

    return request_body


@app.route(
    "/colours",
    methods=["GET"],
)
def get_all_colours():
    result = db.get_all_items()

    try:
        return result["Items"]
    except KeyError:
        raise NotFoundError(
            f"DynamoDB table seems to be empty. Please add some colour for items."
        )


@app.route(
    "/colours/{colour_in_string}",
    methods=["GET"],
)
def get_colour_to_rgb_decimal(colour_in_string):
    result = db.get_item(colour_in_string)

    try:
        return result["Item"]
    except KeyError:
        raise NotFoundError(f"No colour found for {colour_in_string}")


@app.route(
    "/colours/{colour_in_string}",
    methods=["DELETE"],
    authorizer=bearer_auth,
)
def remove_colour(colour_in_string):
    db.delete_item(colour_in_string)

    return {"message": f"Successfully deleted {colour_in_string}"}
