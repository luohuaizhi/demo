# coding:utf-8
from django import template
from django.utils.safestring import mark_safe
from django.template.base import resolve_variable, Node, TemplateSyntaxError

register = template.Library()


@register.simple_tag
def f_w_u(sentence):
    """
    first word upper
    :param sentence:
    :return:
    """
    word_list = [w[0].upper+w[1:] for w in sentence.split(" ") if w]
    return mark_safe(" ".join(word_list))
