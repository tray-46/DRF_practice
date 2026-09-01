from rest_framework import serializers

FORBIDDEN_WORDS = ["ставки", "крипта", "продам", "гараж"]

class WordsValidator:

    def __call__(self, value):
        value = value.lower()
        for word in FORBIDDEN_WORDS:
            if word in value:
                raise serializers.ValidationError(f"Can't use {word} in dogs name.")


def validate_forbidden_words(value):
    if value.lower() in FORBIDDEN_WORDS:
        raise serializers.ValidationError(f"Can't use {value} in dogs name.")
