"""
Text cleaning and formatting utilities.
"""
import re
from typing import str, List


def clean_whitespace(text: str) -> str:
    """
    Remove excessive whitespace from text.

    Args:
        text: Input text

    Returns:
        Cleaned text
    """
    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)
    # Remove leading/trailing whitespace
    text = text.strip()
    return text


def remove_html_tags(text: str) -> str:
    """
    Remove HTML tags from text.

    Args:
        text: Input text with HTML

    Returns:
        Text without HTML tags
    """
    # TODO: Consider using a proper HTML parser like BeautifulSoup for complex cases
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


def truncate_text(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """
    Truncate text to a maximum length.

    Args:
        text: Input text
        max_length: Maximum length
        suffix: Suffix to add when truncated

    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text

    return text[:max_length - len(suffix)].rstrip() + suffix


def format_bullet_list(items: List[str], bullet: str = "•") -> str:
    """
    Format a list of items as a bullet list.

    Args:
        items: List of items
        bullet: Bullet character

    Returns:
        Formatted bullet list string
    """
    if not items:
        return ""

    return "\n".join([f"{bullet} {item}" for item in items])


def extract_keywords(text: str, max_keywords: int = 5) -> List[str]:
    """
    Extract keywords from text (simple implementation).

    Args:
        text: Input text
        max_keywords: Maximum number of keywords

    Returns:
        List of keywords
    """
    # TODO: Implement more sophisticated keyword extraction
    # Consider using NLP libraries like spaCy or NLTK for better results

    # Simple implementation: extract common words
    words = text.lower().split()

    # Remove common stop words (basic list)
    stop_words = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at',
        'to', 'for', 'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are'
    }

    keywords = [word for word in words if word not in stop_words and len(word) > 3]

    # Return unique keywords
    unique_keywords = list(dict.fromkeys(keywords))
    return unique_keywords[:max_keywords]


def sanitize_user_input(text: str) -> str:
    """
    Sanitize user input to prevent injection attacks.

    Args:
        text: User input text

    Returns:
        Sanitized text
    """
    # Remove potentially dangerous characters
    # TODO: Customize based on your security requirements
    sanitized = text.replace('<', '&lt;').replace('>', '&gt;')
    sanitized = re.sub(r'[^\w\s\-.,!?@]', '', sanitized)
    return sanitized


def format_markdown_heading(text: str, level: int = 1) -> str:
    """
    Format text as markdown heading.

    Args:
        text: Heading text
        level: Heading level (1-6)

    Returns:
        Markdown formatted heading
    """
    level = max(1, min(6, level))  # Clamp between 1 and 6
    return f"{'#' * level} {text}"
