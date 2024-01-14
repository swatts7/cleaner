function removeExtraSpaces(htmlContent) {
    // Using regular expression to replace two or more consecutive spaces with a single space
    return htmlContent.replace(/ {2,}/g, ' ');
}

// Example usage
const htmlExample = "<html>  <body>    This is    a   test.  </body> </html>";
const cleanedHtml = removeExtraSpaces(htmlExample);
console.log(cleanedHtml);
