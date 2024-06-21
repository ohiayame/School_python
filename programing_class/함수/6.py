def wrap_in_tag(tag, msg):
    return f"<{tag}>{msg}<{tag}>"

print(wrap_in_tag('p', 'hello'))
print(wrap_in_tag('b', 'world'))