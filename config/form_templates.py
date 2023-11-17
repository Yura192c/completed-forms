from config.database import async_collection


async def add_templates():
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
        existing_template = await async_collection.find_one({"name": template["name"]})
        if existing_template is None:
            print('Template added')
            async_collection.insert_one(template)
        else:
            print('The template has already been added')
