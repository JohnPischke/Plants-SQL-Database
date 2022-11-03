import sqlite3
con = sqlite3.connect('plants.db') # creates a console object
cur = con.cursor() # creates a cursor object
print()

#edits the frost tolerance for a specific plant
def edit_tolerance():   
    name = input("enter name of plant you want to edit ")
    tolerance = input("enter the new tolerance ")
    values = (tolerance,name)
    cur.execute("UPDATE plants SET frost_tolerance = ? WHERE name = ?", values)
    con.commit()

#edits the water for a specific plant
def edit_water():
    name = input("enter name of plant you want to edit ")
    water = input("enter the new water ")
    values = (water,name)
    cur.execute("UPDATE plants SET water = ? WHERE name = ?", values)
    con.commit()

#edits the sun for a specific plant
def edit_sun():
    name = input("enter name of plant you want to edit ")
    sun = input("enter the new sun ")
    values = (sun,name)
    cur.execute("UPDATE plants SET sun = ? WHERE name = ?", values)
    con.commit()

#edits the season for a specific plant
def edit_season():
    name = input("enter name of plant you want to edit ")
    season = input("enter the new season ")
    values = (season,name)
    cur.execute("UPDATE plants SET color = ? WHERE name = ?", values)
    con.commit()


#edits the type for a specific plant
def edit_type():
    name = input("enter name of plant you want to edit ")
    type = input("enter the new type ")
    values = (type,name)
    cur.execute("UPDATE plants SET type = ? WHERE name = ?", values)
    con.commit()

#edits the type for a specific plant
def edit_color():
    name = input("enter name of plant you want to edit ")
    color = input("enter the new color ")
    values = (color,name)
    cur.execute("UPDATE plants SET color = ? WHERE name = ?", values)
    con.commit()

#edits the name for a specific plant
def edit_name():
    name = input("enter name of plant you want to edit ")
    newname = input("enter the new name ")
    values = (newname,name)
    cur.execute("UPDATE plants SET name = ? WHERE name = ?", values)
    con.commit()

#calls the edit functions
def edit(): 
    print("1.) name")
    print("2.) color")
    print("3.) type")
    print("4.) season")
    print("5.) sun")
    print("6.) water")
    print("7.) frost tolerance")
    print()

    answer = input("enter which catagory you would like to edit: ")

    if answer == "1":
        edit_name()
    if answer == "2":
        edit_color()
    if answer == "3":
        edit_type()
    if answer == "4":
        edit_season()
    if answer == "5":
        edit_sun()
    if answer == "6":
        edit_water()
    if answer == "7":
        edit_tolerance()


# displays the database 
def display():
    cur.execute("SELECT name, color, type, season, sun, water, frost_tolerance from plants")
    print()
    print("Name,","Color,","Type,","Season,","Sun,","Water,","Frost-Tolerance")
    print()
    for row in cur:
        print(row[0],",",row[1],",",row[2],",",row[3],",",row[4],",",row[5],",", row[6])
        print()


# deletes a plant based on the name of the plant 
def delete():
    name = input("enter name of plant you want to delete " )
    name = (name,)
    cur.execute("DELETE from plants where name = ?;", name)
    con.commit()

# adds a new plant to the database
def insert():
  name = input("enter name: ")
  color = input("enter color: ")
  type = input("enter type: ")
  season = input("enter season: ")
  sun = input("enter sun: ")
  water = input("enter water: ")
  frost = input("enter frost tolerance: ")
  values = (name,color,type,season,sun,water,frost)
  cur.execute("INSERT INTO plants VALUES (?,?,?,?,?,?,?)",values)
  con.commit()


# this is the options loop that keeps going until you enter 5
while(True):

    print("1.) Display all plants in database")
    print("2.) Add a plant to the database")
    print("3.) remove a plant from the database")
    print("4.) edit a plant in the database")
    print("5.) exit")
    print()


    answer = input("enter number of chosen option: ")
    if answer == "2":
        insert()
    if answer == "3":
        delete()
    if answer == "1":
        display()
    if answer == "4":
        edit()
    if answer == "5":
        break
con.close()