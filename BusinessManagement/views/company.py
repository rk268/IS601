from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
#import pycountry
company = Blueprint('company', __name__, url_prefix='/company')

@company.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS

    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count as employees for the company
    # don't do SELECT *
    #rk268 4/21
    query = """SELECT id, name, address, city, country , state, zip, website, (SELECT count(id) FROM IS601_MP3_Employees WHERE c.id=company_id GROUP BY company_id)
        as employees from IS601_MP3_Companies as c WHERE 1=1"""

    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["name", "city", "country", "state"]
    # TODO search-2 get name, country, state, column, order, limit request args
    #rk268 4/21
    name = request.args.get("name")
    state = request.args.get("state")
    country = request.args.get("country")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit")

    company_dict={}
    # TODO search-3 append a LIKE filter for name if provided
    #rk268 4/21
    if(name != ""):
        company_dict["name"] = "%"+str(name)+"%"
        query= query+ """ AND name like %(name)s """

    # TODO search-4 append an equality filter for country if provided
    #rk268 4/21
    if country:
        query = query+ """ AND country = %(country)s"""
        company_dict["country"] = country

    # TODO search-5 append an equality filter for state if provided
    #rk268 4/21
    if state:
        query = query+ """ AND state = %(state)s"""
        company_dict["state"] = state

    # TODO search-6 append sorting if column and order are provided and within the allows columsn and allowed order asc,desc
    #rk268 4/21 
    if column and order:
        if column in allowed_columns and order in ["asc", "desc"]:
            query = query + " ORDER BY {} {}".format(column.lower(), order.lower())
            company_dict["col_name"] = column.lower()
            company_dict["order"] = order.lower()

    # TODO search-7 append limit (default 10) or limit greater than 1 and less than or equal to 100

    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
    #rk268 4/21
        if(limit!=None):
            if(int(limit) > 0 and int(limit) <= 100):
                query = query+ " LIMIT %(limit)s"
                company_dict["limit"] = int(limit)
        else:
            print("Limit is out of bound, please enter values greater than 0 and less than 101")
            flash("Limit out of bound(1 to 100) or not selected","warning")
    else:
        print("Entered value is not integer, Please enter a valid integer value")


    
    args = company_dict

    #limit = 10 # TODO change this per the above requirements
    #query += " LIMIT %(limit)s"
    #args["limit"] = limit
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, args)
        #print(f"result {result.rows}")
        if result.status:
            rows = result.rows
            print(f"rows {rows}")
    except Exception as e:
        # TODO search-9 make message user friendly
        #rk268 4/21
        flash("Error!! - Cannot fetch the required data", "Danger")
        print(str(e))
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    allowed_columns = [(v,v) for v in allowed_columns]
    return render_template("list_companies.html", rows=rows, allowed_columns=allowed_columns)
    

@company.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        n =  request.form.get("name")
        add =  request.form.get("address")
        city = request.form.get("city")
        website = request.form.get("website")
        zip =  request.form.get("zip")
        country = request.form.get("country")
        state = request.form.get("state")
        print(n)
        #rk268 4/21

        if(n == ""):
            flash("please enter name", "warning")
            has_error = True
            return render_template("add_company.html")
        else:
            has_error = False
        #rk268 4/21

        if(add == ""):
            flash("please enter address", "warning")
            has_error = True
            return render_template("add_company.html")
        else:
            has_error = False
        #rk268 4/21

        if(city == ""):
            flash("please enter city", "warning")
            has_error = True
            return render_template("add_company.html")
        else:
            has_error = False
        #rk268 4/21

        if(zip == ""):
            flash("please enter zip", "warning")
            has_error = True
            return render_template("add_company.html")
        else:
            has_error = False
        #rk268 4/21

        if(country == ""):
            flash("please enter country", "warning")
            has_error = True
            return render_template("add_company.html")
        else:
            has_error = False
        #rk268 4/21
        if(state == ""):
            flash("please enter state", "warning")
            has_error = True
            return render_template("add_company.html")
        else:
            has_error = False
        #rk268 4/21

            

        company_dict={}
        company_dict["name"] = n
        company_dict["address"] = add
        company_dict["city"] = city
        company_dict["website"]= website
        company_dict["zip"]= zip
        company_dict["country"]= country
        company_dict["state"]= state
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        # TODO add-2 name is required (flash proper error message)
        # TODO add-3 address is required (flash proper error message)
        # TODO add-4 city is required (flash proper error message)
        # TODO add-5 state is required (flash proper error message)
        # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
        # hint see geography.py and pycountry documentation
        # TODO add-6 country is required (flash proper error message)
        # TODO add-6a country should be a valid country mentioned in pycountry
        # hint see geography.py and pycountry documentation
        # TODO add-7 website is not required
        # TODO add-8 zipcode is required (flash proper error message)
        # note: call zip variable zipcode as zip is a built in function it could lead to issues

        # use this to control whether or not an insert occurs
        print(company_dict)

        if not has_error:
            try:
                #rk268 4/21
                result = DB.insertOne("""INSERT INTO IS601_MP3_Companies (name, address, city, country,state,zip,website)
                    VALUES (%(name)s, %(address)s, %(city)s, %(country)s, %(state)s, %(zip)s, %(website)s)
                    ON DUPLICATE KEY UPDATE 
                    name = %(name)s, address = %(address)s, 
                    city = %(city)s, country =%(country)s, state = %(state)s , zip = %(zip)s , website = %(website)s""",company_dict
                ) # <-- TODO add-8 add query and add arguments
                print(result)
                if result.status:
                #rk268 4/21
                    flash("Added Company", "success")
            except Exception as e:
                # TODO add-9 make message user friendly
                flash("Company not added", "danger")
        
    return render_template("add_company.html")

