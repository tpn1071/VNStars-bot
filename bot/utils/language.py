def is_vietnamese(text: str) -> bool:
    vietnamese_chars = (
        "ăâđêôơưáàảãạấầẩẫậắằẳẵặéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ"
    )
    text_lower = text.lower()
    return any(c in vietnamese_chars for c in text_lower)


def is_english(text: str) -> bool:
    # Kiểm tra text chỉ gồm ký tự tiếng Anh (a-z) và space
    return all(c.isalpha() or c.isspace() for c in text) and not is_vietnamese(text)
