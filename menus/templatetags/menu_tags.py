from django import template
from django.utils.functional import cached_property

from menus.models import MenuItem

register = template.Library()


@register.inclusion_tag('menus/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    """
    Рисует меню по имени: {% draw_menu 'main_menu' %}
    Делает один запрос к БД.
    """
    request = context['request']
    current_path = request.path

    # 1 запрос к БД
    items_qs = (
        MenuItem.objects
        .filter(menu__name=menu_name)
        .select_related('parent', 'menu')
        .order_by('sort_order', 'id')
    )
    items = list(items_qs)

    # Собираем детей и ищем активный пункт
    children_map = {}
    active_item = None

    for item in items:
        # Сразу резолвим URL (явный или named)
        url = item.get_url()
        item.resolved_url = url

        if url == current_path:
            active_item = item

        parent_id = item.parent_id
        children_map.setdefault(parent_id, []).append(item)

    # Проставляем список детей всем пунктам (удобно в шаблонах)
    for item in items:
        item.children_list = children_map.get(item.id, [])

    # Множество id пунктов, которые должны быть "раскрыты"
    open_ids = set()
    if active_item:
        node = active_item
        while node is not None:
            open_ids.add(node.id)
            node = node.parent  # поднимаемся вверх по дереву

    # Корневые пункты (у которых нет parent)
    root_items = children_map.get(None, [])

    return {
        'menu_name': menu_name,
        'root_items': root_items,
        'open_ids': open_ids,
        'active_item': active_item,
        'request': request,
    }
