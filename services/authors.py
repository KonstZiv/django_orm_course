import warnings

from django.db.models import QuerySet

from db.models import Author


def retrieve(id_: int = None, /, first_name: str = None, last_name: str = None) -> QuerySet | Author:
    if id_ and (last_name or first_name):
        warnings.warn(
            f"""
            {retrieve.__name__} function, when passing an argument to id_, ignores other passed arguments.
            Arguments passed: id_ = {id_}, first_name = {first_name}, last_name = {last_name}.
            Ignored arguments: first_name = {first_name}, last_name = {last_name}.
            """
        )
    if id_:
        return Author.objects.get(id=id_)
    queryset = Author.objects.all()
    if first_name:
        queryset = queryset.filter(first_name=first_name)
    if last_name:
        queryset = queryset.filter(last_name=last_name)
    return queryset


def create(
        first_name: str,
        last_name: str
) -> Author:
    return Author.objects.create(
        first_name=first_name,
        last_name=last_name
    )
