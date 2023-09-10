import sqlite3

conexion = sqlite3.connect("nippa_sensors.db")
conexion.execute("""create table if not exists ICM20948 (
                          ID integer primary key AUTOINCREMENT,
                          time text,
                          ax text,
                          ay text,
                          az text,
                          gx text,
                          gy text,
                          gz text,
                          bx text,
                          by text,
                          bz text                                                    
                    )""")
conexion.execute("""create table if not exists BME280 (
                          ID integer primary key AUTOINCREMENT,
                          time text,
                          temp text,
                          humidity text,
                          pressure text,
                          altitude text                    
                    )""")
