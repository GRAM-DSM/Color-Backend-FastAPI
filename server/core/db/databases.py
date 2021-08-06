from server.core.db import client

class Color_db:
    def __init__(self):
        self.db = client["color"]

    def get_post_col(self):
        return self.db["post"]

    def get_report_col(self):
        return self.db["report"]

    def get_user_col(self):
        return self.db["user"]
