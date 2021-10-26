from flask import Flask, request, jsonify
from blood_calculator import hdl_analysis


app = Flask(__name__)
# create a Flask class server running from __name__ module


# connect the function to the "app" using a decorator called route
@app.route("/", methods=["GET"])  # connect to no route, just the base url
@app.route("/index", methods=["GET"])
def server_status():
    return "Server is on"


@app.route("/info", methods=["GET"])
# the function name and the route name don't have to be the same
def info():
    my_output = "This server is for BME 547"
    return my_output


# @app.route("/hdl", methods=["POST"])
@app.route("/hdl/<hdl_value>", methods=["GET"])
# server functions should not have same name as imported functions,
# otherwise will overwrite
def hdl_analysis_server(hdl_value):
    """
    Input should look like {"hdl": 50, "patient_id": 200}
    This function is a Flask handler. It's attached to a route.
    It does/ should do three and only three things:
    (because it's hard to do pytest on flask handlers)
    """
    # in_data = request.get_json()  # get the data that's sent to it
    # hdl_value = in_data["hdl"]
    hdl_value = int(hdl_value)  # the val you entered in url is a string
    print("The hdl_value is {}".format(hdl_value))
    answer = hdl_analysis(hdl_value)  # call another function to do the work
    return jsonify(answer), 201  # return the answer


@app.route("/say_hello/<input_name>/<last_name>", methods=["GET"])
def say_hello(input_name, last_name):
    return "Hello, {} {}".format(input_name, last_name)


if __name__ == '__main__':
    app.run()
