class Job:
    def __init__(self, uid, company, location, name, description, posted_date, apply_link, expiration_date):
        self.id = uid
        self.company = company
        self.location = location
        self.name = name
        self.description = description
        self.posted_date = posted_date
        self.apply_link = apply_link
        self.expiration_date = expiration_date
