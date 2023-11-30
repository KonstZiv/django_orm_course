import init_django_orm  # noqa: F401

from services import books


def main():
    return books.retrieve(authors_ids=[1])


if __name__ == "__main__":
    # Test-Driven Development with Python,  Hary Percival
    #
    # Django ORM Cookbook, Shabda Raaj, Yash Rastogi
    print(main())
