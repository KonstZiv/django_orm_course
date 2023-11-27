import init_django_orm  # noqa: F401

from db.models import LiteraryFormat, Book


def init():
    Book.objects.all().delete()
    LiteraryFormat.objects.all().delete()

    textbook = LiteraryFormat.objects.create(name="textbook")
    novel = LiteraryFormat.objects.create(name="novel")

    Book.objects.create(
        title="Learning Python",
        price=19.99,
        format=textbook
    )

    Book.objects.create(
        title="Refactoring. Improving the design of existing code",
        price=22.00,
        format=textbook
    )

    Book.objects.create(
        title="Cassandra",
        price=29.99,
        format=novel
    )

    Book.objects.create(
        title="Voroshilovgrad",
        price=19.99,
        format=novel
    )


def main():
    # init()
    novel = LiteraryFormat.objects.get(name="novel")
    novel.delete()


if __name__ == "__main__":
    main()
