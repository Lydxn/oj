from django import template

register = template.Library()

@register.filter
def memory_fmt(num, unit='KiB'):
    """Converts a memory unit to a human-readable format."""
    units = ('B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB')
    num <<= units.index(unit) * 10
    for u in units:
        if num < 1024:
            return f'{num:,} {u}'
        num //= 1024
    return f'{num:,} {u[-1]}'
