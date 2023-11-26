import init_django_orm  # noqa: F401

from db.models import LiteraryFormat


def main():
    filtered_formats = LiteraryFormat.objects.filter(
        format="sci-fi",
    ).delete()
    # print(LiteraryFormat.objects.all())
    print(filtered_formats)


if __name__ == "__main__":
    main()
