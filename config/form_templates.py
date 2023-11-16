from config.database import collection


def add_templates():
    templates = [
        {
            "name": "User registration form",
            "user_name": "text",
            "user_email": "email",
            "user_password": "text",
            "user_date_of_birth": "date",
        },
        {
            "name": "OrderForm",
            "field_name_1": "text",
            "field_name_2": "date"
        }
    ]

    for template in templates:
        existing_template = collection.find_one({"name": template["name"]})
        if existing_template is None:
            print('Template added')
            collection.insert_one(template)
        else:
            print('The template has already been added')
