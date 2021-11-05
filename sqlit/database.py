
import sqlite3


def main():
    db = sqlite3.connect("information1.db")
    db.row_factory = sqlite3.Row
    db.execute("create table if not exists Admin(name text,age int)")
    db.execute("insert into Admin(name,age) values (?, ?)", ('mostfa', 21))
    db.commit()
    curses = db.execute("select * from Admin")
    for row in curses:
        print("name {} age {} ".format(row["name"], row["age"]))

    db.close()


if __name__ == '__main__':
    main()
