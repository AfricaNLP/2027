#!/usr/bin/env python3
"""Local preview server.

GitHub Pages serves /cfp for cfp.html; python3 -m http.server does not.
This adds that one behaviour so the local preview matches the live site.

    python3 serve.py        then open http://127.0.0.1:4027
"""

import http.server
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 4027


class Handler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        local = super().translate_path(path)
        if not os.path.exists(local) and not path.endswith("/"):
            candidate = local + ".html"
            if os.path.isfile(candidate):
                return candidate
        return local


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler) as httpd:
        print("Serving http://127.0.0.1:%d" % PORT)
        httpd.serve_forever()
