def check_edit_permission(schema, context, request):
    for child in schema.children:
        if hasattr(child, 'edit_permission'):
            if not request.has_permission(child.edit_permission, context):
                del schema[child.name]
    return schema
