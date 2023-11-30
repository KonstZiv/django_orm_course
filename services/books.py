from db.models import Book
from django.db.models import QuerySet


# Retrieve list
def retrieve(
        id_: int = None, /,
        title: str = None,
        format_id: int = None,
        price_from: float = None,
        price_to: float = None,
        authors_ids: list[int] = None
) -> QuerySet[Book] | Book:
    if id_:
        return Book.objects.get(id=id_)

    queryset = Book.objects.all()

    if title:
        queryset = queryset.filter(title=title)
    if format_id:
        queryset = queryset.filter(format_id=format_id)
    if price_from:
        queryset = queryset.filter(price__gte=price_from)
    if price_to:
        queryset = queryset.filter(price__lte=price_to)
    if authors_ids:
        queryset = queryset.filter(authors__id__in=authors_ids)

    return queryset


# Create
def create(title: str, price: float, format_id: int, authors_ids: list[int] = None) -> Book:

    new_book = Book.objects.create(
        title=title,
        price=price,
        format_id=format_id,
    )

    if authors_ids:
        new_book.authors.set(authors_ids)

    return new_book