@company.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    # UCID: rk268 Date: 08/09/2023
    #id = False
    id = request.args.get("id")
    print(id)
    if not id: # TODO update this for TODO edit-1
        flash("Id not find. Redirecting to search..","warning")
        return redirect(url_for("company.search"))
    else:
        if request.method == "POST":
            data = {} # use this as needed, can convert to tuple if necessary
            # TODO edit-1 retrieve form data for name, address, city, state, country, zip, website
            # UCID: rk268 Date: 08/09/2023
            name = request.form.get("Name")
            address = request.form.get("address")
            city = request.form.get("city")
            state = request.form.get("state")
            country = request.form.get("country")
            zipcode = request.form.get("zip")
            website = request.args.get("website")
            if(request.form.get("website")):
                website = request.form.get("website")
            has_error = False # use this to control whether or not an insert occurs

            # TODO edit-2 name is required (flash proper error message)
            # UCID: rk268 Date: 08/09/2023
            if(name==""):
                flash("Name cannot be empty ","danger")
                has_error = True
            # TODO edit-3 address is required (flash proper error message)
            # UCID: rk268 Date: 08/09/2023
            if(address==""):
                flash("Address cannot be empty ","danger")
                has_error = True
            # TODO edit-4 city is required (flash proper error message)
            # UCID: rk268 Date: 08/09/2023
            if(city==""):
                flash("City cannot be empty ","danger")
                has_error = True
            # TODO edit-5 state is required (flash proper error message)
            # UCID: rk268 Date: 08/09/2023
            if(state==""):
                flash("State cannot be empty ","danger")
                has_error = True
            # TODO edit-5a state should be a valid state mentioned in pycountry for the selected state
            # hint see geography.py and pycountry documentation
            # UCID: rk268 Date: 08/09/2023
            # TODO edit-6 country is required (flash proper error message)
            # UCID: rk268 Date: 08/09/2023
            if(country==""):
                flash("Country cannot be empty ","danger")
                has_error = True
            # TODO edit-6a country should be a valid country mentioned in pycountry
            # UCID: rk268 Date: 08/09/2023
            # hint see geography.py and pycountry documentation
            # TODO edit-7 website is not required
            # UCID: rk268 Date: 08/09/2023
            flash("Website is optional ","warning")
            # TODO edit-8 zipcode is required (flash proper error message)
            # UCID: rk268 Date: 08/09/2023
            if(zipcode==""):
                flash("Zip cannot be empty.","danger")
                has_error = True
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            # populate data dict with mappings
            
            data["name"] = name
            data["address"] = address
            data["city"] = city
            data["website"]= website
            data["state"]= state
            data["country"] = country
            data["zipcode"]= zipcode
            data["c_id"]=id
            if not has_error:
                try:
                    # TODO edit-9 fill in proper update query
                    # UCID: rk268 Date: 08/09/2023
                    # name, address, city, state, country, zip, website
                    result = DB.update("""UPDATE IS601_MP3_Companies SET name=%(name)s, address=%(address)s, 
                                    city=%(city)s, website=%(website)s, state=%(state)s, country=%(country)s, 
                                    zip=%(zipcode)s  WHERE id=%(c_id)s
                    """, data)
                    if result.status:
                        print("updated record")
                        flash("Updated record", "success")
                    return redirect(url_for('company.search', name="", order="asc", column="", limit=10))
                except Exception as e:
                    # TODO edit-10 make this user-friendly
                    # UCID: rk268 Date: 08/09/2023
                    print(f"{e}")
                    flash("Error!!The updation of the database failed", "danger")
        row = {}
        try:
            # TODO edit-11 fetch the updated data
            # UCID: rk268 Date: 08/09/2023
            result = DB.selectOne("""SELECT id, name, address, city, country , state, zip, website 
                                FROM IS601_MP3_Companies WHERE id=%s""", id)
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-12 make this user-friendly
            # UCID: rk268 Date: 08/09/2023
            flash("Error occured! The data cannot be retrived", "danger")
    # TODO edit-13 pass the company data to the render template
    # UCID: rk268 Date: 08/09/2023
    return render_template("edit_company.html", company=row)

@company.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete company by id (unallocate any employees see delete-5)
    # TODO delete-2 redirect to company search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    # TODO delete-5 for all employees assigned to this company set their company_id to None/null
    # TODO delete-6 if id is missing, flash necessary message and redirect to search
    id = request.args.get("id")
    print("##########################################")
    print(id)
    try:
        result = DB.update(f"UPDATE IS601_MP3_Employees SET company_id=NULL WHERE company_id={id}")
        if result.status:
            flash("Successfully unallocated employees in the company", "success")
        result1 = DB.delete(f"DELETE FROM IS601_MP3_Companies WHERE id={id}")    
        if result1.status:
            flash("Successfully deleted the company", "success")
    except Exception as e:
        flash("Their was and issue unallocating the employees or deleting the company","danger")
        flash(str(e), "danger")

    
    # TODO delete-2 redirect to employee search
    return redirect(url_for('company.search', Name="", address="", website="", city="", country="", state="", zip="" ,limit=10))

    