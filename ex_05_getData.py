
from ex_01_conection_to_db import *
from ex_02_create_tables import *
from ex_03_add_project_and_task import *
from ex_04_selecty import *


conn = create_connection("database.db")

# wszystkie projekty

select_all(conn, "projects")

# wszystkie zadania

select_all(conn, "tasks")

# wszystkie zadania dla projektu o id 1

select_where(conn, "tasks", projekt_id=1)

# wszystkie zadania ze statusem ended

select_where(conn, "tasks", status="ended")

# wszystkie zadania ze statusem started

select_where(conn, "tasks", status="started")

