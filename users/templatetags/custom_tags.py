from django import template

register = template.Library()
import logging
logger = logging.getLogger(__name__)

@register.filter(name='add_attr')
def add_attr(field, attr):
    logger.info(f"Field type: {type(field)}")  # Log the type of the field
    if hasattr(field, 'as_widget'):
        attrs = {}
        definition = attr.split('=')
        if len(definition) == 2:
            key, value = definition
            attrs[key] = value
        return field.as_widget(attrs=attrs)
    return field  # Return the field unchanged if it's not a form field


