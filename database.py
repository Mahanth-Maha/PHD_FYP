import datetime
import sqlite3


class ImagesDB:
    def __init__(self) -> None:
        self.db_name = "./database/image_database.db"
        self.conn = sqlite3.connect(self.db_name)
        try:
            self.conn.execute(
                "CREATE TABLE images (latitude REAL, longitude REAL, time TEXT, name TEXT, path TEXT)")
        except sqlite3.OperationalError:
            pass
        self.conn.close()
        self.cursor = None

    def extract_recent_rows(self):
        if self.cursor.rowcount == 0:
            print("No DATA")
            return False
        sql_query = "SELECT * FROM images ORDER BY time DESC LIMIT 25"
        result = self.cursor.execute(sql_query)
        # for row in result:
        #     print(row)

        return result.fetchall()

    def Run(self, func, *args):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        result = func(*args)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        return result

    def insert_data(self, lat_i, long_i, img_name, img_path):
        current_time = datetime.datetime.now()
        current_time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO images  (latitude, longitude, time, name, path) VALUES (?, ?, ?, ?, ?)",
                            (lat_i, long_i, current_time_str, img_name, img_path))
        return None

    def delete_all_rows(self):
        self.cursor.execute("DELETE FROM images")
        return None

    def phd_markers_generator(self):
        res = self.Run(self.extract_recent_rows)
        print(res)
        locs = [(i[0], i[1]) for i in res]
        print(locs)
        return locs


def main():
    db = ImagesDB()

    db.Run(db.insert_data, 37.4220, -122.0841,
           'image1.jpg', 'path/to/image1.jpg')
    db.Run(db.insert_data, 37.4300, -122.0900,
           'image2.jpg', 'path/to/image2.jpg')

    Res = db.Run(db.extract_recent_rows)
    print(Res)

    # db.Run(db.delete_all_rows)

    db.Run(db.insert_data, 100, 150, "Hello.jpg", "path/l/hel.jpg")
    db.Run(db.insert_data, 200, 250.0, "Hi.jpg", "path/l/hi.jpg")

    Res = db.Run(db.extract_recent_rows)
    print(Res)
    db.Run(db.delete_all_rows)
    db.Run(db.extract_recent_rows)
    print(Res)


if __name__ == '__main__':
    main()
