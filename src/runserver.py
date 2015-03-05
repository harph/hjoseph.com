#!/usr/bin/env python
import argparse
from app import WebApp


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--host", help="Server host", default='127.0.0.1')
    parser.add_argument(
        "--port", help="Server port", default=5000)
    args = parser.parse_args()
    web_app = WebApp()
    flask_app = web_app.create_app()
    flask_app.run(host=args.host, port=int(args.port))
