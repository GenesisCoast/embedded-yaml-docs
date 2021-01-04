class CommentParserError(Exception):
    """
    Custom class for a comment parser error.
    """

    def __init__(token, comment_block, message):
        """
        Constructor for the exception including all the details.
        """
        self.token = token
        self.comment_block = comment_block
        self.message = f"Error parsing the comment block \n {comment_block} from the token \n {token}. With the error message {message}"
        super().__init__(self.message)