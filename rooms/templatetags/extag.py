from django import template


register = template.Library()


@register.filter()
def extag(value):
    print(value)
    return "this 123213123123123y124182is ex"
