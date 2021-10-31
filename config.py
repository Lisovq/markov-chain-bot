import mc

token: str = "..."

# If callback using
group_id: int = None
cb_confirm_token: str = "..."


class settings:
    syntax = mc.formatters.usual_syntax
    words_generate = mc.validators.words_count(1, 20)
    max_len_message: int = 2048
    random_send: bool = True


class patterns:
    from re import compile
    link = compile(
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|"
        r"[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    )
