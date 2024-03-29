def get_model_string(model, contact, char):
    qs = model.objects.filter(person=contact)
    text = ', '.join(qs.values_list(char, flat=True))
    if not text:
        return '---'
    return text + '.'
