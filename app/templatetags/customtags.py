from django import template


register = template.Library()

@register.filter
def time_fmt(num, unit='ms'):
    """Converts a time unit to a human-readable format."""
    units = {'ns': -9, 'µs': -6, 'ms': -3, 's': 0}
    time = num * 10**units[unit]
    return f'{time:.3f}s'

@register.filter
def memory_fmt(num, unit='KiB'):
    """Converts a memory unit to a human-readable format."""
    units = ('B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB')
    num <<= units.index(unit) * 10
    for u in units:
        if num < 1024:
            return f'{num:.2f} {u}'
        num /= 1024
    return f'{num:.2f} {u[-1]}'
