import json
import os

from app import db, models
from datetime import datetime

import re

DATE_PATTERN = re.compile(r'\d{2}/\d{2}/\d{4}')


def load_fixture(file_path):
    """ загружаут содержимое фикстуры
    :param file_path: пусть до файла с фикстурой
    :retrun: данные из фикстуры либо пустой список, если не найдены

    """
    content = []
    if os.path.isfile(file_path):
        with open(file_path) as file:
            content = json.load(file)

    return content


def migration(fixture_path, model, convert_dates=False):
    fixture_content = load_fixture(fixture_path)
    # конвертация дат из формата

    for fixture in fixture_content:
        if convert_dates:
            for field_name, field_value in fixture.items():
                if isinstance(field_value, str) and field_value.count('/') == 2:
                    fixture[field_name] = datetime.strptime(field_value, '%m/%d/%Y')

            if db.session.query(models.Order).filter(model.Order.id == fixture['id']).first() is None:
                db.session.add(model.Order(**fixture))

    db.session.commit()


def migrate_user_roles(fixture_path):
    migration(
        fixture_path=fixture_path,
        model=models.UserRole,
    )


def migrate_users(fixture_path):
    migration(
        fixture_path=fixture_path,
        model=models.User
    )


def migrate_orders(fixture_path):
    migration(
        fixture_path=fixture_path,
        model=models.Order,
        convert_dates=True,
    )

def migrate_offers(fixture_path):
    migration(
        fixture_path=fixture_path,
        model=models.Offer,
    )
