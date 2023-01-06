from flask import Flask, request
from fetch import *

import argparse

# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-p", "--Port", help = "Port number", default = 65432)

# Read arguments from command line
args = parser.parse_args()

f = Fetch({
  'http': 'socks5://127.0.0.1:'+str(args.Port),
  'https': 'socks5://127.0.0.1:'+str(args.Port)
})

# version 1
if __name__ == "__main__":
  app = Flask("pro_xy")

  # make a get request and return response text
  @app.route('/v1/get', methods=['GET'])
  def get():
    res = f.get(request.args.get("url"))
    return res

  # make a post request and return response text
  @app.route('/v1/post', methods=['POST'])
  def post():
    res = f.post(request.json["url"], request.json["headers"], request.json["body"])
    return res

  app.run()
