class FormatData:
    """Format the account data into printable format: name, description and country."""

    def __init__(self, account):
        self.account = account

    def format_data(self):
        account_name = self.account["name"]
        account_desc = self.account["description"]
        account_country = self.account["country"]
        return f"{account_name}, a {account_desc}, from {account_country}"


class CheckAnswer:
    """Take the user guess and follower counts and returns if they got it right."""

    def __init__(self, guess, a_followers, b_followers):
        self.guess = guess
        self.a_followers = a_followers
        self.b_followers = b_followers

    def check_answer(self):
        if self.a_followers > self.b_followers:
            return self.guess == "a"
        else:
            return self.guess == "b"

