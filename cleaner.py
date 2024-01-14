import re

def remove_extra_spaces(html_content):
    """
    Function to remove all extra spaces from HTML content.
    It replaces two or more consecutive spaces with a single space.

    Parameters:
    html_content (str): A string containing HTML content.

    Returns:
    str: Modified HTML content with extra spaces removed.
    """
    # Using regular expression to replace two or more consecutive spaces with a single space
    return re.sub(r' {2,}', ' ', html_content)

# Example usage
html_example = "<html>  <body>    This is    a   test.  </body> </html>"
cleaned_html = remove_extra_spaces(html_example)
print(cleaned_html)
