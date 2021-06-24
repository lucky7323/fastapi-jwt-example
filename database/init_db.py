import sqlite3
import bcrypt


pass1 = "qwerqwer"
pass2 = "qwer1234!!"


if __name__ == "__main__":
    conn = sqlite3.connect("dayoff.db")
    cur = conn.cursor()

    cur.executemany(
        'INSERT INTO tb_user VALUES (?, ?, ?, ?)',
        [(None,
          'eunho@test.com',
          bcrypt.hashpw(pass1.encode("utf-8"), bcrypt.gensalt()).decode(),
          1624513520),
         (None,
          'dookyung03@test.com',
          bcrypt.hashpw(pass2.encode("utf-8"), bcrypt.gensalt()).decode(),
          1624515525)
        ]
    )

    conn.commit()


