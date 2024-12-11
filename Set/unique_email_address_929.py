class EmailList:
    def get_unique_email_count(self, emails: [str]) -> int:
        # If localname has "+", remove everything from this "+" till str.end()
        # If localname has ".", remove it
        email_set = set()

        for email in emails:
            local, domain = email.split('@')

            # If localname has "+", remove everything from this "+" till str.end()
            local = local.split('+')[0]

            # If localname has ".", remove it
            local = local.replace(".", "")

            finalEmail = local + '@' + domain
            email_set.add(finalEmail)
        return len(email_set)


emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
emailList = EmailList()
print(emailList.get_unique_email_count(emails))