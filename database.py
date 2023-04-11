import datetime
import sqlite3


class ImagesDB:
    def __init__(self) -> None:
        self.recent = 90
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
        current_date = datetime.datetime.today()
        past_date = current_date - datetime.timedelta(days=self.recent)
        current_time_str = past_date.strftime("%Y-%m-%d %H:%M:%S")
        # new_sql_query = "SELECT * FROM images WHERE time >= DATE_SUB(NOW(), INTERVAL 90 DAY) AND time < NOW() ORDER BY time DESC"
        # Nolimit_sql_query = "SELECT * FROM images ORDER BY time DESC LIMIT 25"
        sql_query = 'SELECT * FROM images WHERE time >= "' + current_time_str + '" ORDER BY time DESC'
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

    def insert_data(self, lat_i, long_i, img_name, img_path,debug=False):
        current_time = datetime.datetime.now()
        if debug:
            current_time = datetime.date(2020, 1, 1)
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
    
    def print_db(self):
        K = self.cursor.execute("SELECT * FROM images")
        print("-"*25+'\nDATABASE\n'+"-"*25)
        for row in K:
            print(row)
        print("-"*25+'\END\n'+"-"*25)
        return K.fetchall()


def main():
    db = ImagesDB()

    for i in range(20):
        db.Run(db.insert_data, 37.4220+i, -122.0841+i,'image1.jpg', 'path/to/image1.jpg',i%2)
    db.Run(db.insert_data, 37.4300, -122.0900,
           'image2.jpg', 'path/to/image2.jpg')
    # db.Run(db.print_db)
    # Res = db.Run(db.extract_recent_rows)
    # print(Res,"image")

    # db.Run(db.delete_all_rows)

    db.Run(db.insert_data, 100, 150, "Hello.jpg", "path/l/hel.jpg")
    db.Run(db.insert_data, 200, 250.0, "Hi.jpg", "path/l/hi.jpg",True)
    db.Run(db.print_db)
    print('='*20 + "MARKERs" + '='*20 )
    # db.Run(db.phd_markers_generator)
    Res = db.Run(db.extract_recent_rows)
    print(Res)
    db.Run(db.delete_all_rows)
    db.Run(db.extract_recent_rows)
    print(Res)


if __name__ == '__main__':
    main()
