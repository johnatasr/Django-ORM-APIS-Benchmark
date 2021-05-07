from django.db.models import (
    Model,
    BooleanField,
    CharField,
    URLField,
    DateTimeField)

import json
import django_main

django_main.setup()


class Customer(Model):
    gender = CharField(max_length=100, db_index=True)
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    email = CharField(max_length=100)
    street = CharField(max_length=100)
    city = CharField(max_length=100)
    state = CharField(max_length=100)
    phone = CharField(max_length=100)
    domain = URLField(max_length=255, null=True)
    image_url = CharField(max_length=244)
    join_date = DateTimeField(auto_created=True, auto_now_add=True, null=True)
    is_active = BooleanField(default=True)

    def to_dict(self):
        return {
            'id': self.id,
            'domain': self.domain,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'street': self.street,
            'city': self.city,
            'state': self.state,
            'phone': self.phone,
            'image_url': self.image_url,
            'join_date': self.join_date.isoformat() if self.join_date else None,
            'is_active': self.is_active
        }

    def to_json(self):
        return json.dumps(self.to_dict())
