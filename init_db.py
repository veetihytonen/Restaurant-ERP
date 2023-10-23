from sqlalchemy import create_engine
from sqlalchemy.sql import text
from config import DATABASE_URI
from werkzeug.security import generate_password_hash

engine = create_engine(DATABASE_URI)

def init_db() -> None:
    with engine.connect() as conn:
        dt = open("./drop_db.sql")
        drop_tables = text(dt.read())
        dt.close()
        conn.execute(drop_tables)
        conn.commit()

        schema = open("./schema.sql")
        queries = text(schema.read())
        schema.close()
        conn.execute(queries)
        conn.commit()

        ingredients = [('lettuce', 'Kylmä'), ('tomato_diced', 'Kylmä'), ('tortilla', 'Kuiva')]

        ingr_sql = text('INSERT INTO ingredients (name, storage_category) VALUES (:name, :strg_ctgr)')

        for ingr in ingredients:
            name = ingr[0]
            strg_ctgr = ingr[1]
            conn.execute(ingr_sql, {'name':name, 'strg_ctgr':strg_ctgr})
        conn.commit()

        admin_hash = generate_password_hash('salis')

        admin_sql = ("INSERT INTO users (username, password, role) VALUES ('hyde', :password, 2)")

        conn.execute(text(admin_sql), {'password': admin_hash})
        conn.commit()
